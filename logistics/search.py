import requests
import logging
import json
# 1Z090W8Y0399984404\1Z81W1R70310597371
url = 'https://t.17track.net/restapi/track'
data = {
	# "data":[{"num":"1Z81W1R70310597371","fc":0,"sc":0}],
	# "data":[{"num":"1Z090W8Y0399984404","fc":0,"sc":0}],
	"data":[{"num":"1Z9344YV0304748111","fc":0,"sc":0}],
	"guid":"",
	"timeZoneOffset":-480
	}


request_headers = {
	'accept':'application/json, text/javascript, */*; q=0.01',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'zh-CN,zh;q=0.9',
	'Content-Type':'application/json',
	'origin':'https://t.17track.net',
	'referer':'https://t.17track.net/zh-cn',
	'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'x-requested-with':'XMLHttpRequest',
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
	# 1Z81W1R70310597371
	# 'Last-Event-ID':'657572742f6534312f61336635386634316536312f6c6c616d732d736c6f6f742d7179f12525b904e0778c791'
	# 1Z090W8Y0399984404
	# 'Last-Event-ID':'657572742f3164312f63356333633235316536312f6f676f6c2d746c75616665642d71792073782d656c6269736976206f676f6c2d646e6172622d72616276616e1122686882c731e470fc'
	# 'Last-Event-ID':'657572742f3537312f62363062383435316536312f6e776f64706f72642d6b636172742d717920616964656d2d756e656d2d6e776f64706f726420756e656d2d6e776f64706f7264d1227748fb631e470fc'
	# 'Last-Event-ID':'657572742f3537312f30633632653435316536312f65646968207265746e65632d74786574206c656e6170206e67696c612d6c61636974726576207272652d6b726f7774656e2d67736d2d71799122ae3284731e470fc '
	# 'Last-Event-ID':'657572742f3164312f63356333633235316536312f6f676f6c2d746c75616665642d71792073782d656c6269736976206f676f6c2d646e6172622d72616276616e1122686882c731e470fc'
	#1Z9344YV0304748111
	'Last-Event-ID':'657572742f3537312f64383334633935316536312f65646968207265746e65632d74786574206c656e6170206e67696c612d6c61636974726576207272652d6b726f7774656e2d67736d2d71799123f6d50ba6af71812'
	}

response = requests.post(url,data=json.dumps(data,separators=(',',':')),headers=request_headers,cookies=cookies,verify=False)

print(response.text)
'''
{"ret":1,"msg":"Ok","g":"38cd4477d46845e999fcd7fe1fdfb7d9","dat":[{"no":"1Z81W1R70310597371","delay":0,"yt":null,"track":{"b":2105,"c":0,"e":40,"f":8,"w1":100002,"w2":0,"is1":1,"is2":2,"hs":820224827,"z0":{"a":"2019-08-08 11:20","b":null,"c":"MORENO VALLEY, CA, US","d":"","z":"DELIVERED"},"ln9":null,"ln1":"en","ln2":null,"ygt9":0,"ygt1":0,"ygt2":0,"ylt9":"2079-01-01 00:00:00","ylt1":"2019-10-29 00:13:04","ylt2":"2079-01-01 00:00:00","z9":[],"z1":[{"a":"2019-08-08 11:20","b":null,"c":"MORENO VALLEY, CA, US","d":"","z":"DELIVERED"},{"a":"2019-08-08 09:06","b":null,"c":"March Air Reserve Base, CA, United States","d":"","z":"Destination Scan"},{"a":"2019-08-07 22:12","b":null,"c":"March Air Reserve Base, CA, United States","d":"","z":"Arrival Scan"},{"a":"2019-08-07 21:29","b":null,"c":"Ontario, CA, United States","d":"","z":"Departure Scan"},{"a":"2019-08-07 14:42","b":null,"c":"Ontario, CA, United States","d":"","z":"Origin Scan"},{"a":"2019-08-07 14:41","b":null,"c":"Ontario, CA, United States","d":"","z":"Destination Scan"},{"a":"2019-07-31 05:01","b":null,"c":"United States","d":"","z":"Order Processed: Ready for UPS"}],"z2":[],"yt":"","zex":{"trN":"","trC":0,"psex":4001,"sa":false,"dt":1564549260000,"dtS":1564549260000,"dtP":1565263200000,"dtD":1565263200000,"dtL":1565263200000}}}]}
[Finished in 1.0s]
'''