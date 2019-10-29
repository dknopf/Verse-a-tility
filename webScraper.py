from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from bs4 import BeautifulSoup
from cleanCSV import cleanCSV
import re #regular expressions
import csv

# Suppresses the opening of an actual browser window
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3') # Suppresses error messages
driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)


"""
Create a csv where each song in song_list is a new line, writing to csv_given and then cleaning it

song_list: A list of strings that are songs
csv_given: str, a csv file (will create one if the variable file doesn't exist)
returns: None, modifies and cleans csv_given
"""
def writeSonglistCSV(song_list, csv_given):
    with open(csv_given, 'a') as csvFile: # Opens it in append mode
        writer = csv.writer(csvFile)
        for song in song_list:
            writer.writerow([song])

    csvFile.close()
    cleanCSV(csv_given)

"""
Scrapes a google search page and creates a BeautifulSoup object of all the text in the page
then searches through every non-google link in the search page and applies a scraping
function to it

url: string, the url of a google search results page
function: function, a function which can scrape through a link
returns: None, runs function on each link in the search page
"""
def scrapeFromGoogle(url, function):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml") #creates a BeautifulSoup object, which represents the document as a nested data structed
    unique_links = []
    for link in soup.find_all("a"):
        # Create a temporary variable 'url' that is equal to the href attribute of link
        temp_url = link.get('href')
        if temp_url not in unique_links:
            unique_links.append(temp_url)
            # Checks whether the url is None or not and whether or not it is a valid url
            if temp_url != None and temp_url[:5] == "https" and re.findall("google", temp_url) == []:
                function(temp_url)


"""
Scrapes the top karaoke songs from a link

url: string
returns: None, writes to a csv
"""
def scrapeTopKaraokeSongs(url):
    songs_for_this_url = findSongs(url) # Creates a variable for the list of songs from temp_url
    writeSonglistCSV(songs_for_this_url, 'song_list.csv') # writes to song_list.csv after each page so the code doesn't need to run all the way

"""
Takes a URL and finds all the strings of songs in it

url: string
returns: list
"""
def findSongs(url):
    driver.get(url) # Navigates to the webpage listed
    page_text = driver.find_element_by_tag_name("body").text
    list_of_songs = []

    # Create a regular expression that checks if the regexp is preceeded by the
    # Open quote character and is any number of characters followed by the close quote character

    between_quotes = re.compile(r'(?<=“).*(?=”)')
    all_between_quotes = re.findall(between_quotes, page_text)
    list_of_songs += all_between_quotes

    # checks if preceeeded by a match for any \d is any digit, . is any char, (?=\s*-) checks if the NEXT string matches \s* (any white space chars) -

    between_num_dash = re.compile('\d*.*(?=\s*–)') #create a regexp that takes anything between a number and a dash
    all_num_dash_matches = re.findall(between_num_dash, page_text) # Get a list of all the matches of the regexp in the page
    list_of_songs += all_num_dash_matches

    return list_of_songs


#creates a song list from the google page for the search "best Karaoke songs"
first_google_karaoke_page = "https://www.google.com/search?rlz=1C1CHFX_enUS704US704&ei=fYuzXdq9MY3b5gKxzITIBg&q=best+karaoke+songs&oq=best+karaoke+songs&gs_l=psy-ab.3..0i71l8.0.0..3240278...0.2..0.0.0.......0......gws-wiz.HjPC1IKlIYs&ved=0ahUKEwia8OGZzrjlAhWNrVkKHTEmAWkQ4dUDCAs&uact=5"
second_google_karaoke_page = 'https://www.google.com/search?q=best+karaoke+songs&rlz=1C1CHFX_enUS704US704&sxsrf=ACYBGNSUVbGAY3wYZEeFcHS-g988vIDPPg:1572323047807&ei=5763XbDzMMOq_QbiwYmwBA&start=10&sa=N&ved=0ahUKEwjwgvLlz8DlAhVDVd8KHeJgAkYQ8tMDCOwC&biw=1536&bih=752'
third_google_karaoke_page = "https://www.google.com/search?q=best+karaoke+songs&rlz=1C1CHFX_enUS704US704&sxsrf=ACYBGNQMBfiNSRNdcKWlCnhEd4tvmuecqQ:1572323051452&ei=6763XYyVG8-k_Qb5kYWACw&start=20&sa=N&ved=0ahUKEwjMttDnz8DlAhVPUt8KHflIAbA4ChDy0wMIhwE&biw=1536&bih=752"
fourth_google_karaoke_page = "https://www.google.com/search?q=best+karaoke+songs&rlz=1C1CHFX_enUS704US704&sxsrf=ACYBGNTWVdePOUWYNiaEQBWdRhG__7cuMw:1572323189665&ei=db-3XbyQKKiyggff17voBw&start=30&sa=N&ved=0ahUKEwj8nsSp0MDlAhUomeAKHd_rDn04FBDy0wMIhwE&biw=1536&bih=752"
song_list_from_google = scrapeFromGoogle(first_google_karaoke_page, scrapeTopKaraokeSongs)
