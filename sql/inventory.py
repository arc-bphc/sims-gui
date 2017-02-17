from insert_data_users import *

catagoryList = []
items = []
itemInfo = []

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
		print self.catagories[catagoryNo]
		self.itemList = []
		self.itemList = self.user.selectQuery('inventory',['*'],["CATAGORY = '" + self.catagories[catagoryNo] + "'"])
		print self.itemList
		for j in range(len(self.itemList)):
			items.append(self.itemList[j][1])
		return items

	def getItemInfo(self,itemNO):
		itemInfo = self.itemList[itemNO]
		return itemInfo


def main():
	obj = selectFromInventrory()
	print obj.getCatagories()
	print obj.getItems(0)
	print obj.getItemInfo(1)


if __name__ == '__main__':
    main()