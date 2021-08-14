#!/usr/bin/python
import requests

def ping_http(host,retry=2):
	def check(host,to):
		return requests.head(host,timeout=to)
	for _ in range(0,retry):
		try:
			httphead = check(host,0.5) #statuscode 200 = ok
			if httphead.status_code==200:return httphead.status_code
		except requests.exceptions.ConnectionError:
			continue
		except requests.exceptions.ReadTimeout:
			continue
	return


def main(url):
	print(ping_http(f'{url}'))
	
if __name__ == '__main__':
	main('http://ftp.belnet.be')
	main('http://httpbin.org/status/200')

