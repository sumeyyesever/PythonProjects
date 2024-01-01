from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

# scrape

year = input("Enter the year you want to travel its musics to YYYY-MM-DD ")

web_url = f"https://www.billboard.com/charts/hot-100/{year}/"
response = requests.get(web_url)
billboard_page_html = response.text
soup = BeautifulSoup(billboard_page_html, "html.parser")

artist_lines = soup.find_all(name="span", class_="a-no-trucate")
song_lines = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")

artists = [artist.getText().strip() for artist in artist_lines]
songs = [song.getText().strip() for song in song_lines]
print(artists)
print(songs)

# create playlist with spotipy

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    cache_path="token.txt",
    username="S"
))

user = spotify.current_user()
username = user["id"]

playlist = spotify.user_playlist_create(user=username, name=f"Billboard Top 100 for {year}", public=False)
print(playlist)

songs_uri_list = []
for song in songs:
    the_song = spotify.search(song, type="track")
    songs_uri_list.append(the_song["tracks"]["items"][0]["uri"])

spotify.playlist_add_items(playlist_id=playlist["id"], items=songs_uri_list)
