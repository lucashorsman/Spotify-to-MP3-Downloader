import os
import shutil
import subprocess
from mutagen.easyid3 import EasyID3
import sys
import spotFuncs
import concurrent.futures
import csver

# Usage: python spotifylinkstomp3player.py link1 link2 link3 ...
# This script will download the songs from the links and move them to the mp3 player location

mp3_player_location = "D:\\albums"  # Location of the mp3 player
download_location = "E:\\music\\unsorted"  # Location to download the songs

def sanitize(filename):
    # Remove illegal characters from filename (Windows)
    illegal_characters = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    for c in illegal_characters:
        filename = filename.replace(c, "_")
    return filename

# Load the list of already downloaded albums from the CSV file
downloaded_albums = set()
with open('downloaded_albums.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            downloaded_albums.add(row[0])

# 1. Pick album from Spotify
if len(sys.argv) > 1:
    links = sys.argv[1:]  # Get album links from command line arguments
else:
    links = spotFuncs.get_rand_albums()  # Get random album links using spotFuncs

if len(links) == 1:
    link = links[0]
    if link in downloaded_albums:
        print("Album already downloaded. Exiting script.")
        sys.exit()

print("Selected album links:")
for link in links:
    spotFuncs.printAlbumfromLink(link)  # Print album details from the link

# Remove already downloaded albums from the list
links = [link for link in links if link not in downloaded_albums]
if not links:
    print("All albums are already downloaded. Exiting script.")
    sys.exit()

print("Downloading songs from Spotify...")

# 2. Tell spotdl to download files
results = []
def download(link):
    subprocess.run(["spotdl", link, "--output", download_location])  # Download songs using spotdl
    return os.listdir(download_location)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_to_link = {executor.submit(download, link): link for link in links}
    for future in concurrent.futures.as_completed(future_to_link):
        results.extend(future.result())

# Add the downloaded albums to the list and save it back to the CSV file
with open('downloaded_albums.csv', 'a') as f:
    writer = csv.writer(f)
    for link in links:
        writer.writerow([link])

print("Renaming and moving mp3 files...")

# 3. Rename and move mp3 files
for track in results:
    # Get the filename
    old_filename = os.path.join(download_location, track)
    if os.path.isfile(old_filename):
        # Extract metadata
        audio = EasyID3(old_filename)
        title = audio.get('title', [track])[0]
        track_number = audio.get('tracknumber', ['Unknown'])[0].split('/')[0]
        track_number = track_number.zfill(2)  # Add leading zeros if necessary
        artist_name = audio.get('artist', ['Unknown Artist'])[0].split('/')[0]
        album_name = audio.get('album', ['Unknown Album'])[0]
        
        # Rename and move the file
        # Sanitize the filename
        title = sanitize(title)
        artist_name = sanitize(artist_name)
        album_name = sanitize(album_name)
        
        new_filename = f"{download_location}/{track_number}-{title}-{artist_name}.mp3"
        new_directory = os.path.dirname(new_filename)
        os.makedirs(new_directory, exist_ok=True)
        shutil.move(old_filename, new_filename)
        
        # Move the file to mp3 player location if it doesn't already exist
        album_directory = f"{mp3_player_location}/{album_name}-{artist_name}"
        os.makedirs(album_directory, exist_ok=True)
        destination_file = f"{album_directory}/{os.path.basename(new_filename)}"
        if not os.path.exists(destination_file):
            shutil.move(new_filename, destination_file)

print("Songs downloaded and moved successfully!")
