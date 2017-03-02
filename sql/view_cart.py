''' Use getItemList function to get all the items
	issued by an user to display the list in the
	cart. on clicking an item call getItemInfo which
	returns a list containing information about a
	single item'''


from insert_data_users import *

item_list = []
items_issued = []
final_list = []
itemID_issued = []

class view_cart:

	def __init__(self):
		self.user = db('sql/test.db')

	def getItemList(self, id): #this has a very big problem! It copies the list repeatedly
		item_list = self.user.selectQuery('transactions',['*'],['ID = ' + str(id)])
		# print item_list
		items_issued = []
		itemID_issued = []
		self.quantity = []
		for i in range(len(item_list)):
			itemID_issued.append(item_list[i][2])
			self.quantity.insert(i,item_list[i][3])
		# print itemID_issued
		# print self.quantity
		self.itemInfoList = []
		for j in range(len(itemID_issued)):
			itemInfo = self.user.viewItemInfo(itemID_issued[j])
			itemInfo = itemInfo[0]
			items_issued.append(itemInfo[1])
		print items_issued
		return items_issued

	def getItemInfo(self,itemId): 
		final_list = self.user.viewItemInfo(itemId)
		return final_list

def main():
	obj = view_cart()
	obj.getItemList(1)
	print '\n'
	print obj.getItemInfo(1)
	#obj.getItemId('\'raspi\'')

if __name__ == '__main__':
    main()
