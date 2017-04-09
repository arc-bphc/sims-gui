from insert_data_users import *

class editUsers:
	def __init__(self,dbname):
		self.user = db(dbname)

	def deleteUser(self,userID):
		self.user.deleteQuery('users',['ID = ' + str(userID)])

	def makeAdmin(self,userID):
		self.user.updateQuery('users',['ISADMIN = 1'],['ID = ' + str(userID)])

	def listUser(self):
		nameList = []
		count = self.user.selectQuery('users',['count(*)'])
		count = count[0][0]
		for i in range(1,count+1):
			my_list = self.user.selectQuery('users',['*'],['ID = ' + str(i)])
			name = my_list[0][1]
			nameList.append(name)
		return nameList
			
def main():
	obj = editUsers('test.db')
	print obj.listUser()
	obj.makeAdmin(1)
	obj.deleteUser(2)


if __name__ == '__main__':
    main()
