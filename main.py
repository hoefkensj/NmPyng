#!/usr/bin/python
import con,ping
import log
from collections import deque
import sys,time

conns=[]
c_up =[]
c_dn =[]
limit=100
q = deque()

def eval_pyng(host):
	
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


def mkvars():
	varlist,conns, c_up, c_dn,limit,q=[]
	varlist+=[conns, c_up, c_dn,limit,q]
	return varlist


def setvars(v):
	v['limit']	= 100
	v['q'] = deque()
	return v
	
def main():
	vars = mkvars()
	data= setvars(vars)
	global conns,c_up,c_dn,limit,q
	count=0
	log.logg(f'{log.dte()}\n')
	while True:
		ppl_q('Telenet')
		if c_up[0]:
			log.logg(f'Connected to {c_up[0][0]} with {c_up[0][3]}: \n')
			while True:
				log.logg(log.time())
				ping.http('http://ftp.belnet.be') #http://193.190.198.27'
				time.sleep(5)
		if not c_up[0]:
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