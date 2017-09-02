from bs4 import BeautifulSoup as bs
from bs4 import Tag, NavigableString

def getNavStrandA(soup):
    if soup is None:
        return ''
    e = []
    for element in soup:
        if isinstance(element, NavigableString):
            e.append(''.join(element.split('\n')).strip())
    return ''.join(e)

def getLinkFromMainContent(soup):
    if soup is None:
        return ''
    e = []
    for element in soup:
        if isinstance(element, Tag) and element.name == 'a':
            e.append(''.join(element.text.split('\n')).strip())
    return e


# 提取來源
def getSource(s):
    if not r'1.媒體來源:' in s or not r'2.完整新聞標題:' in s:
        return ''
    source = s.split(r'1.媒體來源:',1)[1].split(r'2.完整新聞標題:',1)[0]
    source = source.lower()
    if '聯合' in source or 'udn' in source:
        source = 'udn'
    elif '蘋果' in source or 'apple' in source:
        source = 'apple'
    elif 'bbc' in source:
        source = 'bbc'
    elif 'buzzfeed' in source:
        source = 'buzzfeed'
    elif 'buzzorange' in source or '中央社' in source:
        source = 'buzzorange'
    elif 'ettoday' in source or 'et today' in source or '東森' in source or source[:2] == 'et':
        source = 'ettoday'
    elif 'ntdtv' in source or '新唐' in source:
        source = 'ntdtv'
    elif '自由' in source or '自冉' in source or 'ltn' in source or 'liberty' in source:
        source = 'liberty times'
    elif 'technews' in source:
        source = 'technews'
    elif 'tvbs' in source:
        source = 'tvbs'
    elif 'wsj' in source or 'wall street' in source:
        source = 'wsj'
    elif 'yahoo' in source or '奇摩' in source:
        source = 'yahoo'
    elif 'yam' in source or '番新聞' in source or '蕃薯' in source:
        source = 'yam'
    elif '三立' in source or 'set' in source:
        source = '三立'
    elif '世界' in source:
        source = 'world journal'
    elif '上報' in source or 'up media' in source:
        source = 'up media'
    elif '中天' in source or 'ctitv' in source:
        source = 'ctitv'
    elif '中廣' in source or '廣播' in source or 'bcc' in source:
        source = 'bcc'
    elif '中時' in source or 'china times' in source or 'chinatimes' in source or '中國時報' in source:
        source = 'china times'
    elif '中華' in source or 'china daily' in source or 'chinadaily' in source:
        source = 'china daily'
    elif '今周' in source or '今週' in source or 'business today' in source or 'businesstoday' in source:
        source = 'business today'
    elif '壹週' in source or '壹周' in source or 'next media' in source or 'next' in source:
        source = 'next media'
    elif '旺報' in source or '旺旺' in source:
        source = 'wang bao'
    elif '東方' in source or 'oriental' in source:
        source = 'dong fang'
    elif '民視' in source or 'ftv' in source or 'formosa' in source:
        source = 'formosa tv'
    elif '華視' in source or 'cts' in source:
        source = 'cts'
    elif '鏡' in source or 'mirror' in source:
        source = 'mirror media'
    elif '風傳' in source or 'storm' in source:
        source = 'storm media'
    elif 'now' in source or '今日' in source:
        source = 'now news'
    elif 'pchome' in source:
        source = 'pchome'
    elif '新頭殼' in source or 'newtalk' in source or 'new talk' in source:
        source = 'newtalk'
    elif '大紀元' in source:
        source = "epochtimes"
    return source




# 提取標題
def getHeadline(s):
    if not r'2.完整新聞標題:' in s or not r'3.完整新聞內文:' in s:
        return ''
    return s.split(r'2.完整新聞標題:',1)[1].split(r'3.完整新聞內文:',1)[0]



# 提取內文
def getContent(s):
    if not r'3.完整新聞內文:' in s or not r'4.完整新聞連結 (或短網址):' in s:
        return ''
    return s.split(r'3.完整新聞內文:',1)[1].split(r'4.完整新聞連結 (或短網址):',1)[0]


# 提取
def getOriginalLink(s):
    if not r'4.完整新聞連結 (或短網址):' in s or not r'5.備註:' in s:
        return ''
    return s.split(r'4.完整新聞連結 (或短網址):',1)[1].split(r'5.備註:',1)[0]
