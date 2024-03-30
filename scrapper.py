#!/usr/bin/env python3

from pytube import Playlist

URL_PLAYLIST = "https://www.youtube.com/playlist?list=PLC8UWZPWDAiUFzH1jWz6zJpAiYxN1iJvP"

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)
    print(url)
