import spotipy
import yt_dlp
import os
from termcolor import colored
from spotipy.oauth2 import SpotifyClientCredentials
from concurrent.futures import ThreadPoolExecutor

def download_tracks(track):
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    search_query = f"{artist_name} {track_name}"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])
    except:
        pass

# Spotify API configuration
client_id = '<ID>'
client_secret = '<KEY>'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
print(colored(f"\n[+] Spotify Connected", 'green'))

# Get playlist URL and fetch tracks
url = input(f"\n[+] Enter the URL of the playlist: ")
folder = input(f"[+] Enter the folder path of the playlist: ")
playlist_id = url.split("/")[-1].split("?")[0]  # Extract playlist ID from URL
tracks = []
offset = 0

while True:
    results = sp.playlist_items(playlist_id, offset=offset)
    tracks.extend(results['items'])
    offset += len(results['items'])

    if not results['next']:
        break

print(colored(f"\n[+] Found {len(tracks)} tracks\n", 'cyan'))

download_folder = f'~/Música/{folder}'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'default_search': 'ytsearch'
}

max_threads = 10
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(download_tracks, track) for track in tracks]
    for future in futures:
        future.result()

print(colored(f"\n[+] Completed\n", 'green'))







