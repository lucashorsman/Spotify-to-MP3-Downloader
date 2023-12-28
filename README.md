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
It is also possible run the script without command line arguments, and the script will select 3 random saved albums from the user's spotify account. 
(Be aware this will ask for you to authenticate your spotify account in a browser)

The script will download the songs from the links and move them to the location specified in the mp3_player_location variable.

You can adjust the number of maximum workers to control the degree of parallelism during the download process. This parameter determines how many downloads can occur simultaneously, which can significantly speed up the overall process.

However, be aware that increasing the number of maximum workers will also increase CPU usage. A setting of 1 will minimize CPU usage but result in slower downloads, as albums will be downloaded one at a time. A higher setting, such as 4, will allow for faster downloads by using more CPU cores, but will also consume more CPU resources. Adjust this setting according to your system's capabilities and your performance needs.

## Configuration
You can configure the download and destination locations by modifying the following variables in the sp2mp3.py script:

mp3_player_location: The location of the mp3 player. The downloaded albums will be moved to this location.
download_location: The location to download the songs.
num_max_workers: Number of cores to use while downloading
## Dependencies
This script requires the following Python libraries:

os, shutil, subprocess, sys: for file operations and running commands

mutagen.easyid3: for handling ID3 tags in MP3 files

concurrent.futures: for parallel processing

csver: custom module for handling CSV files

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
