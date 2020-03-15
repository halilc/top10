
import urllib3, re
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter


response ={}
url = 'https://listverse.com/2020/03/14/top-10-debunked-myths-about-laundry/'
req = urllib3.PoolManager()
res = req.request('GET', url)
soup = BeautifulSoup(res.data, 'html.parser')

title = soup.find_all('h1')
# print(title[0].text)


subtitles = soup.find_all('h2')
subtitle_list = []

for item in subtitles:
    subtitle_list.append(item.text)
    # print(item.text)
#
#
# def check_ok(tag):
#
#     if tag.find_previous_sibling().name == 'h2':
#         return True
#
#     return check_ok(tag.find_previous_sibling())


posts = soup.find_all('p')
post_list = []
# for item in posts:
#     # print('-------')
#     # print(item.find_previous_sibling().name)
#     if item.find_previous_sibling().name == 'h2' or 'p':
#         # print(item.name)
#         post_list.append(item.text)
#     # print(item.text)


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

for item in post_list:
    print('-----')
    print(item)
response['title'] = str(title[0].text)
response['posts'] = post_list
