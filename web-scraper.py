from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

# Set webdriver to use Google Chrome
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Test code for web scraping
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
