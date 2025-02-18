import logging
import json
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown
from common.utils.request_util import RequestUtil

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CompanyBrochure:

    def __init__(self, company_name, url, openai_util=None):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.company_name = company_name
        self.url = url
        self.openai_util = openai_util

    def scrape_website(self, response):
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            if soup.body:
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                text = soup.body.get_text(separator="\n", strip=True)
            else:
                text = ""
            links = [link.get('href') for link in soup.find_all('a')]
            inner_links = [link for link in links if link]
            return [title, text, inner_links]  
        except Exception as e:
            logger.error(f"An error occurred while scraping the website: {e}")
            return None
        
    def return_links(self):
        return self.links
        
    def get_contents(self, title=None, text=None):
        return f"Webpage Title:\n{title}\nWebpage Contents:\n{text}\n\n"

    def link_system_prompt(self):
        link_system_prompt = "You are provided with a list of links found on a webpage. \
        You are able to decide which of the links would be most relevant to include in a brochure about the company, \
        such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
        link_system_prompt += "You should respond in JSON as in this example:"
        link_system_prompt += """
        {
            "links": [
                {"type": "about page", "url": "https://full.url/goes/here/about"},
                {"type": "careers page": "url": "https://another.full.url/careers"}
            ]
        }
        """
        return link_system_prompt
    
    def brochure_system_prompt(self):
        return "You are an assistant that analyzes the contents of several relevant pages from a company website \
        and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
        Include details of company culture, customers and careers/jobs if you have the information."
    
    def get_brochure_user_prompt(self, company_name, full_website_contents=None):
        user_prompt = f"You are looking at a company called: {company_name}\n"
        user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
        user_prompt += full_website_contents if full_website_contents else ""
        user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
        return user_prompt

    def get_links_user_prompt(self, url, inner_links):
        user_prompt = f"Here is the list of links on the website of {url} - "
        user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
        Do not include Terms of Service, Privacy, email links.\n"
        user_prompt += "Links (some might be relative links):\n"
        user_prompt += "\n".join(inner_links)
        return user_prompt

    def send_request(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = RequestUtil.get(url, headers=headers)
        if response is None:
            raise ValueError("Failed to fetch the webpage.")
        return response
    
    def get_website_content(self, url):
        response = self.send_request(url)
        title, text, inner_links = self.scrape_website(response)
        return title, text, inner_links

    def get_all_details(self,  full_website_content, processed_links):
        result = "Landing page:\n"
        result += full_website_content

        try:
            json_output = json.loads(processed_links)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
            logger.error(f"Raw response content: {processed_links}")
        if "links" not in json_output:
            return None
        for link in json_output["links"]:
            result += f"\n\n{link['type']}\n"
            title, text = self.get_website_content(link["url"])
            result += self.get_contents(title, text)
        return result
    
    def print_markdown(self, content):
        if content is None:
            logger.error("No content to display.")
            return
        console = Console()
        md = Markdown(content)
        console.print(md)

    def create_brochure(self):
        title, text, inner_links = self.get_website_content(self.url)
        links_user_message = self.get_links_user_prompt(self.url, inner_links)
        processed_links = self.openai_util.generate_response(self.link_system_prompt(), links_user_message, response_type="json_object")
        base_website_content = self.get_contents(title, text)
        full_website_contents = self.get_all_details(base_website_content, processed_links)
        brochure_user_prompt =  self.get_brochure_user_prompt(self.company_name, full_website_contents)
        response = self.openai_util.generate_response(self.brochure_system_prompt(), brochure_user_prompt)
        self.print_markdown(response)