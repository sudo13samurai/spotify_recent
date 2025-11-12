# spotify_recent
A minimalist Python script that fetches your 500 most recently played Spotify tracks, displays them formatted and styled in the terminal, and exports a webpage with album art, artist info, and playback timestamps.

<img width="300" height="534" alt="image" src="https://github.com/user-attachments/assets/116e0be6-6632-4e5b-b2c3-03c64e82c561" />

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
## [Access Token Doc](https://developer.spotify.com/documentation/web-api/concepts/access-token)

1. Get a Spotify Developer account: [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create an app → copy your **Client ID**, **Client Secret**, and add: http://127.0.0.1:8888/callback Redirect URIs.
3. Use the Authorization Code Flow to get your access token, or run spotify_token.sh once to handle it.
4. Export your token before running: export SPOTIFY_TOKEN="your_access_token_here"

## 🧠 Usage
export SPOTIFY_TOKEN="your_access_token_here"
python3 spotify_recent_500.py

## You’ll see progress live in your terminal:
 Fetching vantagho_ST's last 500 played tracks...

1. Black Pinot — Meyhem Lauren, Daringer, Action Bronson (Black Vladimir)
2. In Due Time — SUBSTANCE810, Jay Royale (Makin Waves 2)
3. Street Knowledge — BADBADNOTGOOD, Ghostface Killah, Tree (Sour Soul)
4. Rick — Benny The Butcher (Tana Talk 3)
5. Rex Ryan (feat. Westside Gunn & Roc Marciano) — Conway the Machine, Westside Gunn, Roc Marciano (Reject 2)

✅ Done!
💾 Saved JSON → spotify_recent_500.json
🌐 Web page → spotify_recent_500.html

## <img width="150" height="250" alt="image" src="https://github.com/user-attachments/assets/4c53438d-c147-406c-a9f4-35c5419257f0" />
--
Then just open spotify_recent_500.html in your browser — profit

## <img width="300" height="534" alt="image" src="https://github.com/user-attachments/assets/116e0be6-6632-4e5b-b2c3-03c64e82c561" />
--
## 💚 Credits
Built with ⚡ and 🎧 by @sudo13samurai


