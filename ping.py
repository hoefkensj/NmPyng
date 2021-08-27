#!/usr/bin/python
import requests,time
import log,sys
import signal, os


def sudo(trys=2):
	euid = os.geteuid
	if euid() != 0:
		print("Script not started as root. Running sudo..")
		args = ['sudo', sys.executable] + sys.argv + [os.environ]
		# the next line replaces the currently-running process with the sudo
		os.execlpe('gksu', *args)
	else:
		return euid == 0
	left=trys-1
	print(left)
	sudo(left)
#	sudo(trys - 1) if trys<0 else sys.exit()
	
def handler(signum, frame):
	print('Signal handler called with signal', signum)
	raise OSError("Couldn't open device!")


def simhang():
	time.sleep(50)
	return False
def reqhead(host, to):
	status_code=False
	try:
		head=requests.head(host, timeout=to)
		status_code=head.status_code
	except requests.exceptions.ConnectionError:
		status_code=-1
	except requests.exceptions.ReadTimeout:
		status_code=-1
	return status_code
	
def http(host,retry=2,ttl=0.3):
	for _ in range(0,retry):
		return True if reqhead(host,ttl)==200 else False


def main(url):
	log.logg(f'{log.dte()}\n')
	while True:
		now = log.tme().split(':')
		sex = now[2]
		time.sleep(10 - divmod(int(sex), 10)[1])
		if now[1] == '00' and now[2] == '00':
			log.logg('------------------------\n')
		
		log(f'{log.tyme()}\t')
		try:
			status = http(url)
			log.logg(f'{status}\n')
		except KeyboardInterrupt:
			break
	return
	
if __name__ == '__main__':
	uiid=sudo()
	#main(f'http://193.190.198.27.' if sys.argv is None else f'http://{sys.argv}.' )
	#main('http://httpbin.org/status/200')
	
	# Set the signal handler and a 5-second alarm
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(5)
	
	# This open() may hang indefinitely
	#fd = os.open('/dev/ttyS0', os.O_RDWR)
	fd = simhang()
	print('waited 5 sec')
	signal.alarm(0)  # Disable the alarm



