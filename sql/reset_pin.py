from insert_data_users import *
from Crypto.Hash import SHA256

class resetPin:

	def __init__(self):
		self.user = db('test.db')

	def comparePin(self, id, pin):
		print pin
		user_list = self.user.selectQuery('users',['*'],['ID = ' + str(id)])
		salt = user_list[0][6]
		print salt
		hashed_pin = user_list[0][7]
		print hashed_pin
		pin = pin + salt
		print pin
    	entered_pin = SHA256.new(pin).hexdigest()
    	print entered_pin
    	# if hashed_pin == entered_pin:
    	# 	print 1
    	# else:
    	# 	print 0


def main():
	obj = resetPin()
	obj.comparePin(1,'1234')	

if __name__ == '__main__':
    main()
		