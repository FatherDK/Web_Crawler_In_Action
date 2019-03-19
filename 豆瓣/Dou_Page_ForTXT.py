import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://movie.douban.com/top250')
soup = BeautifulSoup(r.text,'html.parser')
p = re.compile(r'[\u4e00-\u9fa5]+[0-9]*')

with open('豆瓣250.txt','wt',encoding = 'utf-8') as f:
    for each in soup.find_all('span','title'):
        if p.match(each.string):
            f.write(each.string + '\n')
