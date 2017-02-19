from insert_data_users import *
from Crypto.Hash import SHA256

class resetPin:
	def __init__(self):
		self.user = db('sql/test.db')

	def compareEnteredPin(self,id,pin,newPin):
		print 'old pin ' + pin + ' new pin ' + newPin
		newPin = comparePin(self,id,pin,newPin)

		if self.flag == 1:
			self.user.updateQuery('users',["HASHED_PASSWORD = '" + newPin + "'"],['ID = ' + str(id)])
		print self.flag
		status = self.flag

def comparePin(obj,id,pin,newPin):
	#print pin
	user_list = obj.user.selectQuery('users',['*'],['ID = ' + str(id)])
	salt = user_list[0][6]
	#print salt
	hashed_pin = user_list[0][7]
	#print "hashed_pin from database:  " + hashed_pin
	pin = pin + salt
	newPin = newPin + salt
	# print pin
	entered_pin = SHA256.new(pin).hexdigest()
	newPin = SHA256.new(newPin).hexdigest()
	#print "entered_pin:	" + entered_pin
	if hashed_pin == entered_pin:
		obj.flag = 1
		#print "newPin:	" + newPin
		return newPin
	else:
		obj.flag = 0
		return '0'



def main():
	obj = resetPin()
	print obj.compareEnteredPin(1,'1234','hello')

if __name__ == '__main__':
    main()
