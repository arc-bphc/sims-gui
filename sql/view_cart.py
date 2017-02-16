''' Use getItemList function to get all the items 
	issued by an user to display the list in the 
	cart. on clicking an item call getItemInfo which
	returns a list containing information about a 
	single item'''


from insert_data_users import *

item_list = []
items_issued = []
quantity = []
final_list = []
itemID_issued = []

class view_cart:

	def __init__(self):
		self.user = db('sql/test.db')

	def getItemList(self, id):
		item_list = self.user.selectQuery('transactions',['*'],['ID = ' + str(id)])
		# print item_list
		for i in range(len(item_list)):
			itemID_issued.append(item_list[i][2])
			quantity.insert(i,item_list[i][3])
		# print items_issued
		# print quantity
		for j in range(len(items_issued)):
			self.item_info_list = self.user.selectQuery('inventory',['*'],['ITEM_ID = ' + str(itemID_issued[j])])
			items_issued.append(item_info_list[j][1])
		return items_issued

	def getItemInfo(self,item_no):
		# print self.item_info_list
		final_list = [self.item_info_list[item_no][0],self.item_info_list[item_no][1],self.item_info_list[item_no][2],self.item_info_list[item_no][3],self.item_info_list[item_no][4],self.item_info_list[item_no][5],quantity[item_no]]
		# print final_list
		return final_list

def main():
	obj = view_cart()
	obj.getItemList(1)
	print '\n'
	obj.getItemInfo(0)	

if __name__ == '__main__':
    main()
		