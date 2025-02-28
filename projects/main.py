# from web_page_summarizer.webpage_summarizer import WebPageSummarizer
# from company_brochure.company_brochure import CompanyBrochure
# from chatbot.chatbot import ChatBot
from common.utils.openai_util import OpenAIUtils
from airline_assistant.airline_assistant import AirlineAssistant

if __name__ == "__main__":

    AirlineAssistant(OpenAIUtils()).launch_chatbot()

    # ChatBot(OpenAIUtils()).launch_chatbot()

    # CompanyBrochure("Hugging Face", "https://huggingface.co", OpenAIUtils()).create_brochure()
    ''' 
    Add the webpage url you want to summarize
    pass the the flag use_openai=True to use OpenAI for summarization
    otherwise, the locally running Ollama server will be used
    '''
    # website = WebPageSummarizer("https://cnn.com")
    # website.display_summary(use_openai=True) 