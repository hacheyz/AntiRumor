import os
import re
import requests
from bs4 import BeautifulSoup
import random
from urllib.parse import urljoin
import pandas as pd
from selenium import webdriver

# 要爬取的主页面 URL
base_url = "https://www.piyao.org.cn/jrpy/index.htm"

# 请求头部，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

def get_article_links(url):
    """
    模拟点击页面下方的“查看更多”，获取页面上的所有文章链接和发布时间
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 找到包含文章链接的列表元素
    articles = soup.select('ul#list > li')
    article_urls = []

    for article in articles:
        # 获取相对链接
        relative_link = article.find('a')['href']
        # 拼接成完整链接
        full_link = urljoin(url, relative_link)
        article_urls.append(full_link)

    return article_urls


def get_article_content(url):
    """
    获取文章的文本内容、发布日期、发布者和标题
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找所有的 <p> 标签并过滤掉没有文本或只有空白的 <p> 标签
    paragraphs = soup.find_all('p')

    text_content = []
    published_date = ''

    for p in paragraphs:
        # 检查 <p> 标签中的文本内容是否为空或仅包含空白字符
        if p.get_text(strip=True) != '':
            # 检查是否为发布日期
            if published_date == '' and re.match(r'\d+年\d+月\d+日', p.get_text(strip=True)):
                published_date = p.get_text(strip=True)
            else:
                text_content.append(p.get_text(strip=True))

    return {
        'contents': text_content,
        'published_date': published_date,
        'publisher': '中国互联网联合辟谣平台',
        'url': url
    }

def processContennt(contents):
    """
    处理文章内容，将文章内容拆分为谣言和真相
    """
    rumor_truth_pairs = []
    for i in range(0, len(contents)):
        content = contents[i]
        if content.startswith('谣言：') or content.startswith('误区：'):
            rumor = content[3:]
            # 除去结尾的标点符号（。？！：等）
            if rumor[-1] in ['。', '？', '！', '：']:
                rumor = rumor[:-1]
            truth = ''
            for j in range(i+1, len(contents)):
                content = contents[j]
                if content.startswith('真相：'):
                    truth = content[3:]
                    break
            # 检查 truth 末尾是否有类似“（来源：XXX）”的内容
            origin = "中国互联网联合辟谣平台"
            if re.search(r'（来源：.*?）$', truth):
                origin = re.search(r'（来源：(.*?)）$', truth).group(1)
                truth = re.sub(r'（来源：.*?）$', '', truth)
            rumor_truth_pairs.append({'rumor': rumor, 'truth': truth, 'origin': origin})

    return rumor_truth_pairs
            
def main():
    # 获取主页面上所有文章链接
    article_urls = get_article_links(base_url)
    
    # 数据表
    df = pd.DataFrame(columns=['rumor', 'truth', 'published_date', 'origin', 'url'])
    
    for article_url in article_urls:
        article_info = get_article_content(article_url)
        results = processContennt(article_info['contents'])
        for result in results:
            df = df._append({
                'rumor': result['rumor'],
                'truth': result['truth'],
                'published_date': article_info['published_date'],
                'origin': result['origin'],
                'url': article_info['url']
            }, ignore_index=True)
    
    df.to_csv('./data/rumor_truth.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()
