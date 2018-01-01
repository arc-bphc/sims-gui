from .insert_data_users import *
import datetime
class projectDB:
	def __init__(self,dbname):
		self.user=db(dbname)
	
	def getProjectsList(self):
		self.project_list = self.user.selectQuery('Projects',['*'])
		return self.project_list
		
	def updateProject(self,project_id,name,lead_id):
		if name=='' or lead_id==None:
			return 0
		self.user.updateQueryNew('Projects',[str(name),str(lead_id)],['Name','Lead_ID'],['Project_ID='+str(project_id)])
		return 1
		
	def newProject(self,name,lead_id):
		if name=='' or lead_id==None:
			return 0
		try:
			id_list = [i[0] for i in self.project_list]
			project_id=max(id_list)+1
		except:
			project_id=1
		self.user.insertTuple('Projects',[project_id,name,lead_id],['Project_ID','Name','Lead_ID'])
		return 1
		
	def deleteProject(self,project_id,lead_id):
		if project_id==None or lead_id==None:
			return 0	
		self.user.deleteQuery('Projects',['Project_ID='+str(project_id)])
		return 1
		
	def getItemList(self, userId): #this has a very big problem! It copies the list repeatedly
		self.item_list = self.user.selectQuery('project_cart',['*'],['PROJECT_ID = ' + str(userId)])
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
		quantityList = self.user.selectQuery('project_cart',['QUANTITY'],['PROJECT_ID = ' + str(userId), 'ITEM_ID = ' + str(itemId)])
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
		itemAlreadyPresent = self.user.selectQuery('project_cart',['*'],['PROJECT_ID = ' + str(userID), 'ITEM_ID = ' + str(itemID)])
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
		self.user.updateQuery('project_cart',['QUANTITY = ' + str(quantity)], ['PROJECT_ID = ' + str(userID), 'ITEM_ID = ' + str(itemID)])
		return 1
		
	def removeFromCart(self, userId, itemId):
		itemInfo = self.user.viewItemInfo(itemId)
		preQuantity = itemInfo[0][7]
		transactionQuantity = self.user.selectQuery('project_cart',['QUANTITY'],['PROJECT_ID = ' + str(userId), 'ITEM_ID = ' + str(itemId)])
		transQuantity = transactionQuantity[0][0]
		# print transQuantity
		self.user.deleteQuery('project_cart', ['PROJECT_ID = ' + str(userId), 'ITEM_ID = ' + str(itemId)])
		self.user.updateQuery('inventory',['QUANTITY_AVBL = ' + str(transQuantity + preQuantity)],['ITEM_ID = ' + str(itemId)])
