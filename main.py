#!/usr/bin/python
from conn import conn_findname,conn_next,conn_up,conn_dn
from ping import ping_http
from logg import logg,logg_time,logg_date
from collections import deque
import sys,time

conns=[]
c_up =[]
c_dn =[]
limit=100
q = deque()

def pyng(host):
	stat=ping_http(host)
	if stat is None:
		logg(f'\t-\tNO Connection ...\n')
		connext()
		return
	else:
		logg(f'\t-\tConnected \n')

def ppl_q(match):
	global conns, c_up, c_dn, q
	conns=conn_findname(match)
	for conn in conns:
		if conn[3]!='':
			c_up.append(conn)
		else:
			c_dn.append(conn)
			q.append(conn[1])

def connext():
	global q,c_up
	active=conn_up(q.popleft())
	if c_up[0]:
		print(c_up[0])
		killed=conn_dn(c_up[0])
	return active

def main():
	global conns,c_up,c_dn,limit,q
	count=0
	logg(f'{logg_date()}\n')
	while True:
		ppl_q('Telenet')
		if c_up != []:
			logg(f'Connected to {c_up[0][0]} with {c_up[0][3]}: \n')
			while True:
				logg(logg_time())
				pyng('http://ftp.belnet.be') #http://193.190.198.27'
				time.sleep(5)
		if c_up == []:
			p=connext()
			while p.poll() is not None:
				time.sleep(0.1)
				count += 1
				print(count)
				if count == limit:
					break
				
	
				

				
		




#while True:
#	logg(f'{logg_time()}\t')
#	pyng('http://ftp.belnet.be')

if __name__ == '__main__':
	main()