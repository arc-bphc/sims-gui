from insert_data_users import *

class view_cart:
	item_list,quantity

	def __init__(self):
		self.user = db('test.db')

	def getItemList(self, id):
		item_list = self.user.selectQuery('transactions',['*'],['ID = ' + str(id)])
		for i in item_list:
			items_issued.insert(i,item_list[i][2])
			quantity.insert(i,item_list[i][3])
		print items_issued
		for j in items_issued:
			self.item_info_list.insert(j,self.user.selectQuery('inventory',['*'],['ITEM_ID = ' + str(items_issued[j])]))
		return items_issued

	def getItemInfo(self,item_no):
		final_list = [self.item_info_list[item_no][0],self.item_info_list[item_no][1],self.item_info_list[item_no][2],self.item_info_list[item_no][3],self.item_info_list[item_no][4],self.item_info_list[item_no][5],self.quantity[item_no]]
		return final_list

def main():
	obj = view_cart()
	print obj.getItemList(1)
	print '\n'
	print obj.getItemInfo(1)	

if __name__ == '__main__':
    main()
		