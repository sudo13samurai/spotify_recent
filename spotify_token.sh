#!/usr/bin/env bash

CLIENT_ID="bca60dd23c5442d09249bb0cf8f922bd"
CLIENT_SECRET="3262030bf1ec4aa1b5deff23f8ac0652"
REDIRECT_URI="http://127.0.0.1:8000/callback"
SCOPE="user-read-recently-played"

# Step 1: Open Spotify login page
echo "Open this URL in your browser and log in:"
echo "https://accounts.spotify.com/authorize?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${REDIRECT_URI}&scope=${SCOPE}"
echo ""
read -p "Paste the full redirect URL after login: " RESPONSE_URL

# Extract the code from redirect
CODE=$(echo "$RESPONSE_URL" | grep -oP 'code=\K[^&]+')

# Step 2: Exchange for access token
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=authorization_code&code=${CODE}&redirect_uri=${REDIRECT_URI}&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}" \
