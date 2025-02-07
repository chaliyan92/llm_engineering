from webpage_summarizer import WebPageSummarizer
        
if __name__ == "__main__":

    # Add the webpage url you want to summarize
    website = WebPageSummarizer("https://cnn.com")
    # pass the the flag use_openai=True to use OpenAI for summarization
    # otherwise, the locally running Ollama server will be used
    website.display_summary(use_openai=True) 