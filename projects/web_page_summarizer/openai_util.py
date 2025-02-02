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
            logger.error("No API key was found - please make sure to include an .env file with your OpenAI API key with the name OPENAI_API_KEY")
            exit(-1)
        self.openai = OpenAI(api_key=api_key)

    def summarize_text(self, system_prompt, user_prompt, model="gpt-4o-mini"):
        try:
            response = self.openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error summarizing text: {e}")
            return None
