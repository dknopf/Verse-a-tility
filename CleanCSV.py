import re
import csv


"""
Cleans the CSV by deleting duplicates, empty lists, and strings that are too long to be songs
Right now it doesn't handle extra puncutation such as commas and periods

CSV_given: an existing csv
Returns: None, just modifies csv_given
"""
def cleanCSV(csv_given):
    list_of_unique_songs = []
    with open(csv_given, 'r') as csvReader: # Open csv_given in read mode
        reader = csv.reader(csvReader)
        for line in reader: # Iterate through each line (element) in the csv read file
            if line != []:
                clean_title = re.sub(r'\.\s*|,|\”|\’|\'|\“|\(|\)\s*|\"|\'|\!|\?|^\s+|\s+$|[0-9]', '', str(line[0]).lower())
                if len(clean_title) < 25 and clean_title not in list_of_unique_songs:
                    list_of_unique_songs.append(clean_title)

    with open(csv_given, 'w') as csvWriter:
        writer = csv.writer(csvWriter)
        for song in list_of_unique_songs: # rewrite csv_given
            writer.writerow([song]) # Each row is a line containing the singleton set of each song in unique songs

    csvReader.close()
    csvWriter.close()
