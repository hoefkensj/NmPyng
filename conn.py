#!/usr/bin/python
import subprocess,shlex,time,sys
from collections import deque
from logg import logg
q = deque()

def run_old(*a):
	process = subprocess.Popen(*a, stdout=subprocess.PIPE, universal_nlines=True)
	while process.poll() is None:time.sleep(0.001)
	if process.poll() is not None:return(process.stdout.readlines())
def run(*a):
	return subprocess.Popen(*a, stdout=subprocess.PIPE, universal_newlines=True)

def conn_get():
	lns=[]
	nlines=[]
	dct_conns={}
	process = run(('nmcli','-t','c','show'))
	while True:
		#lns.append(process.stdout.readline().strip())
		if process.poll() is not None:break
	lns= process.stdout.readlines()
	for line in lns:
		line=line.strip('\n')
		line=line.split(':')
		nlines.append(line)
	for i,line in enumerate(nlines):
		dct_conns[i]=line
	return dct_conns
	
def conn_get_wifi():
	wifi=[]
	conns=conn_get()
	for con in conns:
		if 'wireless' in list(conns[con])[2]:
			wifi.append(conns[con])
	return wifi

def conn_findname(name):
	matches=[]
	conns=conn_get()
	for con in conns:
		if name in list(conns[con])[0]:
			matches.append(conns[con])
	return matches
	
def conn_up(UUID):
	process = run (('nmcli','c','up', UUID))
	#dont wait ffor this top finish11
	return process
def conn_dn():
	process = run ('nmcli','c','down','UUID')
	#dont wait ffor this top finish
	return process
def conn_next():
	#get active connections, if no active start first
	pass

	


	
def main():
	telenet=conn_findname('Telenet')


	print(telenet)
if __name__ == '__main__':
	main()