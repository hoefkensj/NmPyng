#!/usr/bin/python
import subprocess,shlex,time,sys
import log
import ping
from collections import deque
from functools import partial


def proc(*a, **k):
	subprocess.Popen(a, universal_newlines=True, stdout=subprocess.PIPE)

def run(a):
	return subprocess.Popen(a,universal_newlines=True,stdout=subprocess.PIPE )

def check(host):
	def offline():
		log.logg(f'\tOFFLINE\n')
		return False
	def online():
		log.logg(f'\tONLINE\n')
		return True
	return online() if ping.http(host) else offline()



def get():
	lns=[]
	nlines=[]
	dct_conns={}
	process = run('nmcli -t c show')
	while True:
		if process.poll() is not None:break
	lns= process.stdout.readlines()

	for line in lns:
		nlines.append(line.strip('\n').split(':'))
	for i,line in enumerate(nlines):
		dct_conns[i]=line
	return dct_conns
	
def findname(name):
	matches=[]
	conns=conn.get()
	for con in conns:
		if name in list(conns[con])[0]:
			matches.append(conns[con])
	return matches
	

def up(UUID):
	return  run (('nmcli','c','up', UUID))
def dn(UUID):
	return run (('nmcli','c','down',UUID))
def nxt():
	#get active connections, if no active start first
	pass
	




def main():
	telenet=conn.findname('Telenet')
	print(telenet)
if __name__ == '__main_.':
	main()