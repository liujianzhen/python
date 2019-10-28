import requests
import logging
from urllib.parse import urlencode

url = 'https://t.17track.net/restapi/track'
form_data = {
	"data":[{"num":"1Z81W1R70310597371","fc":0,"sc":0}],
	"guid":"",
	"timeZoneOffset":-480
	}

form_data_gb2312 = urlencode(form_data, encoding='gb2312')

request_headers = {
	# 'authority': 't.17track.net',
	# 'method': 'POST',
	# 'path': '/restapi/track',
	# 'scheme': 'https',
	# 'accept': 'application/json, text/javascript, */*; q=0.01',
	# 'accept-encoding': 'gzip, deflate, br',
	# 'accept-language': 'zh-CN,zh;q=0.9',
	# 'content-length': '85',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': '_yq_bid=G-40B76FFCB7A2A3F1; _ga=GA1.2.1066765095.1542172049; __gads=ID=61f49d7156dbf737:T=1542172044:S=ALNI_MZLEmPvfsu4YFm5snrlfzlTL8sYVg; v5_TranslateLang=zh-Hans; _gid=GA1.2.19936691.1571618328; v5_HisExpress=100002_100003_21051_100001_07048_07041_07047; Last-Event-ID=657572742f6332312f65626630353931666436312f737070612d616964656d2d756e656d2d6e776f64706f72642d717921253d76f610778c791',
	# 'origin': 'https://t.17track.net',
	'Referer': 'https://t.17track.net/zh-cn',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	# 'x-requested-with': 'XMLHttpRequest',
	}

response = requests.post(url,data=form_data_gb2312,headers=request_headers)
print(response.text)