import logging
import json
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown
from common.utils.openai_util import OpenAIUtils
from common.utils.request_util import RequestUtil

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CompanyBrochure:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url

    def scrape_website(self, response):
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.title = soup.title.string if soup.title else "No title found"
            if soup.body:
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                self.text = soup.body.get_text(separator="\n", strip=True)
            else:
                self.text = ""
            links = [link.get('href') for link in soup.find_all('a')]
            self.links = [link for link in links if link]
        except Exception as e:
            logger.error(f"An error occurred while scraping the website: {e}")
            return None
        
    def return_links(self):
        return self.links
        
    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"

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
    
    def get_brochure_user_prompt(self, company_name):
        user_prompt = f"You are looking at a company called: {company_name}\n"
        user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
        user_prompt += self.get_all_details()
        user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
        return user_prompt

    def get_links_user_prompt(self):
        user_prompt = f"Here is the list of links on the website of {self.url} - "
        user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
        Do not include Terms of Service, Privacy, email links.\n"
        user_prompt += "Links (some might be relative links):\n"
        user_prompt += "\n".join(self.return_links())
        return user_prompt
    
    # def get_all_details(url):
    #     result = "Landing page:\n"
    #     result += Website(url).get_contents()
    #     links = get_links(url)
    #     print("Found links:", links)
    #     for link in links["links"]:
    #         result += f"\n\n{link['type']}\n"
    #         result += Website(link["url"]).get_contents()
    #     return result
    
    def send_request(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = RequestUtil.get(url, headers=headers)
        if response is None:
            raise ValueError("Failed to fetch the webpage.")
        return response
    
    def get_website_content(self, url):
        print(url + " {}{}{}{}{}{}{}")
        response = self.send_request(url)
        self.scrape_website(response)
        return self.get_contents()

    def get_all_details(self):
        openai_util = OpenAIUtils()
        result = "Landing page:\n"
        result += self.get_website_content(self.url)
        links = openai_util.generate_response(self.link_system_prompt(), self.get_links_user_prompt())
        try:
            json_output = json.loads(links)
            print(json_output)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Raw response content: {links}")
        if "links" not in json_output:
            return None
        for link in json_output["links"]:
            print(link)
            result += f"\n\n{link['type']}\n"
            result += self.get_website_content(link["url"])
        return result
    
    def print_markdown(self, content):
        console = Console()
        md = Markdown(content)
        console.print(md)

    def create_brochure(self, company_name):
        openai_util = OpenAIUtils() # initiate this in the constructor and keep it in a var
        response = openai_util.generate_response(self.brochure_system_prompt(), self.get_brochure_user_prompt(company_name))
        self.print_markdown(response)