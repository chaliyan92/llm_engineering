import gradio as gr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def system_message():
    return "You are a helpful assistant that can chat with users. Respond in a helpful manner."

class ChatBot:
    def __init__(self, openai=None):
        self.openai = openai

    def chat(self, user_message, history):
        logger.info("Received message: %s", user_message)
        logger.info("History: %s", history)
        for value in self.openai.generate_response(system_message(), user_message, history_messages=history, stream=True):
            yield value

    def launch_chatbot(self):
        gr.ChatInterface(fn=self.chat, type="messages", title="Simple Chatbot").launch()
