'''
抓取亚马逊bestsellers数据
'''

import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG)

#函数定义-----------------------------------------------------------------------------------------开始
def get_soup(url):
	'''获取对应url的soup'''
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
	response = requests.get(url,headers=headers)
	html = response.text
	return BeautifulSoup(html,'html.parser')

def get_pd_url(url):
	'''获取bestsellers页面中所有产品详情页面的url'''

	#bestsellers页面中所有产品详情页面的url列表
	urls = []

	soup = get_soup(url)

	for li in soup.select('#zg-ordered-list > li'):
		href = 'https://www.amazon.com' + li.find('a').get('href')
		logging.info(href)
		urls.append(href)
	
	return urls

def get_pd_data(urls):
	'''获取urls中的产品数据'''

	#存放产品数据的字典
	data = {}

	for url in urls:
		soup = get_soup(url)
		title = soup.select_one('#productTitle').get('text')
		print(title)
		data.update(title = title)



def scrape(url):
	'''抓取bestsellers产品数据'''
	
	#1、获取bestsellers页面中所有产品详情页面的url
	urls = get_pd_url(url)
	#2、抓取产品的数据
	data = get_pd_data(urls)


#函数定义-----------------------------------------------------------------------------------------结束


# bestsellers 第一页
url_1 = 'https://www.amazon.com/Best-Sellers-Mens-Athletic-Shorts/zgbs/fashion/1046660/ref=zg_bs_pg_2?_encoding=UTF8&pg=1'
# bestsellers 第二页
url_2 = 'https://www.amazon.com/Best-Sellers-Mens-Athletic-Shorts/zgbs/fashion/1046660/ref=zg_bs_pg_2?_encoding=UTF8&pg=2'
urls = [url_1,url_2]

for url in urls:
	scrape(url)


