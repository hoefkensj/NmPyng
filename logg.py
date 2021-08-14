#!/usr/bin/python
import time,datetime,sys
debug=True

def logg(entry):
	if debug == True:
		sys.stdout.write(entry)
	with open(f'pong.log' , 'a') as file:
		file.write(entry)

def logg_time():
	now = str(datetime.datetime.now()).split()[1].split('.')[0]
	return now
	
def logg_date():
	today=str(datetime.datetime.now()).split()[0]
	return today

def main():
	pass

if __name__ == '__main__':
	main()