#!/usr/bin/python
import subprocess,shlex,time,requests

def ping_ping(host):
	args = f'ping -c 100 -i 10 {host}'
	bashline =  shlex.split(args)
	process = subprocess.Popen(bashline, stdout=subprocess.PIPE, universal_newlines=True)
	while True:
		return_code = process.poll()
		if return_code is not None:
			for line in process.stdout.readlines():
				if 'time=' in line:
					lagg = shlex.split(line)[-2]
					return lagg
		else:
			return -1
		return
	return

def ping_http(host,retry=5):
	status=0
	httphead=requests.head
	while retry > 0:
		retry-=1
		try:
			httphead = httphead(host,timeout=0.5)
			#statuscode 200 = ok
			status=httphead.status_code
			if status==200:
				retry=0
				return status
		except requests.exceptions.ConnectionError:
			if retry==0:
				status=-1
				return status
		except requests.exceptions.ReadTimeout:
			if retry==0:
				status=-1
				return status
	return
	


def main():
	status=ping_http('http://ftp.belnet.be')
	#ping_http('http://httpbin.org/status/200')

	
if __name__ == '__main__':
	main()


