from .insert_data_users import db

class editUsers:
	def __init__(self,dbname):
		self.user = db(dbname)

	def deleteUser(self,userID):
		self.user.deleteQuery('users',['ID = ' + str(userID)])
		self.user.updateQuery('fingerprint', ['SENSOR = 2'],['ID = ' + str(userID)])
# 
	def adminAccess(self,userID,isAdmin,roomAccess,inventoryAccess):
		self.user.updateQueryNew('users',[isAdmin,roomAccess,inventoryAccess],['ISADMIN','DOOR_ACCESS','INVENTORY_ACCESS'],['ID = ' + str(userID)])
	# def listUser(self):
	# 	nameList = []
	# 	count = self.user.selectQuery('users',['count(*)'])
	# 	count = count[0][0]
	# 	for i in range(1,count+1):
	# 		my_list = self.user.selectQuery('users',['*'],['ID = ' + str(i)])
	# 		if len(my_list) == 0:
	# 			break
	# 		name = (my_list[0][0], my_list[0][1])
	# 		nameList.append(name)
	# 	# print(nameList)
	# 	return nameList
	def updateUser(self, values, userId):
		for i in values:
			if ((i=="") and (not i==values[2])):
				print("empty string")
				return false
		values[0] = "NAME = '" + values[0] + "'"
		values[1] = "PHONE_CALL = '" + values[1] + "'"
		values[2] = "PHONE_WHATSAPP = '" + values[2] + "'"
		values[3] = "ROOM_NO = '" + values[3] + "'"
		values[4] = "EMAIL_ID = '" + values[4] + "'"
		self.user.updateQuery('users',values, ['ID = ' + str(userId)])
		return True

		
	def listUser(self):
		nameList=self.user.selectQuery('users',['ID','NAME'])
		print("list of users:")
		print(nameList)
		return nameList

	def modifyFingerprint(self,userID,newFinger):
		self.user.updateQueryNew('fingerprint',[newFinger,0],['TEMPLATE','SENSOR'],['ID = ' + str(userID)])
		
			
def main():
	obj = editUsers('SIMS.db')
	# print (obj.listUser())
	# obj.deleteUser(5)
	# obj.modifyFingerprint(5,1)


if __name__ == '__main__':
    main()
