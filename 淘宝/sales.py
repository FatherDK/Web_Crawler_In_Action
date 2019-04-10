import requests
from bs4 import BeautifulSoup

def open_url(keyword):
    payload = {'q':keyword,'sort':'sale-desc'}
    url = 'https://s.taobao.com/search'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    res = requests.get(url, params=payload, headers=headers)
    return res

def main():
    keyword = input('请输入关键词：')
    res = open_url(keyword)

    with open("items.txt",'wt',encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':
    main()
