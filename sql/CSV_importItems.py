#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys
from insert_data_users import *

class importCSV:
	def __init__(self,dbname):
		self.user = db(dbname)	
		f = open(sys.argv[1], 'rb')
		reader = csv.reader(f)
		for row in reader:
			row[2] = int(row[2])
			row[3] = int(row[3])
			row[5] = int(row[5])
			print row

			self.user.insertTuple('inventory', row, ['NAME','RFID','SHELF_NO','BOX_NO','CATEGORY','QUANTITY'])

		 
		f.close()

def main():
	csv = importCSV('test.db')

if __name__ == '__main__':
    main()