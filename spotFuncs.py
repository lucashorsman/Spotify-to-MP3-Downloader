import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta

import random

from sympy import true

# Set up the Spotify API credentials
client_id = '14f23c99c6174bc7843cd7864abc22cc'
client_secret = 'b2d3a6bbebe24e69a78b98a446471072'
redirect_uri = 'https://localhost:8080'

scope = "user-library-read user-top-read"
token = util.prompt_for_user_token(
    None, scope, client_id, client_secret, redirect_uri="https://localhost:8080"
)
sp = spotipy.Spotify(auth=token)


def get_rand_albums():
    # Get the user's top albums based on listening time
    time_range = 'long_term'  # 'short_term' represents the last month

# Set the random seed based on the current time
    random.seed()

# Randomly select an offset
    offset = random.randint(0, 100)

# Get the top albums with the randomly selected offset
    top_albums_rand = sp.current_user_saved_albums(limit=50, offset=offset)['items']

# Randomly select 3 albums
    random_albums = random.sample(top_albums_rand, 3)

    return 1

def printAlbumfromLink(link):
    album = sp.album(link)
    print(album['name'] + " by " + album['artists'][0]['name'])

def get_artist_albums(artist, top_3_only=False):
    results = sp.search(q='artist:' + artist, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        # print(artist['name'], artist['images'][0]['url'])
        results = sp.artist_albums(artist['id'], album_type='album')
        albums = results['items']
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])
        album_links = []
        albums.sort(key=lambda album:album["release_date"], reverse=False)
        for album in albums:
            album_links.append(album['external_urls']['spotify'])
        if top_3_only:
            return album_links[:3]
    
        return album_links
    else:
        print("Can't find that artist")

def get_playlist_songs(playlist):
    results = sp.playlist(playlist)
    songs = results['tracks']['items']
    while results['tracks']['next']:
        results = sp.next(results['tracks'])
        songs.extend(results['tracks']['items'])
    song_links = []
    for song in songs:
        song_links.append(song['track']['external_urls']['spotify'])
    return song_links
def printSongfromLink(link):
    song = sp.track(link)
    print(song['name'] + " by " + song['artists'][0]['name'])
# # Save the links to each album
# album_links = []
# album_links = get_artist_albums("arcade fire")
# for album in album_links:
#     printAlbumfromLink(album)
# somethin= get_artist_albums("arcade fire", True)
# print(somethin)
# for album in somethin:
#     printAlbumfromLink(album)