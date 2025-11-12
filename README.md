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
1. Get a Spotify Developer account: [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create an app → copy your **Client ID**, **Client Secret**, and add: http://127.0.0.1:8888/callback Redirect URIs.
3. Use the Authorization Code Flow to get your access token, or run spotify_token.sh once to handle it.
4. Export your token before running: export SPOTIFY_TOKEN="your_access_token_here"
## [Access Token Doc](https://developer.spotify.com/documentation/web-api/concepts/access-token)

## 🧠 Usage
export SPOTIFY_TOKEN="your_access_token_here"
python3 spotify_recent_500.py

You’ll see progress live in your terminal:
 Fetching vantagho_ST's last 500 played tracks...

1. Black Pinot — Meyhem Lauren, Daringer, Action Bronson (Black Vladimir)
2. In Due Time — SUBSTANCE810, Jay Royale (Makin Waves 2)
3. Street Knowledge — BADBADNOTGOOD, Ghostface Killah, Tree (Sour Soul)
4. Rick — Benny The Butcher (Tana Talk 3)
5. Rex Ryan (feat. Westside Gunn & Roc Marciano) — Conway the Machine, Westside Gunn, Roc Marciano (Reject 2)
6. Big Steppa — Rome Streetz (KISS THE RING)
7. Valedictorians — Meyhem Lauren, Daringer (Black Vladimir)
8. Thrill of the hunt — SUBSTANCE810, Chuck Chan, Pro Dillinger (Desolate Lands)
9. Zig Zag Zig — Roc Marciano, The Alchemist (The Elephant Man's Bones)
10. Rubber Bands & Weight — Benny The Butcher (Tana Talk 3)
11. Lemon (feat. Method Man) — Conway the Machine, Method Man (From King To A GOD)
12. The Devil’s Chord — DJ Muggs, Rome Streetz (Death & The Magician)
13. Trigger Point Therapy — Meyhem Lauren, Daringer, Westside Gunn (Black Vladimir)
14. Lion's Share — SUBSTANCE810, Observe Since 98, Supreme Cerebral (The Lion's Share)
15. Self Made — Erick the Architect (Self Made)
16. Paula Deen (feat. Westside Gunn) — Armani Caesar, Westside Gunn (THE LIZ 2)
17. 14 KI's — Conway the Machine, The Alchemist (LULU)
18. Eric B — Westside Gunn (Hitler Wears Hermes 2)
19. Airplane Mode — Meyhem Lauren, Daringer (Black Vladimir)
20. My Brother's Keeper — Ka (Descendants of Cain)
21. Rahbannga — Big Ghost Ltd, Westside Gunn, Conway the Machine (Griselda Ghost)
22. Hunnit Dolla Hiccup (feat. Stove God Cooks) — Armani Caesar, Benny The Butcher, Stove God Cooks (THE LIZ 2)
23. E.I.F. — Conway the Machine (Everybody Is F.O.O.D. 3)
24. 100 Up — SmooVth, JD Era, Fredro Starr (Project Near You)
25. Lavish Vision — Meyhem Lauren, Daringer (Black Vladimir)
26. Alpaca — Conway (The Blakk Tape)
27. Paper Plate — GZA (Pro Tools)
28. Broken Bottles — Benny The Butcher (Tana Talk 3)
29. Blakk Tape — Conway the Machine (Reject 2)
30. Eggz — Westside Gunn (Hitler Wears Hermes 2)
31. Conflict Resolution — Meyhem Lauren, Daringer (Black Vladimir)
32. Quantum Leap — Roc Marciano, The Alchemist (The Elephant Man's Bones)
33. Survival Of The Littest — Armani Caesar (THE LIZ 2)
34. Rare Form — Conway (The Blakk Tape)
35. Gold BBS'S — Conway the Machine, The Alchemist (LULU)
36. Long Nights Alone - Intro — SUBSTANCE810, Observe Since 98 (The Lion's Share)
37. Broken Rubberbands — Meyhem Lauren, Daringer (Black Vladimir)
38. Bang (feat. Eminem) - Remix — Griselda, Eminem (WWCD)
39. Hearing Damage — Thom Yorke (Hearing Damage)
40. After Dark — Mr.Kitty (Time)
41. Silo (feat. fknsyd) — RL Grime, Hex Cougar, fknsyd (Silo (feat. fknsyd))
42. Menace 2 (Migos, Lil Yachty) — Quality Control, Migos, Lil Yachty (Quality Control: Control The Streets Volume 2)
43. Erased — Volumes (No Sleep)
44. Erased — Volumes (No Sleep)
45. Flex (Ooh, Ooh, Ooh) — Rich Homie Quan (Flex (Ooh, Ooh, Ooh) - Single)
46. Fuck Yo Man — King Von (Grandson, Vol. 1)
47. Burgundy — $uicideboy$ (New World Depression)
48. Trials & Tribulations — Ace Hood (Trials & Tribulations (Deluxe))
✅ Done!
💾 Saved JSON → spotify_recent_500.json
🌐 Web page → spotify_recent_500.html
<img width="150" height="250" alt="image" src="https://github.com/user-attachments/assets/4c53438d-c147-406c-a9f4-35c5419257f0" />
--
Then just open spotify_recent_500.html in your browser — profit
<img width="300" height="534" alt="image" src="https://github.com/user-attachments/assets/116e0be6-6632-4e5b-b2c3-03c64e82c561" />
--
💚 Credits
Built with ⚡ and 🎧 by @sudo13samurai


