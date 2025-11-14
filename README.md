# 🎧 Spotify-Recently-Played

A minimalist Python script that fetches your **500 most recently played Spotify tracks**,  
displays them formatted and styled in the terminal, and exports a dark-themed webpage  
with album art, artist info, and playback timestamps.

<p align="center">
  <img width="250" height="250" alt="Spotify Recent Screenshot" src="https://github.com/user-attachments/assets/fe7c3295-1087-434c-8913-a6814827be92" />
  <img width="250" height="250" alt="Terminal Output" src="https://github.com/user-attachments/assets/40527eb7-3e87-41e2-92b3-d3a20f55a829" />
</p>

---

## 🚀 Features
- Fetches your 500 most recent Spotify plays using the official Web API  
- Shows colorized, live updates right in the terminal  
- Generates a responsive HTML page (Spotify-dark themed)  
- Includes clickable links to each track and album art  
- Saves all data to `spotify_recent_500.json` for analysis or reuse  
- Automatically displays your Spotify display name as the page title
- Pulls your Spotify profile picture dynamically via /v1/me.
- Renders it beside your username in a rounded avatar style.

---

## ⚙️ Requirements
- Python **3.8+**  
- A valid Spotify API token with the scope:  
  ```
  user-read-recently-played
  ```

---

## 🔑 Setup

📘 [Spotify Access Token Documentation](https://developer.spotify.com/documentation/web-api/concepts/access-token)

1. Create or log in to your Spotify Developer account:  
   👉 [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create a new app → copy your **Client ID** and **Client Secret**.
3. Add this to your Redirect URIs:  
   ```
   http://127.0.0.1:8888/callback
   ```
4. Use the **Authorization Code Flow** to get your access token, or run `spotify_token.sh` to handle it automatically.
5. Export your token before running:
   ```bash
   export SPOTIFY_TOKEN="your_access_token_here"
   ```

---

## 🧠 Usage

```bash
export SPOTIFY_TOKEN="your_access_token_here"
python3 spotify_recent_500.py
```

### You’ll see progress live in your terminal:
```
🎵 Fetching vantagho_ST's last 500 played tracks...

  1. Black Pinot — Meyhem Lauren, Daringer, Action Bronson (Black Vladimir)
  2. In Due Time — SUBSTANCE810, Jay Royale (Makin Waves 2)
  3. Street Knowledge — BADBADNOTGOOD, Ghostface Killah, Tree (Sour Soul)
  4. Rick — Benny The Butcher (Tana Talk 3)
  5. Rex Ryan (feat. Westside Gunn & Roc Marciano) — Conway the Machine, Westside Gunn, Roc Marciano (Reject 2)

✅ Done!
💾 Saved JSON → spotify_recent_500.json
🌐 Web page → spotify_recent_500.html
```

Then just open `spotify_recent_500.html` in your browser — **profit.**

---

## 💚 Credits
Built with ⚡ and 🎧 by [**@sudo13samurai**](https://github.com/sudo13samurai)
