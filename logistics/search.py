import requests
import logging
# from urllib.parse import urlencode
from hyper.contrib import HTTP20Adapter
import json

url = 'https://t.17track.net/restapi/track'
form_data = {
	"data":[{"num":"1Z81W1R70310597371","fc":0,"sc":0}],
	"guid":"",
	"timeZoneOffset":-480
	}

# form_data_gb2312 = urlencode(form_data, encoding='gb2312')

request_headers = {
	':method': 'POST',
	':authority': 't.17track.net',
	':scheme': 'https',
	':path': '/restapi/track',
	'content-length': '85',
	'accept': 'application/json, text/javascript, */*; q=0.01',
	'origin': 'https://t.17track.net',
	'x-requested-with': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'https://t.17track.net/zh-cn',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	}

cookies = {
	'_yq_bid':'G-3F8A0DB855407670',
	'_ga':'GA1.2.247428011.1542183274',
	'__gads':'ID=f78eb66443dc08f8:T=1542183269:S=ALNI_MZr6PsUpt--sbPeEMYZ6IUHYHNb0A',
	'v5_TranslateLang':'zh-Hans',
	'v5_HisExpress':'100002',
	'__cfduid':'d12ea016e259bde8881bf4639b68540511572048500',
	'_gid':'GA1.2.1481590150.1572230058',
	'_gat':'1',
	'Last-Event-ID':'657572742f3936322f30313932373330316536312f6461672d6c656e61702d717913223ebdae130778c791'
	}

session = requests.Session()
session.mount(url,HTTP20Adapter())
response = session.post(url,json=form_data,cookies = cookies,headers=request_headers,verify=False)
# response = requests.post(url,json=form_data,headers=request_headers)
r = response.request
# print('headers:'+r.headers)
# print('data:'+r.json)
for attr in dir(r):
	print(attr+':'+str(getattr(r,attr)))

print(response.text)
