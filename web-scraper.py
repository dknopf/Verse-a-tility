from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from bs4 import BeautifulSoup
import re #regular expressions
import csv

# Suppresses the opening of an actual browser window
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3') # Suppresses error messages

"""
Create a webdriver Object using url and returns the WebElement that contains the body tag

url: string
returns: WebElement object
"""
def set_up_webdriver(url):
    # Set webdriver to use Google Chrome
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)
    driver.get(url) # Navigates to the webpage listed
    content = driver.find_element_by_tag_name("body")
    return content

"""
Create a csv where each song in song_list is a new line, writing to song_list.csv

song_list: A list of strings that are songs
csv_given: A csv file
returns: None, modifies csv_given
"""
def write_songlist_csv(song_list, csv_given):
    with open(csv_given, 'a') as csvFile: # Opens it in append mode
        writer = csv.writer(csvFile)
        for song in song_list:
            writer.writerow([song])

    csvFile.close()

"""
Cleans the CSV by deleting duplicates, empty lists, and strings that are too long to be songs
Right now it doesn't handle extra puncutation such as commas and periods

CSV_given: an existing csv
Returns: None, just modifies csv_given
"""
def clean_csv(csv_given):
    list_of_unique_songs = []
    with open(csv_given, 'r') as csvReader: # Open csv_given in read mode
        reader = csv.reader(csvReader)
        for line in reader: # Iterate through each line (element) in the csv read file
            if line != [] and len(line[0]) < 25 and line[0] not in list_of_unique_songs:
                list_of_unique_songs.append(line[0])

    with open(csv_given, 'w') as csvWriter:
        writer = csv.writer(csvWriter)
        for song in list_of_unique_songs: # rewrite csv_given
            writer.writerow([song]) # Each row is a line containing the singleton set of each song in unique songs

    csvReader.close()
    csvWriter.close()

"""
Scrapes a google search page and creates a BeautifulSoup object of all the text in the page
then searches through every non-google link in the search page and applies a scraping
function to it

url: string, the url of a google search results page
function: function, a function which can scrape through a link
returns: None, runs function on each link in the search page
"""
def scrape_from_google(url, function):
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    driver.get(url) # Navigates to webpage listed
    content = driver.page_source # Content = the html(?) of the webpage given
    # content = set_up_webdriver_page_source(url)
    soup = BeautifulSoup(content, "lxml") #creates a BeautifulSoup object, which represents the document as a nested data structed
    for link in soup.find_all("a"):
        # Create a temporary variable 'url' that is equal to the href attribute of link
        temp_url = link.get('href')
        # Checks whether the url is None or not and whether or not it is a valid url
        if temp_url != None and temp_url[:5] == "https" and re.findall("google", temp_url) == []:
            function(temp_url)


"""
Scrapes the top karaoke songs from a link

url: string
returns: None, writes to a csv
"""
def scrape_top_karaoke_songs(url):
    songs_for_this_url = find_songs(url) # Creates a variable for the list of songs from temp_url
    write_songlist_csv(songs_for_this_url, 'song_list.csv') # writes to song_list.csv after each page so the code doesn't need to run all the way

"""
Takes a URL and finds all the strings of songs in it

url: string
returns: list
"""
def find_songs(url):
    # Create a temp webdriver
    content = set_up_webdriver(url)
    page_text = content.text # Gets the text that would be displayed on the webpage(url)
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
song_list_from_google = scrape_from_google("https://www.google.com/search?rlz=1C1CHFX_enUS704US704&ei=fYuzXdq9MY3b5gKxzITIBg&q=best+karaoke+songs&oq=best+karaoke+songs&gs_l=psy-ab.3..0i71l8.0.0..3240278...0.2..0.0.0.......0......gws-wiz.HjPC1IKlIYs&ved=0ahUKEwia8OGZzrjlAhWNrVkKHTEmAWkQ4dUDCAs&uact=5", scrape_top_karaoke_songs)

# Cleans the song_list.csv file
# clean_csv('song_list.csv')
