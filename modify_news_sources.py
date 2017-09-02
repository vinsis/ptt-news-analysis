import pandas as pd
import numpy as np

df = pd.read_csv("data/news.csv")

def getSourceFromLink(link):
    if pd.isnull(link):
        return ''
    source = ''
    if r'udn.com' in link:
        source = 'udn'
    elif r'epochtimes' in link or r'大紀元' in link:
        source = 'epochtimes'
    elif r'imgur' in link:
        source = 'imgur'
    elif r'youtu' in link:
        source = 'youtube'
    elif r'cna' in link or r'中央' in link:
        source = 'cna'
    elif r'hinet' in link:
        source = 'hinet'
    elif r'cnyes' in link:
        source = 'cnyes'
    elif r'鉅亨' in link:
        source = 'cnyes'
    elif r'公視' in link or r'pts' in link:
        source = 'pts'
    elif r'peoplenews' in link:
        source = 'peoplenews'
    elif r'ithome' in link:
        source = 'ithome'
    elif r'cdnews' in link:
        source = 'cdnews'
    elif r'rti' in link:
        source = 'rti'
    elif r'ctee' in link:
        source = 'ctee'
    elif r'nextmag' in link:
        source = 'nextmag'
    elif r'lens' in link:
        source = 'thenewslens'
    elif r'initium' in link:
        source = 'theinitium'
    elif r'apple' in link:
        source = 'apple'
    elif r'bbc.' in link:
        source = 'bbc'
    elif r'buzzfeed' in link:
        source = 'buzzfeed'
    elif r'buzzorange.com' in link:
        source = 'buzzorange'
    elif r'ettoday' in link:
        source = 'ettoday'
    elif r'ntdtv.com' in link:
        source = 'ntdtv'
    elif r'ltn.com' in link:
        source = 'liberty times'
    elif r'technews' in link or r'科技新報' in link:
        source = 'technews'
    elif r'tvbs.com' in link:
        source = 'tvbs'
    elif r'wsj.net' in link or r'wsj.com' in link:
        source = 'wsj'
    elif r'yahoo' in link:
        source = 'yahoo'
    elif r'yam.com' in link:
        source = 'yam'
    elif r'setn.com' in link:
        source = '三立'
    elif r'worldjournal.com' in link:
        source = 'world journal'
    elif r'upmedia.mg' in link:
        source = 'up media'
    elif r'ctitv.com' in link:
        source = 'ctitv'
    elif r'bcc.com' in link:
        source = 'bcc'
    elif r'chinatimes.com' in link or r'中國時報' in link:
        source = 'china times'
    elif r'nextmedia' in link:
        source = 'next media'
    elif r'ftv.com' in link:
        source = 'formosa tv'
    elif r'cts.com' in link:
        source = 'cts'
    elif r'mirrormedia.' in link:
        source = 'mirror media'
    elif r'storm.mg' in link:
        source = 'storm media'
    elif r'nownews.' in link:
        source = 'now news'
    elif r'pchome.' in link:
        source = 'pchome'
    elif r'newtalk.tw' in link:
        source = 'newtalk'
    else:
        a = link.split('//')
        if len(a) > 1:
            source = link.split('//')[1].split('/')[0]
    return source


for i, row in df.iterrows():
    if pd.isnull(row['source']):
        df.set_value(index=i, col='source', value=getSourceFromLink(row['original_link']))


df.to_csv("data/news_modified.csv")
