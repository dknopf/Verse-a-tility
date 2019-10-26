from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from bs4 import BeautifulSoup
import re
# import pandas as pd

# Suppresses the opening of an actual browser window
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create a webdriver Object using url and returns the page that the driver is on
def set_up_webdriver_page_source(url):
    # Set webdriver to use Google Chrome
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    # Navigates to the webpage listed
    driver.get(url)


    content = driver.find_element_by_tag_name("body")
    #Unsure what this does but it was in the tutorial I found online

    # content = driver.page_source
    return content

def scrape_from_google(url):
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    # Navigates to the webpage listed
    driver.get(url)


    # content = driver.find_element_by_tag_name("body")
    #Unsure what this does but it was in the tutorial I found online

    content = driver.page_source
    # content = set_up_webdriver_page_source(url)
    soup = BeautifulSoup(content, "lxml") #creates a BeautifulSoup object, which represents the document as a nested data structed
    for link in soup.find_all("a"):
        # Create a temporary variable 'url' that is equal to the href attribute of link
        temp_url = link.get('href')
        # Checks whether the url is None or not and whether or not it is a valid url
        overall_song_list = []
        if temp_url != None and temp_url[:5] == "https" and re.findall("google", temp_url) == []:
            songs_for_this_url = find_songs(temp_url)
            overall_song_list.append(songs_for_this_url)
            print("song list for", temp_url, "is", songs_for_this_url)
    return(overall_song_list)


# Takes a URL and finds all the strings of songs in it
def find_songs(url):
    # Create a temp webdriver
    content = set_up_webdriver_page_source(url)
    page_text = content.text
    # webpage_soup = BeautifulSoup(content)
    # page_text = webpage_soup.get_text()
    print ("PAGE TEXT STARTS", page_text, "PAGE TEXT ENDS")
    seen_open_quote = False
    list_of_songs = []
    i = 0
    while i < len(page_text):
        if page_text[i] == '“' and seen_open_quote == False:
            open_quote_index = i + 1
            seen_open_quote = True
        elif page_text[i] == '”' and seen_open_quote == True:
            list_of_songs.append(page_text[open_quote_index:i])
            seen_open_quote = False
        i += 1

    count = 0
    count_chars_btwn = 0
    seen_num = False
    first_num_seen = 0
    while count < len(page_text):
        if isinstance(page_text[count], int) == True and seen_num == False:
            seen_num == True
            first_num_seen = i
        elif seen_num == True and count_chars_btwn < 20 and page_text[count] == "–":
            list_of_songs.append(page_text[i:count])
            count += 1
            seen_num = False
            count_chars_btwn = 0
        elif seen_num == True and count_chars_btwn < 20:
            count_chars_btwn += 1
            count += 1

    position = 0
    between_num_dash = re.compile("[0-9]+.{5,20}(-|—|–)") #create a regexp that takes anything between a number and a dash
    all_num_dash_matches = re.findall(between_num_dash, page_text) # Get a list of all the matches of the regexp in the page
    print("all_num_dash_matches is", all_num_dash_matches)
    list_of_songs.append(all_num_dash_matches)
    # while position < len(page_text):
    #     match = between_num_dash.search(page_text, position)
    #     if match != None:
    #         list_of_songs.append(match.group(0))
    #         position += match.end(0)
    #     else:
    #         break

    return list_of_songs
    # between_quotes = re.compile(r'.*\".*\"')
    # match = webpage_soup.find_all(between_quotes)

    # result = between_quotes.search(page_text).group(0)
    # print("match is", match)
    # return match

print(scrape_from_google("https://www.google.com/search?rlz=1C1CHFX_enUS704US704&ei=fYuzXdq9MY3b5gKxzITIBg&q=best+karaoke+songs&oq=best+karaoke+songs&gs_l=psy-ab.3..0i71l8.0.0..3240278...0.2..0.0.0.......0......gws-wiz.HjPC1IKlIYs&ved=0ahUKEwia8OGZzrjlAhWNrVkKHTEmAWkQ4dUDCAs&uact=5"))

# print(find_songs("https://www.timeout.com/newyork/music/the-50-best-karaoke-songs-ever"))
