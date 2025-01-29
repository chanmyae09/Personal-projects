import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy



client_id = "7a60e7e2bafc43debafc53ea43c2f7a5"
client_secret = "14d7d42e0f6f4bf8be0f58fd4f2329dc"


day = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = day.split('-')[1]

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = f"https://www.billboard.com/charts/hot-100/{day}/"
response = requests.get(url=URL,headers=header)
data = response.text
soup = BeautifulSoup(data,"html.parser")
songs=soup.select(selector = "li ul li h3")
song_list = []

for song in songs:
    song = song.getText().strip()
    song_list.append(song)

print(song_list)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://example.com",
        show_dialog=True,
        scope="playlist-modify-private",
        cache_path="token.txt",
        username="31kgkywniw5dp6vleqsnhedsi74a"
))
user_id = sp.current_user()['id']

song_uris=[]
for song in song_list:
    song_search = sp.search(q=f"track: f{song} year: {year}", type='track')
    try:
        song_uri = song_search['tracks']['items'][0]['uri']
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
print(song_uris)

playlist = sp.user_playlist_create(user = user_id,name=f"{day} Billboard 100",public=False)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items = song_uris)
