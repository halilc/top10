

import urllib3, re
from bs4 import BeautifulSoup
from pymongo import MongoClient
import random
import uuid


c = 1
article_list = []
while(1):
    url = 'https://listverse.com/gaming/page/'
    url = url + str(c)
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        if article.a['href'] in article_list: continue
        article_list.append(article.a['href'])
        print(article.a['href'])
    c += 1
    if c == 20:
        break

final_response = []
client = MongoClient()
client = MongoClient('mongodb://**********:27017/')
db = client['top10']
collection = db.main
response ={}
for article_link in article_list:
    # url = 'https://listverse.com/2020/03/14/top-10-debunked-myths-about-laundry/'
    url = article_link
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')

    title = soup.find_all('h1')

    subtitles = soup.find_all('h2')
    subtitle_list = []
    for item in subtitles:
        subtitle_list.append(item.text)

    posts = soup.find_all('p')
    post_list = []

    for i in soup.find_all('h2'):
        temp = []
        for sib in i.next_siblings:
            if sib.name == 'p':
                if len(sib.text) == 0:
                    continue
                temp.append(sib.text)
            elif sib.name == 'h2':
                post_list.append(temp)
                break

    response['_id'] = uuid.uuid4().hex
    response['type'] = 'gaming'
    response['title'] = str(title[0].text)
    response['subtitles'] = subtitle_list
    response['posts'] = post_list
    print(response)
    # final_response.append(response)

    response_id = collection.insert_one(response)
