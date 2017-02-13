from insert_data_users import *

class user_info:

	def __init__(self):
		self.user = db('test.db')

	def get_user_info(self, id):
		user_info_list = self.user.selectQuery('users',['*'],['ID = ' + str(id)])
		return user_info_list

	def update_user_info(self, values, id):
		self.user.updateQuery('users',values, ['ID = ' + str(id)])



# def main():
# 	obj = user_info()
# 	user_info_list = obj.get_user_info(1)
# 	print user_info_list

# if __name__ == '__main__':
#     main()
#     