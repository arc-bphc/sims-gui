from insert_data_users import *

class user_info:

	def get_user_info(self, id):
		self.user = db('test.db')
		user_info_list = self.user.selectQuery('users',['*'],['ID = ' + str(id)])
		return user_info_list


def main():
	obj = user_info()
	user_info_list = obj.get_user_info(1)
	print user_info_list

if __name__ == '__main__':
    main()
    