from webpage_summarizer import WebPageSummarizer

if __name__ == "__main__":
    # Add the webpage url you want to summarize
    website = WebPageSummarizer("https://cnn.com")
    website.display_summary()