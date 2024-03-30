#!/usr/bin/env python3

from pytube import Playlist
from bs4 import BeautifulSoup
import requests
import re

URL_PLAYLIST = "https://www.youtube.com/playlist?list=PLC8UWZPWDAiUFzH1jWz6zJpAiYxN1iJvP"

def description_scrapper(url:str):
    soup = BeautifulSoup(requests.get(url).content, features='html.parser')
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    description = pattern.findall(str(soup))[0].replace('\\n','\n')
    return (description)

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
descriptions = []
for url in playlist:
    urls.append(url)
    print(url)
    desc = description_scrapper(url)
    descriptions.append(desc)
    print(desc)