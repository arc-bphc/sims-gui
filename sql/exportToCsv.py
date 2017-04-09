import csv
import sys
from insert_data_users import *


class importCSV:
	def __init__(self,dbname,exitFile):
		self.user = db(dbname)	
		ifile  = open('test.csv', "rb")
		reader = csv.reader(ifile)
		f  = open(exitFile, "wb")
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		 
		for row in reader:
		    writer.writerow(row)
		 
		ifile.close()
		ofile.close()

def main():
	csv = importCSV('test.db','users.csv')

if __name__ == '__main__':
    main()