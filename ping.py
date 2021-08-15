#!/usr/bin/python
import requests,time
from logg import logg,logg_date,logg_time


def pyng_reqhead(host, to):	return requests.head(host, timeout=to)
	
def pyng_http(host,retry=2,ttl=0.4):
	for _ in range(0,retry):
		try:return pyng_reqhead(host,ttl)
		except requests.exceptions.ConnectionError:continue
		except requests.exceptions.ReadTimeout:continue
	return

def main(url):
	logg(f'{logg_date()}\n')
	while True:
		try:logg(f"{logg_time()}",f"{'Connected' if pyng_http(url).status_code == 200 else 'Not Connected'}\n")
		except KeyboardInterrupt:break
		time.sleep(5)
	return
	
if __name__ == '__main__':
	main('http://193.190.198.27')
	#main('http://httpbin.org/status/200')

