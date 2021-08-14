#!/usr/bin/python
from conn import conn_findname,conn_next,conn_up,conn_dn
from ping import ping_ping,ping_http
from logg import logg,logg_time,logg_date
from collections import deque
import sys,time

conns=[]
c_up =[]
c_dn =[]
limit=100

def pyng(host):
	stat=ping_http(host)
	if stat== -1:
		logg(f'\t-\tNO Connection ...')
		conn_next(span)
		return
	else:
		logg(f'\t-\tConnected \n')

def ppl_q(match):
	global conns, c_up, c_dn
	conns=conn_findname(match)
	for conn in conns:
		if conn[3]!='':
			c_up.append(conn)
		else:
			c_dn.append(conn)


def main():
	global conns,c_up,c_dn,limit
	count=0
	logg(f'{logg_date()}\n')
	ppl_q('Telenet')
	if c_up != []:
		while True:
			logg(logg_time())
			pyng('http://ftp.belnet.be')
			time.sleep(10)
	if c_up == []:
		p=conn_up(c_dn[0][1])
		
		while stat is not None:
			stat=p.poll()
			time.sleep(0.1)
			count += 1
			if count == limit:
				break
			

			

				
		




#while True:
#	logg(f'{logg_time()}\t')
#	pyng('http://ftp.belnet.be')

if __name__ == '__main__':
	main()