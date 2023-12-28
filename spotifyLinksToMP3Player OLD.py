import os
import shutil
import subprocess
from mutagen.easyid3 import EasyID3
import sys
import spotFuncs
import sys

#usage: python spotifylinkstomp3player.py link1 link2 link3 ...
# this script will download the songs from the links and move them to the mp3 player location
mp3_player_location = "D:\\albums"
download_location = "E:\\music\\unsorted"

def sanitize(filename):
    #remove illegal characters from filename (windows)
    illegal_characters = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    for c in illegal_characters:
        filename = filename.replace(c, "_")
    return filename

# 1. Pick album from Spotify
if len(sys.argv) > 1:
    links = sys.argv[1:]
else:
    links = spotFuncs.get_rand_albums()

print("Selected album links:")
for link in links:
    spotFuncs.printAlbumfromLink(link)

print("Downloading songs from Spotify...")

# 2. Tell spotdl to download files
results = []
for link in links:
    subprocess.run(["spotdl", link, "--output", download_location])
    results.extend(os.listdir(download_location))

print("Renaming and moving mp3 files...")

# 3. Rename and move mp3 files
for track in results:
    #get the filename
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
        #sanitize the filename
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
