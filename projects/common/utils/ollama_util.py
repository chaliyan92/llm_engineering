import os
import logging
import ollama

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OllamaUtils:

    def __init__(self):
        pass

    # calls the locally running ollama server to generate a response
    def generate_response(self, system_prompt, user_prompt, model="llama3.2"):
        try:
            response = ollama.chat(model=model, messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ])
            logger.info(f"Using model: {model} with ollama")
            return response['message']['content']
        except Exception as e:
            logger.error(f"Error summarizing text: {e}")
            return None
