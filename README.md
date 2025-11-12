# spotify_recent
A minimalist Python script that fetches your 500 most recently played Spotify tracks, displays them formatted and styled in the terminal, and exports a webpage with album art, artist info, and playback timestamps.

<img width="999" height="1434" alt="image" src="https://github.com/user-attachments/assets/116e0be6-6632-4e5b-b2c3-03c64e82c561" />

# 🎧 Spotify Recently Played (500 Track Dashboard)

A clean Python script that uses the Spotify Web API to fetch your **last 500 played songs**,  
display them colorized in your terminal, and generate a beautiful dark-themed HTML page  
complete with album art, artists, albums, and timestamps.

---

## 🚀 Features
- Fetches your 500 most recent Spotify plays using the official Web API  
- Shows colorized, live updates right in the terminal  
- Generates a responsive HTML page (Spotify-dark themed)  
- Includes clickable links to each track and album art  
- Saves all data to `spotify_recent_500.json` for analysis or reuse  
- Automatically displays your Spotify display name as the page title

---

## ⚙️ Requirements
- Python 3.8+  
- A valid Spotify API token with the scope: user-read-recently-played

## 🔑 Setup
1. Get a Spotify Developer account: [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create an app → copy your **Client ID**, **Client Secret**, and add: http://127.0.0.1:8888/callback Redirect URIs.
3. Use the Authorization Code Flow to get your access token, or run spotify_token.sh once to handle it.
4. Export your token before running: export SPOTIFY_TOKEN="your_access_token_here"
## [https://developer.spotify.com/documentation/web-api/concepts/access-token](Access Token Documentation)

## 🧠 Usage
export SPOTIFY_TOKEN="your_access_token_here"
python3 spotify_recent_500.py

You’ll see progress live in your terminal:
🎵 Fetching User's last 500 played tracks...

  1. Eggz — Westside Gunn (Hitler Wears Hermes 2)
  2. Broken Rubberbands — Meyhem Lauren, Daringer (Black Vladimir)
  ...
✅ Done!
💾 Saved JSON → spotify_recent_500.json
🌐 Web page → spotify_recent_500.html

<img width="545" height="664" alt="image" src="https://github.com/user-attachments/assets/4c53438d-c147-406c-a9f4-35c5419257f0" />

Then just open spotify_recent_500.html in your browser — it looks like your own personal Spotify Wrapped.

💚 Credits

Built by Krystian Carnahan


