#!/usr/bin/env python3

from pytube import Playlist
from bs4 import BeautifulSoup
import requests
import re

URL_PLAYLIST = "https://www.youtube.com/playlist?list=PLC8UWZPWDAiUFzH1jWz6zJpAiYxN1iJvP"

def description_scrapper(url:str):
    soup = BeautifulSoup(requests.get(url).content, features='html.parser')


    link = soup.find_all(name="title")[0]
    title = str(link)
    title = title.replace("<title>","")
    title = title.replace(" - YouTube</title>","")

    print(title, end='\t')

    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    description = pattern.findall(str(soup))[0].replace('\\n','\n')
    return (description)

def exercices_scrapper(desc:str):
    lines = [line for line in desc.split('\n') if 'google' in line]
    #[print(line) for line in lines]
    ex  = next((line for line in lines if line.startswith('Exercices')), None)
    if ex:
        ex = ex.lstrip('Exercices de japonais ▶ ') # Keep link only
    return ex #Return the exercises pages
    

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
#print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
descriptions = []
exercises_urls = []
for url in playlist:
    urls.append(url)
    #print(url)
    desc = description_scrapper(url)
    descriptions.append(desc)
    ex = exercices_scrapper(desc)
    if ex:
        print(ex, end='') #No return to line yet
    exercises_urls.append(ex)
    print() #Return after each url

#[print(ex) for ex in exercises_urls]