#!/usr/bin/env python3
#import gdown
from export_pdf import credentials_handler, export_pdf
from re import match

def get_lines(file:str):
    with open(file) as f:
        content = f.read()
    lines = content.split('\n')
    return lines

def get_ex_urls(file:str):
    with open(file) as f:
        content = f.read()
    #print(content)

    exos = [ex for ex in content.split() if ex.startswith('http')] #keep only urls
    #[print(ex) for ex in exos]
    return exos

def dl_pdf(creds, title, url):
    #print(title, url)
    output = "pdfs/" + title + ".pdf"
    #gdown.download(url, output, format="pdf")
    if ("id=" in url): #Pattern 1
        id = url.split("id=")[1]
    else: #Pattern 2
        id = url.split('/d/')[1].split('/')[0] #Extract ID from google url (dirty)
    print(id)
    dled = export_pdf(creds, id) #IO.object with location
    with open(output, "wb") as f:
        f.write(dled)
    #exit() # For debug purposes

#ex_urls = get_ex_urls('Exercices.txt')
lines = get_lines("Exercices.txt")
#ex_lines = [line for line in lines if "http" in line] # Filter on lines with exercices
ex_lines = [line.split('\t') for line in lines if "http" in line]
"""# Filter lines with exo and extract key data"""
#[print(line) for line in ex_lines]
creds = credentials_handler()
[dl_pdf(creds, title, url) for (title, url) in ex_lines]