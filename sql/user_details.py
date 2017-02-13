from insert_data_users import *

class user_info:

	def __init__(self):
		self.user = db('test.db')

	def get_user_info(self, id):
		user_list = self.user.selectQuery('users',['*'],['ID = ' + str(id)])
		user_info_list = [user_list[0][1],user_list[0][3],user_list[0][4],user_list[0][5],user_list[0][2]]
		return user_info_list

	def update_user_info(self, values, id):
		values[0] = "NAME = '" + values[0] + "'"
		values[1] = "PHONE_CALL = '" + values[1] + "'"
		values[2] = "PHONE_WHATSAPP = '" + values[2] + "'"
		values[3] = "ROOM_NO = '" + values[3] + "'"
		values[4] = "EMAIL_ID = '" + values[4] + "'"
		self.user.updateQuery('users',values, ['ID = ' + str(id)])



def main():
	obj = user_info()
	user_info_list = obj.get_user_info(1)
	print user_info_list
	obj.update_user_info(["yashdeep thorat",'9010712068','9665333384','BM036',"yashdeep97@gmail.com"],1)
	user_info_list = obj.get_user_info(1)
	print user_info_list

if __name__ == '__main__':
    main()
    