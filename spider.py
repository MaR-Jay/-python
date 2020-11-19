import requests
from bs4 import BeautifulSoup

base_url = ''

# 伪装浏览器请求
def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}

    resp = requests.get(url, headers=headers)
    resp.encoding = 'gbk'
    bsobj = BeautifulSoup(resp.text, 'html.parser')
    return bsobj

# 获取连接，返回
def get_pages():
    pages_ = []
    bs = get_url('')
    pages = bs.find('div', {'class': 'listmain'}).findAll('a')
    for page in pages:
        title = page.get_text()
        href = page.get('href')
        pages_.append((title, base_url + href))
    return pages_

# 解析数据
def get_content(link=None):
    if not link:
        bsobj = get_url(url)
    else:
        bsobj = get_url(link)
    title = bsobj.find('div', {'class', 'content'}).find('h1').get_text()
    print(title)
    content = bsobj.findAll('div', {'class': 'showtxt'})
    text = content[0].text.replace('\xa0' * 8, '\n\n')
    return title, text

# 写入文件
def write_text(text):
    with open('flie/%s.txt' % text[0], 'w', encoding='utf8') as f:
        for line in text:
            f.write(line)
    print('下载完成')


if __name__ == '__main__':
    url = ''
    b = get_content()
    write_text(b)
    lst = get_pages()
    for li in lst:
        a_link = li[1]
        c = get_content(a_link)
        write_text(c)
