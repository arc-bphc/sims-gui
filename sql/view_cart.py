''' Use getItemList function to get all the items
	issued by an user to display the list in the
	cart. on clicking an item call getItemInfo which
	returns a list containing information about a
	single item'''


from .insert_data_users import *

item_list = []
items_issued = []
final_list = []
itemID_issued = []
quantityList = []

class view_cart:

	def __init__(self,dbname):
		self.user = db(dbname)

	def getItemList(self, userId): #this has a very big problem! It copies the list repeatedly
		self.item_list = self.user.selectQuery('transactions',['*'],['ID = ' + str(userId)])
		#print(item_list)
		items_issued = []
		itemID_issued = []
		for i in range(len(self.item_list)):
			itemID_issued.append(self.item_list[i][3])
		# print itemID_issued
		self.itemInfoList = []
		for j in range(len(itemID_issued)):
			itemInfo = self.user.viewItemInfo(itemID_issued[j])
			itemInfo = itemInfo[0]
			items_issued.append(itemInfo[1])
		# print(items_issued)
		return items_issued

	def getItemInfo(self,userId,itemId):
		final_list = self.user.viewItemInfo(itemId)
		quantityList = self.user.selectQuery('transactions',['QUANTITY'],['ID = ' + str(userId), 'ITEM_ID = ' + str(itemId)])
		quantity = quantityList[0][0]
		final_list = final_list[0]
		final_list = list(final_list)
		# print quantity
		final_list[6] = quantity
		final_list[7] = quantity
		return final_list
		
	def changeQuantity(self,userID,itemID,quantity):
		if quantity <= 0:
			return 0
		itemAlreadyPresent = []
		itemAlreadyPresent = self.user.selectQuery('transactions',['*'],['ID = ' + str(userID), 'ITEM_ID = ' + str(itemID)])
		quantity_issued=itemAlreadyPresent[0][4]
		quantity_returned=quantity_issued-quantity
		if quantity_returned==0:
		    return 0
		# print itemAlreadyPresent
		item = []
		item = self.user.selectQuery('inventory',['*'],["ITEM_ID = " + str(itemID)])
		preQuantity = item[0][7]
		# print preQuantity
		postQuantity = preQuantity + quantity_returned
		self.user.updateQuery('inventory',['QUANTITY_AVBL= ' + str(postQuantity)],['ITEM_ID = ' + str(itemID)])
		self.user.updateQuery('transactions',['QUANTITY = ' + str(quantity)], ['ID = ' + str(userID), 'ITEM_ID = ' + str(itemID)])
		return 1
	def removeFromCart(self, userId, itemId):
		itemInfo = self.user.viewItemInfo(itemId)
		preQuantity = itemInfo[0][7]
		transactionQuantity = self.user.selectQuery('transactions',['QUANTITY'],['ID = ' + str(userId), 'ITEM_ID = ' + str(itemId)])
		transQuantity = transactionQuantity[0][0]
		# print transQuantity
		self.user.deleteQuery('transactions', ['ID = ' + str(userId), 'ITEM_ID = ' + str(itemId)])
		self.user.updateQuery('inventory',['QUANTITY_AVBL = ' + str(transQuantity + preQuantity)],['ITEM_ID = ' + str(itemId)])


def main():
	obj = view_cart('test.db')
	# obj.getItemList(1)
	# print '\n'
	# print obj.getItemInfo(1,1)
	obj. removeFromCart(1,3)

if __name__ == '__main__':
    main()
