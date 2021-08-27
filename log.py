#!/usr/bin/python
import time,datetime,sys
debug=True

def logg(*a):
	if debug == True:
		sys.stdout.write(" ".join(a))
	with open(f'pong.log' , 'a') as file:
		file.write(" ".join(a))

def tme():
	now = str(datetime.datetime.now()).split()[1].split('.')[0]
	return now
	
def dte():
	today=str(datetime.datetime.now()).split()[0]
	return today


def main(*a):
	logg(a)

if __name__ == '__main__':
	main(sys.argv)