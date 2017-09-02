import requests
from collections import Counter
import time
from bs4 import BeautifulSoup as bs
from bs4 import Tag, NavigableString

from string_parsing_funcs import *

baseUrl = "https://www.ptt.cc"
newsUrls = []

def extractNewsUrls(resp):
    soup = bs(resp.text, "html5lib")
    for tag in soup.find_all('a'):
        if tag.string and '[新聞]' in tag.string and not 'Re: [新聞]' in tag.string:
            newsUrls.append(tag.get('href'))

def crawlPPTGossiping(i,j):
    for i in range(i, j):
        url = baseUrl + '/bbs/Gossiping/index' + str(i) + '.html'
        #time.sleep(0.1)
        resp = requests.get(url = url, cookies={'over18': '1'}, verify=True)
        extractNewsUrls(resp)

crawlPPTGossiping(13822,22640)

def writeLinksToFile():
    for u in newsUrls:
        with open('data/newsUrls.txt','a') as f:
            f.write(u)
            f.write("\n")

writeLinksToFile()

def extractFeatures(n):
    soup = bs(n)
    author = ""
    datetime = ""
    headline = ""
    metatags = [t.get_text() for t in soup.find_all('span', class_ = 'article-meta-value')]
    if len(metatags) == 4:
        author = metatags[0]
        datetime = metatags[-1]
        headline = metatags[-2]
    reactions = [t.get_text().strip() for t in soup.find_all('span', class_='push-tag')]
    reactions_count = Counter(reactions)
    upvotes = reactions_count['推']
    downvotes = reactions_count['噓']
    forwards = reactions_count['→']
    soup_main_content = soup.find(id="main-content")
    maincontent = getNavStrandA(soup_main_content)
    linksInContent = getLinkFromMainContent(soup_main_content)
    originalLink = ''
    if not r'4.完整新聞連結 (或短網址):' in maincontent or not r'5.備註:' in maincontent:
        if len(linksInContent) > 0:
            originalLink = linksInContent[0]
    else:
        originalLink = getOriginalLink(maincontent)
    line = ','.join([author,datetime,str(upvotes),str(downvotes),str(forwards),getSource(maincontent),headline,originalLink+'\n'])
    #print(line)
    with open('data/news.csv','a') as f:
        f.write(line)

with open('data/news.csv','w') as f:
    f.write("author,datetime,upvotes,downvotes,forwards,source,headline,original_link"+"\n")

for nu in newsUrls:
    u = baseUrl + nu
    extractFeatures(requests.get(url = u, cookies={'over18': '1'}, verify=True).text)
