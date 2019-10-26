from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set webdriver to use Google Chrome
driver = webdriver.Chrome()

# Test code for web scraping
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

# Navigates to the webpage listed
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

#Unsure what this does but it was in the tutorial I found online
# content = driver.page_source
soup = BeautifulSoup(content) #creates a BeautifulSoup object, which represents the document as a nested data structed
for a in soup.find_all("a"):
    print(a.get('href'))
    # temporary_webdriver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    # temporary_webdriver.get(a.get('href'))
