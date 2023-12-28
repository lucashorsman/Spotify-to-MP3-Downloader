import csv
import sys

# Get the album links from the command line arguments
links = sys.argv[1:]

# Open the CSV file in read mode ('r') to check for duplicates
with open('downloaded_albums.csv', 'r') as f:
    reader = csv.reader(f)
    existing_links = set(row[0] for row in reader)

    
x = 0;
# Open the CSV file in append mode ('a') and write the links to it
with open('downloaded_albums.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for link in links:
        if link not in existing_links:
            writer.writerow([link])
            existing_links.add(link)
            x+=1

print(f"Added {x} new album(s) to downloaded_albums.csv")

