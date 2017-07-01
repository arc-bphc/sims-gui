from .insert_data_users import *

catagoryList = []
items = []
itemInfo = []

class selectFromInventory:
	def __init__(self,dbname):
		self.user = db(dbname)

	def getCatagories(self):
		catagoryList = self.user.selectDistinctQuery('inventory',['CATEGORY'])
		self.catagories = []
		for i in range(len(catagoryList)):
			self.catagories.append(catagoryList[i][0])
		return self.catagories

	def getItems(self,catagoryNo):
	#	print self.catagories[catagoryNo]
		items = []
		self.itemList = []
		self.itemList = self.user.selectQuery('inventory',['*'],["CATEGORY = '" + self.catagories[catagoryNo] + "'"])
	#	print self.itemList
		for j in range(len(self.itemList)):
			items.append(self.itemList[j][1])
		return items

	def getItemInfo(self,itemNO):
		itemInfo = self.itemList[itemNO]
		# self.preQuantity = itemInfo[6]
		# print self.preQuantity
		return itemInfo

	def getItemId(self, name):
		itemId = self.user.selectQuery('inventory', ['ITEM_ID'], ['NAME = ' + str(name)])
		return itemId[0][0]

	def addToCart(self,userID,userName,itemID,quantity,issueTime):
		if quantity <= 0:
			return 1
		itemAlreadyPresent = []
		itemAlreadyPresent = self.user.selectQuery('transactions',['*'],['ID = ' + str(userID), 'ITEM_ID = ' + str(itemID)])
		# print itemAlreadyPresent
		item = []
		item = self.user.selectQuery('inventory',['*'],["ITEM_ID = " + str(itemID)])
		preQuantity = item[0][6]
		# print preQuantity
		postQuantity = preQuantity - quantity
		# print postQuantity
		if postQuantity < 0:
			return 0
			#returns 0 if quantity demanded is more than that in inventory.
		else:
			if len(itemAlreadyPresent) == 0:
				self.user.insertTuple('transactions', [userID,userName,itemID,quantity,issueTime], ['ID','NAME','ITEM_ID','QUANTITY','ISSUE_DATETIME'])
			else:
				self.user.updateQuery('transactions',['QUANTITY = ' + str(itemAlreadyPresent[0][3]+quantity)], ['ID = ' + str(userID), 'ITEM_ID = ' + str(itemID)])
			self.user.updateQuery('inventory',['QUANTITY = ' + str(postQuantity)],['ITEM_ID = ' + str(itemID)])
			return 1
			#returns 1 if demanded quantity is valid and changes are made to the database.

# def main():
# 	obj = selectFromInventory('test.db')
# 	# obj.getCatagories()
# 	# obj.getItems(1)
# 	# obj.getItemInfo(0)
# 	obj.addToCart(1,'yashdeep',3,20,'now')


# if __name__ == '__main__':
#     main()
