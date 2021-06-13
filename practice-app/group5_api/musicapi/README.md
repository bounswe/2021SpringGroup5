# Musicapi API Description

Welcome to the Music API.

Musicapi  provides the song names of a particular sport playlist. Music API is developed with Django framework and it only supports GET method.

# API Routes

/musicapi/api

# API Functionality

# GET /musicapi/api

returns name of the songs in json format.

There should be two input in the code, PLAYLIST_ID and TOKEN. 
https://open.spotify.com/playlist/4JhDvULKIy5CXyzJRufHLt?si=14e994f8c07a4dc4 
PLAYLIST_ID: 4JhDvULKIy5CXyzJRufHLt
OAuth Token can be reachable on https://developer.spotify.com/console/get-playlist-tracks/
OAuth is valid for 1 hour. I couldn't find a way to extend this time period. Because of that I should renew it to get the list of song names. 

Here is some screenshots of the API.

<img width="1440" alt="Ekran Resmi 2021-06-09 11 34 06" src="https://user-images.githubusercontent.com/47904355/121321511-d67e5880-c916-11eb-83a6-6a35398246b5.png">

<img width="1440" alt="Ekran Resmi 2021-06-09 11 33 51" src="https://user-images.githubusercontent.com/47904355/121321523-d8481c00-c916-11eb-976e-061e7cc214d9.png">


