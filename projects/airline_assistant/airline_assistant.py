import logging
import json
import gradio as gr

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def system_message():
    system_message = "You are a helpful assistant for an Airline called FlightAI. "
    system_message += "Give short, courteous answers, no more than 1 sentence. "
    system_message += "Always be accurate. If you don't know the answer, say so."
    return system_message

def get_ticket_price(destination_city):
    # Dummy implementation for ticket pricing
    prices = {
        "NEW YORK": "300 USD",
        "LOS ANGELES": "350 USD",
        "CHICAGO": "250 USD",
        "HOUSTON": "200 USD",
        "MIAMI": "280 USD"
    }
    destination_upper = destination_city.upper()
    price = prices.get(destination_upper, "Destination not available")
    logger.info("Selected city: %s, Price: %s", destination_upper, price)
    return price

# There's a particular dictionary structure that's required to describe our function:

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'How much is a ticket to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

# We have to write that function handle_tool_call:
def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    logger.info("Received tool call: %s", tool_call)
    arguments = json.loads(tool_call.function.arguments)
    logger.info("Arguments: %s", arguments)
    city = arguments.get('destination_city')
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city,"price": price}),
        "tool_call_id": tool_call.id
    }
    return response, city

class AirlineAssistant:
    def __init__(self, openai=None):
        self.openai = openai

    def chat(self, user_message, history):
        logger.info("Received message: %s", user_message)
        logger.info("History: %s", history)
        message_list = (
                [{"role": "system", "content": system_message()}]
                + history
                + [{"role": "user", "content": user_message}]
        )
        response = self.openai.generate_response_with_tools(message_list,  tools=[{"type": "function", "function": price_function}])
        if response.choices[0].finish_reason=="tool_calls":
            message = response.choices[0].message
            logger.info("***** Received message from response: %s", message)
            response, city = handle_tool_call(message)
            message_list.append(message)
            message_list.append(response)
            response = self.openai.generate_response_with_tools(messages=message_list)
    
        return response.choices[0].message.content

    def launch_chatbot(self):
        gr.ChatInterface(fn=self.chat, type="messages", title="Airline Assistant").launch()

