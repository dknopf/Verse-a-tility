from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from bs4 import BeautifulSoup
import re
import csv
# import pandas as pd

# Suppresses the opening of an actual browser window
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3')

# Create a webdriver Object using url and returns the page that the driver is on
def set_up_webdriver_page_source(url):
    # Set webdriver to use Google Chrome
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    # Navigates to the webpage listed
    driver.get(url)

    # The content is the body of the webpage
    content = driver.find_element_by_tag_name("body")
    return content


# Create a csv where each song in song_list is a new line, writing to song_list.csv
def write_songlist_csv(song_list, csv_given):
    with open(csv_given, 'a') as csvFile:
        writer = csv.writer(csvFile)
        for song in song_list:
            writer.writerow([song])

    csvFile.close()


def clean_csv(csv_given):
    list_of_unique_songs = []
    with open(csv_given, 'r') as csvReader:
        reader = csv.reader(csvReader)
        # lines = list(reader)
        # print(lines[:10])
        for line in reader:
            # print(line)
            if line != [] and len(line[0]) < 25 and line[0] not in list_of_unique_songs:
            #     for i in range(len(line[0])):
            #         first_quote = -99
            #         if line[0][i] == '"' and first_quote == -99:
            #             first_quote = i
            #         elif line[0][i] == '"' and first_quote != -99:
            #             list_of_unique_songs.append(line[0][:first_quote] + line[0][first_quote + 1: i])
                list_of_unique_songs.append(line[0])
            # else:
            #     if len(line[0]) > 15:
            #         lines.remove(element)
            #     elif element[0] not in list_of_unique_songs:
            #         list_of_unique_songs.append(element[0])
            #     elif element[0] in list_of_unique_songs:
            #         lines.remove(element)








        # print(lines[:15])
        # for i in range(len(lines)):
        #     if lines[i] == []:
        #         lines.remove(lines[i])
        #     else: # Len > 0
        #         row = lines[i][0]
        #         if len(row) > 25:
        #             lines.remove(row)
        #         elif row not in list_of_unique_songs:
        #             list_of_unique_songs.append(row)
        #             print("unique songs are", list_of_unique_songs)
        #         elif row in list_of_unique_songs:
        #             lines.remove(row)
        print(list_of_unique_songs[:10])
            # else:
            #     for index in len(range(row)):
            #         if row[index] == '"':
            #             lines[row] = row[:index] + row[index + 1:]

    with open(csv_given, 'w') as csvWriter:
        writer = csv.writer(csvWriter)
        for song in list_of_unique_songs:
            writer.writerow([song])

    csvReader.close()
    csvWriter.close()


def scrape_from_google(url):
    driver = webdriver.Chrome('C:/Users/daniel/Downloads/chromedriver_win32/chromedriver.exe', options=options)

    driver.get(url) # Navigates to webpage listed
    content = driver.page_source # Content = the html(?) of the webpage given
    # content = set_up_webdriver_page_source(url)
    soup = BeautifulSoup(content, "lxml") #creates a BeautifulSoup object, which represents the document as a nested data structed
    for link in soup.find_all("a"):
        # Create a temporary variable 'url' that is equal to the href attribute of link
        temp_url = link.get('href')
        # Checks whether the url is None or not and whether or not it is a valid url
        overall_song_list = []
        if temp_url != None and temp_url[:5] == "https" and re.findall("google", temp_url) == []:
            songs_for_this_url = find_songs(temp_url) # Creates a variable for the list of songs from temp_url
            write_songlist_csv(songs_for_this_url, 'song_list.csv') # writes to song_list.csv after each page so the code doesn't need to run all the way
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
    # print ("PAGE TEXT STARTS", page_text, "PAGE TEXT ENDS")
    seen_open_quote = False
    list_of_songs = []
    i = 0
    while i < len(page_text):
        if (page_text[i] == '“' or page_text[i] == '"') and seen_open_quote == False:
            open_quote_index = i + 1
            seen_open_quote = True
        elif (page_text[i] == '”' or page_text[i] == '"') and seen_open_quote == True:
            list_of_songs.append(page_text[open_quote_index:i])
            seen_open_quote = False
        i += 1

    # Create a while loop that checks if there is a string that starts with a number then has at most 20 chars
    # Before ending in a dash
    # count = 0
    # count_chars_btwn = 0
    # seen_num = False
    # first_num_seen = 0
    # while count < len(page_text):
    #     if isinstance(page_text[count], int) == True and seen_num == False:
    #         seen_num == True
    #         first_num_seen = count
    #         count += 1
    #     elif seen_num == True and count_chars_btwn < 20 and page_text[count] == "–":
    #         list_of_songs.append(page_text[first_num_seen:count])
    #         count += 1
    #         seen_num = False
    #         count_chars_btwn = 0
    #     elif seen_num == True and count_chars_btwn < 20:
    #         count_chars_btwn += 1
    #         count += 1
    #     elif seen_num == True and count_chars_btwn > 20:
    #         seen_num = False
    #         count_chars_btwn = 0
    #         count += 1
    #     else:
    #         count += 1

    #attempt using regexps to create a regexps that is [num]+ at most 20 chars "-"
    # checks if preceeeded by a match for any \d is any digit, . is any char, (?=\s*-) checks if the NEXT string matches \s* (any white space chars) -
    between_num_dash = re.compile('\d*.*(?=\s*–)') #create a regexp that takes anything between a number and a dash
    all_num_dash_matches = re.findall(between_num_dash, page_text) # Get a list of all the matches of the regexp in the page
    list_of_songs += all_num_dash_matches

    # position = 0
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

# song_list_from_google = scrape_from_google("https://www.google.com/search?rlz=1C1CHFX_enUS704US704&ei=fYuzXdq9MY3b5gKxzITIBg&q=best+karaoke+songs&oq=best+karaoke+songs&gs_l=psy-ab.3..0i71l8.0.0..3240278...0.2..0.0.0.......0......gws-wiz.HjPC1IKlIYs&ved=0ahUKEwia8OGZzrjlAhWNrVkKHTEmAWkQ4dUDCAs&uact=5")

# print(find_songs("https://www.timeout.com/newyork/music/the-50-best-karaoke-songs-ever"))
clean_csv('song_list.csv')
