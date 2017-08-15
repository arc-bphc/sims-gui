from .insert_data_users import db

class editUsers:
	def __init__(self,dbname):
		self.user = db(dbname)

	def deleteUser(self,userID):
		self.user.deleteQuery('users',['ID = ' + str(userID)])
		self.user.updateQuery('fingerprint', ['SENSOR = 2'],['ID = ' + str(userID)])
# 
	def makeAdmin(self,userID):
		self.user.updateQuery('users',['ISADMIN = 1'],['ID = ' + str(userID)])

	def listUser(self):
		nameList = []
		count = self.user.selectQuery('users',['count(*)'])
		count = count[0][0]
		for i in range(1,count+1):
			my_list = self.user.selectQuery('users',['*'],['ID = ' + str(i)])
			name = str(my_list[0][0]) + '/' + my_list[0][1]
			nameList.append(name)
		return nameList

	def modifyFingerprint(self,userID,newFinger):
		self.user.updateQuery('fingerprint', ['TEMPLATE = '+str(newFinger), 'SENSOR = 0'],['ID = ' + str(userID)])
		
			
def main():
	obj = editUsers('SIMS.db')
	# print (obj.listUser())
	# obj.deleteUser(5)
	# obj.modifyFingerprint(5,1)


if __name__ == '__main__':
    main()
