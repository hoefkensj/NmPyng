#!/usr/bin/python
import subprocess,shlex,time,sys
from collections import deque
from logg import logg
from ping import ping_http

def run(*a):
	return subprocess.Popen(*a, stdout=subprocess.PIPE, universal_newlines=True)

def conn_check():
	ping_http(host)
	if stat is None:
		logg(f'\t-\tNO Connection ...\n')
		connext()
		return
	else:
		logg(f'\t-\tConnected \n')


def conn_get():
	lns=[]
	nlines=[]
	dct_conns={}
	process = run(('nmcli','-t','c','show'))
	while True:
		if process.poll() is not None:break
	lns= process.stdout.readlines()
	for line in lns:
		nlines.append(line.strip('\n').split(':'))
	for i,line in enumerate(nlines):
		dct_conns[i]=line
	return dct_conns
	
def conn_findname(name):
	matches=[]
	conns=conn_get()
	for con in conns:
		if name in list(conns[con])[0]:
			matches.append(conns[con])
	return matches
	

def conn_up(UUID):
	return  run (('nmcli','c','up', UUID))
def conn_dn(UUID):
	return run (('nmcli','c','down',UUID))
def conn_next():
	#get active connections, if no active start first
	pass
	




def main():
	telenet=conn_findname('Telenet')
	print(telenet)
if __name__ == '__main__':
	main()