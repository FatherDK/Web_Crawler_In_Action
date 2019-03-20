import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://movie.douban.com/top250')
soup = BeautifulSoup(r.text,'html.parser')
p0 = re.compile(r'[\u4e00-\u9fa5]+[0-9]*')

ranks = []      # 排名
titles = []     # 标题
directors = []  # 导演
actors = []     # 主演
years = []      # 发行年份
countries = []  # 发行国
types = []      # 类型
scores = []     # 得分
quote = []      # 引用

# 排名
for each in soup.find_all('em'):
    ranks.append(each.string)

# 标题
for each in soup.find_all('span','title'):
    if p0.match(each.string):
        titles.append(each.string)

# 导演 演员
for each in soup.find_all('p'):
    string = each.string
    string = re.split(r'(\&nbsp;)(<br>)',string)
    
    string = string.remove('')
    
    


with open('豆瓣250.txt','wt',encoding = 'utf-8') as f:
    
