from insert_data_users import *

catagoryList = []
itemList = []

class selectFromInventrory:

	def __init__(self):
		self.user = db('test.db')

	def getCatagories(self):
		catagoryList = self.user.selectDistinctQuery('inventory',['CATAGORY'])
		self.catagories = []
		for i in range(len(catagoryList)):
			self.catagories.append(catagoryList[i][0])
		return self.catagories

	def getItems(self,catagoryNo):
		itemList = self.user.selectQuery('inventory',['*'],['CATAGORY = ' + self.catagories[catagoryNo]])
		return itemList



def main():
	obj = selectFromInventrory()
	print obj.getCatagories()
	print getItems(0)


if __name__ == '__main__':
    main()