from insert_data_users import *
from Crypto.Hash import SHA256

class resetPin:

	def __init__(self):
		self.user = db('test.db')

	def compareEnteredPin(self,id,pin):
		return comparePin(self,id,pin)


def comparePin(obj,id, pin):
	print pin
	user_list = obj.user.selectQuery('users',['*'],['ID = ' + str(id)])
	salt = user_list[0][6]
	# print salt
	hashed_pin = user_list[0][7]
	print "hashed_pin from database:  " + hashed_pin
	pin = pin + salt
	# print pin
	entered_pin = SHA256.new(pin).hexdigest()
	print "entered_pin:	" + entered_pin
	if hashed_pin == entered_pin:
		return 1
	else:
		return 0


def main():
	obj = resetPin()
	print obj.compareEnteredPin(1,'1234')	

if __name__ == '__main__':
    main()
		