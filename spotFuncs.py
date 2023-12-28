import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta

import random

# Set up the Spotify API credentials
client_id = '14f23c99c6174bc7843cd7864abc22cc'
client_secret = 'b2d3a6bbebe24e69a78b98a446471072'
redirect_uri = 'https://localhost:8080'

scope = "user-library-read user-top-read"
token = util.prompt_for_user_token(
    None, scope, client_id, client_secret, redirect_uri="https://localhost:8080"
)
sp = spotipy.Spotify(auth=token)

# Get the user's top albums based on listening time in the last month
time_range = 'long_term'  # 'short_term' represents the last month

# Set the random seed based on the current time
random.seed()

# Randomly select an offset
offset = random.randint(0, 100)

# Get the top albums with the randomly selected offset
top_albums_rand = sp.current_user_saved_albums(limit=50, offset=offset)['items']

# Randomly select 3 albums
random_albums = random.sample(top_albums_rand, 3)

# Save the links to each album
album_links = []
for album in random_albums:
    album_links.append(album['album']['external_urls']['spotify'])



def get_rand_albums():
    return album_links

def printAlbumfromLink(link):
    album = sp.album(link)
    print(album['name'] + " by " + album['artists'][0]['name'])