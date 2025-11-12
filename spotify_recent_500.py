#!/usr/bin/env python3
import requests, os, time, json

# --- CONFIG ---
TOKEN = os.getenv("SPOTIFY_TOKEN")  # export SPOTIFY_TOKEN="your_access_token"
URL_RECENT = "https://api.spotify.com/v1/me/player/recently-played"
URL_ME = "https://api.spotify.com/v1/me"
LIMIT = 50
TARGET = 500
SLEEP = 0.25

if not TOKEN:
    raise SystemExit("❌ Missing SPOTIFY_TOKEN environment variable.")

HEADERS = {"Authorization": f"Bearer {TOKEN}"}
tracks = []
before = None

# --- COLORS ---
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# --- FETCH USER INFO ---
def fetch_me():
    """Get Spotify user profile (name + avatar)."""
    r = requests.get(URL_ME, headers=HEADERS)
    if r.status_code != 200:
        return {"name": "My", "avatar": ""}
    data = r.json()
    return {
        "name": data.get("display_name", "My"),
        "avatar": data.get("images", [{}])[0].get("url", "")
    }

# --- FETCH RECENTLY PLAYED ---
def fetch_recent(before=None):
    params = {"limit": LIMIT}
    if before:
        params["before"] = before
    r = requests.get(URL_RECENT, headers=HEADERS, params=params)
    if r.status_code != 200:
        raise SystemExit(f"❌ API error {r.status_code}: {r.text}")
    return r.json()

# --- MAIN FETCH LOOP ---
me = fetch_me()
username = me["name"]
avatar = me["avatar"]

print(f"{MAGENTA}🎵 Fetching {username}'s last {TARGET} played tracks...{RESET}\n")

while len(tracks) < TARGET:
    data = fetch_recent(before=before)
    items = data.get("items", [])
    if not items:
        print("⚠️ No more history available.")
        break

    for item in items:
        track = item["track"]
        artist_names = ", ".join(a["name"] for a in track["artists"])
        played_at = item["played_at"]
        album_images = track["album"].get("images", [])
        album_art = album_images[1]["url"] if len(album_images) > 1 else album_images[0]["url"] if album_images else ""

        entry = {
            "name": track["name"],
            "artist": artist_names,
            "album": track["album"]["name"],
            "played_at": played_at,
            "url": track["external_urls"]["spotify"],
            "art": album_art
        }
        tracks.append(entry)

        # Colorized terminal output
        print(
            f"{CYAN}{len(tracks):>3}.{RESET} "
            f"{BOLD}{entry['name']}{RESET} — "
            f"{YELLOW}{entry['artist']}{RESET} "
            f"({MAGENTA}{entry['album']}{RESET})"
        )

    before = data["cursors"]["before"]
    time.sleep(SLEEP)

# --- SAVE JSON ---
json_output = "spotify_recent_500.json"
with open(json_output, "w") as f:
    json.dump(tracks[:TARGET], f, indent=2)

# --- GENERATE HTML ---
html_output = "spotify_recent_500.html"

# Avatar + Username header section
h1_section = f"""
<div style="display:flex; align-items:center; gap:15px; margin-bottom:20px;">
  {'<img src="'+avatar+'" alt="avatar" width="64" height="64" style="border-radius:50%;">' if avatar else ''}
  <h1 style="margin:0;">{username}'s Recently Played Tracks (500)</h1>
</div>
"""

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{username}'s Spotify Recently Played</title>
<style>
  body {{
    font-family: 'Inter', sans-serif;
    background-color: #121212;
    color: #e5e5e5;
    margin: 40px auto;
    max-width: 900px;
    line-height: 1.6;
  }}
  h1 {{
    color: #1db954;
    font-weight: 600;
  }}
  a {{
    color: #1db954;
    text-decoration: none;
  }}
  a:hover {{
    text-decoration: underline;
  }}
  .track {{
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #333;
  }}
  img.album {{
    width: 75px;
    height: 75px;
    border-radius: 6px;
    margin-right: 15px;
    object-fit: cover;
  }}
  .info {{
    flex: 1;
  }}
  .artist {{
    color: #ccc;
  }}
  .album {{
    color: #888;
  }}
  .played {{
    font-size: 0.8em;
    color: #666;
  }}
</style>
</head>
<body>
{h1_section}
{"".join([
    f'<div class="track">'
    f'<img class="album" src="{t["art"]}" alt="album art">'
    f'<div class="info">'
    f'<a href="{t["url"]}" target="_blank"><strong>{t["name"]}</strong></a><br>'
    f'<span class="artist">{t["artist"]}</span><br>'
    f'<span class="album">{t["album"]}</span><br>'
    f'<span class="played">{t["played_at"]}</span>'
    f'</div></div>'
    for t in tracks[:TARGET]
])}
</body>
</html>
"""

with open(html_output, "w") as f:
    f.write(html_content)

print(f"\n✅ {BOLD}Done!{RESET}")
print(f"💾 Saved JSON → {CYAN}{json_output}{RESET}")
print(f"🌐 Web page → {YELLOW}{html_output}{RESET}")

