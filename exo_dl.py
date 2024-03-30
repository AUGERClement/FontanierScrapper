#!/usr/bin/env python3
import gdown

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

#ex_urls = get_ex_urls('Exercices.txt')
lines = get_lines("Exercices.txt")
#ex_lines = [line for line in lines if "http" in line] # Filter on lines with exercices
ex_lines = [line.split('\t') for line in lines if "http" in line]
"""# Filter lines with exo and extract key data"""
[print(line) for line in ex_lines]


