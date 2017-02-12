from insert_data_users.py import *

class user_info:

	def get_user_info(id):
		user = db('test.db')
		user_info_list = user.selectQuery('users',['*'],['ID = ' + id])