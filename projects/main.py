from web_page_summarizer.webpage_summarizer import WebPageSummarizer
from company_brochure.company_brochure import CompanyBrochure

if __name__ == "__main__":


    CompanyBrochure("https://huggingface.co").create_brochure("Hugging Face")
    ''' 
    Add the webpage url you want to summarize
    pass the the flag use_openai=True to use OpenAI for summarization
    otherwise, the locally running Ollama server will be used
    '''
    # website = WebPageSummarizer("https://cnn.com")
    # website.display_summary(use_openai=True) 