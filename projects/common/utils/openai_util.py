import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OpenAIUtils:
    def __init__(self):
        load_dotenv(override=True)
        api_key = os.getenv('OPENAI_API_KEY')

        # Check the key
        if not api_key:
            logger.error("No API key was found - please make sure to include an .env file with your OpenAI API key "
                         "with the name OPENAI_API_KEY")
            exit(-1)
        self.openai = OpenAI(api_key=api_key)

    def generate_response(self, system_prompt, user_prompt, history_messages=None, model="gpt-4o-mini",
                          response_type="text", stream=False):
        if history_messages is None:
            history_messages = []
        message_list = (
                [{"role": "system", "content": system_prompt}]
                + history_messages
                + [{"role": "user", "content": user_prompt}]
        )
        logger.info(f"Message list: {message_list}")
        try:
            logger.info(f"Using model: {model} with openai with response type: {response_type} and streaming: {stream}")
            response = self.openai.chat.completions.create(
                model=model,
                messages=message_list,
                response_format={"type": response_type},
                stream=stream
            )
            if response:
                result = ""
                for chunk in response:
                    result += chunk.choices[0].delta.content or ""
                    yield result
            else:
                return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error summarizing text: {e}")
            return None
