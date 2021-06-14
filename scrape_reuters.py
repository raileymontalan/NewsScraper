# Web scraper for New York Times


# Import necessary libraries
import sys, requests, re
from bs4 import BeautifulSoup as bs

def download_page(url):
    """
    Download the HTML script of the provided page.
    """

    print("Attempting to download the page in {}\n".format(url))
    try:
        page = requests.get(url)
        content = page.content
        page.close()
        print("Page {} was downloaded successfully.\n".format(url))

        return content
    except:
        print("Could not download page from {}.\n".format(url))

def scrape_page(content):
    """
    Parse the page content to retriev the title, article body, and
    other metadata.
    """
    parser = bs(content, 'html.parser')

    title = parser.find_all('h1')
    body = parser.find_all('p', {'class': re.compile('ArticleBody')})
    byline = parser.find_all('p', {'class': re.compile('Byline')})

    print(title[0].text + '\n')
    print(byline[0].text + '\n')

    for i in body:
        print(i.text + '\n')


def main():
    """
    Execute program
    """
    try:
        url = str(sys.argv[1])
        content = download_page(url)
        scrape_page(content)
    except:
        print("No URL provided.")

main()