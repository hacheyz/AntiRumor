import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 要爬取的主页面 URL
base_url = "https://www.piyao.org.cn/jrpy/index.htm"

# 请求头部，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

# 配置 Chrome 浏览器驱动
service = Service(executable_path='D:\Code\Python\Anaconda\Scripts\chromedriver.exe')
driver = webdriver.Chrome(service=service)


def make_click():
    """
    模拟点击页面，返回点击后的页面内容
    """
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    # timer = time.time()
    while True:
        # if time.time() - timer > 10:
        # break
        try:
            # 查找并点击“查看更多”按钮
            more_button = wait.until(EC.element_to_be_clickable((By.ID, 'more')))
            # 查看按钮文字是否为“查看更多”，如果是则点击
            if more_button.text == '查看更多':
                more_button.click()
                print("Clicked...")
                time.sleep(1)
            else:
                print("No more button")
                break
        except TimeoutException:
            print("No more button")
            break
    html_content = driver.page_source
    return html_content


def get_article_links(base_url, html_content):
    """
    模拟点击页面下方的“查看更多”，获取页面上的所有文章链接和发布时间
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到包含文章链接的列表元素
    articles = soup.select('ul#list > li')
    article_urls = []

    for article in articles:
        # 获取相对链接
        relative_link = article.find('a')['href']
        # 拼接成完整链接
        full_link = urljoin(base_url, relative_link)
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
            for j in range(i + 1, len(contents)):
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
    html_content = make_click()
    article_urls = get_article_links(base_url, html_content)
    print("Total article count: ", len(article_urls))

    # 数据表
    df = pd.DataFrame(columns=['rumor', 'truth', 'published_date', 'origin', 'url'])
    cnt = 0

    for article_url in article_urls:
        article_info = get_article_content(article_url)
        results = processContennt(article_info['contents'])
        cnt += 1
        print("Processed article count: ", cnt, " URL: ", article_url)
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
