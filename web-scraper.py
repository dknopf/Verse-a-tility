from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from bs4 import BeautifulSoup
import re
import pandas as pd

# Suppresses the opening of an actual browser window
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create a webdriver Object using url and returns the page that the driver is on
def set_up_webdriver_page_source(url):
    # Set webdriver to use Google Chrome
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    # Navigates to the webpage listed
    driver.get(url)

    #Unsure what this does but it was in the tutorial I found online
    content = driver.page_source
    return content

def create_soup(url):
    content = set_up_webdriver_page_source(url)
    soup = BeautifulSoup(content, "lxml") #creates a BeautifulSoup object, which represents the document as a nested data structed
    for link in soup.find_all("a"):
        # Create a temporary variable 'url' that is equal to the href attribute of link
        temp_url = link.get('href')
        # Checks whether the url is None or not and whether or not it is a valid url
        if temp_url != None and temp_url[:5] == "https" and temp_url[13:20] != "google":
            return find_songs(temp_url)



# Takes a URL and finds all the strings of songs in it
def find_songs(url):
    # Create a temp webdriver
    content = set_up_webdriver_page_source(url)
    webpage_soup = BeautifulSoup(content, "lxml")
    # page_text = webpage_soup.get_text()
    between_quotes = re.compile('.*".*"')
    match = webpage_soup.find(string=between_quotes)
    # between_num_dash = re.compile('[0-9][0-9]*.* (- + -- + —)')
    # result = between_quotes.search(page_text).group(0)
    print(match)
    return match

create_soup("https://www.google.com/search?rlz=1C1CHFX_enUS704US704&ei=fYuzXdq9MY3b5gKxzITIBg&q=best+karaoke+songs&oq=best+karaoke+songs&gs_l=psy-ab.3..0i71l8.0.0..3240278...0.2..0.0.0.......0......gws-wiz.HjPC1IKlIYs&ved=0ahUKEwia8OGZzrjlAhWNrVkKHTEmAWkQ4dUDCAs&uact=5")
