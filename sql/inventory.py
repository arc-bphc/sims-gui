from insert_data_users import *

catagoryList = []
items = []
itemInfo = []

class selectFromInventory:
	def __init__(self):
		self.user = db('sql/test.db')

	def getCatagories(self):
		catagoryList = self.user.selectDistinctQuery('inventory',['CATAGORY'])
		self.catagories = []
		for i in range(len(catagoryList)):
			self.catagories.append(catagoryList[i][0])
		return self.catagories

	def getItems(self,catagoryNo):
	#	print self.catagories[catagoryNo]
		items = []
		self.itemList = []
		self.itemList = self.user.selectQuery('inventory',['*'],["CATAGORY = '" + self.catagories[catagoryNo] + "'"])
	#	print self.itemList
		for j in range(len(self.itemList)):
			items.append(self.itemList[j][1])
		return items

	def getItemInfo(self,itemNO):
		itemInfo = self.itemList[itemNO]
		self.preQuantity = itemInfo[6]
		print self.preQuantity
		return itemInfo

	def addToCart(self,userID,userName,itemID,quantity,issueTime):
		postQuantity = self.preQuantity - quantity
		print postQuantity
		if postQuantity < 0:
			return 0
			#returns 0 if quantity demanded is more than that in inventory.
		else:
			self.user.insertTuple('transactions', [userID,userName,itemID,quantity,issueTime], ['ID','NAME','ITEM_ID','QUANTITY','ISSUE_DATETIME'])
			self.user.updateQuery('inventory',['QUANTITY = ' + str(postQuantity)],['ITEM_ID = ' + str(itemID)])
			return 1
			#returns 1 if demanded quantity is valid and changes are made to the database.

def main():
	obj = selectFromInventrory()
	print obj.getCatagories()
	print obj.getItems(1)
	print obj.getItemInfo(0)
	print obj.addToCart(1,'yashdeep',3,20,'now')


if __name__ == '__main__':
    main()
