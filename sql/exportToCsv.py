import csv
import sys
from insert_data_users import *


class importCSV:
	def __init__(self,dbname,exitFile):
		self.user = db(dbname)
		f  = open(exitFile, "wb")
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
		count = self.user.selectQuery('users',['count(*)'])
		count = count[0][0]
		# print count
		for i in range(1,count+1):
			my_list = self.user.selectQuery('users',['*'],['ID = ' + str(i)])
			# print my_list
			my_list = list(my_list[0])
			# print my_list
			writer.writerow(my_list)
		f.close()

def main():
	csv = importCSV('test.db','users.csv')

if __name__ == '__main__':
    main()