from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import re

driver = webdriver.Chrome()
driver.get("https://www.tuwanjun.com")
driver.maximize_window()

time.sleep(2)

n = 1

while(n <= 5):
    js = "var q=document.documentElement.scrollTop=" + str(n*10000)
    driver.execute_script(js)
    n+=1
    time.sleep(5)

text = driver.page_source
soup = BeautifulSoup(text, 'html.parser')
url_tags = soup.find_all('img', src=re.compile(r'.*(jpg)$'))
print(url_tags)
num = 1
for tag in url_tags:
    url = tag['src']
    try:
        img = requests.get(url)
    except requests.exceptions.MissingSchema:
        continue
    with open('D:\\Python\\爬虫\\tuwanjun\\'+str(num)+'.jpg', 'wb') as f:
        f.write(img.content)
    num+=1

driver.quit()








