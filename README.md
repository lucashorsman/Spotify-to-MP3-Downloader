# Spotify-to-MP3-Downloader

This Python script downloads albums from Spotify and moves them to a specified location. It also keeps track of already downloaded albums to avoid duplicates.

## Files

- `sp2mp3.py`: The main script. It takes Spotify album links as command line arguments, downloads the songs, and moves them to the specified location.

- `spotFuncs.py`: This file contains functions related to interacting with Spotify, such as fetching album information and generating download links.

- `add_albums_to_csv.py`: This script takes a list of album links from the command line and appends them to the `downloaded_albums.csv` file. This is useful for manually adding albums to the list of downloaded albums.

- `downloaded_albums.csv`: This CSV file keeps track of the albums that have already been downloaded. Each line in the file represents one album. The script checks this file before downloading an album to ensure it hasn't been downloaded before.

## Usage

Run the main script with the Spotify album links as command line arguments:

```bash
python sp2mp3.py link1 link2 link3 ...
```

The script will download the songs from the links and move them to the location specified in the mp3_player_location variable.

## Configuration
You can configure the download and destination locations by modifying the following variables in the sp2mp3.py script:

mp3_player_location: The location of the mp3 player. The downloaded albums will be moved to this location.
download_location: The location to download the songs.
#Dependencies
This script requires the following Python libraries:

os, shutil, subprocess, sys: for file operations and running commands

mutagen.easyid3: for handling ID3 tags in MP3 files

concurrent.futures: for parallel processing

csver: custom module for handling CSV files

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
