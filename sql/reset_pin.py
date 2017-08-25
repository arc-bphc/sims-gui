from .insert_data_users import *
from Crypto.Hash import SHA256
import hashlib

class resetPin:
	def __init__(self,dbname):
		self.user = db(dbname)

	def compareEnteredPin(self,id,pin,newPin):
		print ('old pin ' + pin + ' new pin ' + newPin)
		newPin = comparePin(self,id,pin,newPin)

		if self.flag == 1:
			self.user.updateQuery('users',["HASHED_PASSWORD = '" + newPin + "'"],['ID = ' + str(id)])
		status = self.flag
		return self.flag

def comparePin(obj,id,pin,newPin):
	#print pin
	user_list = obj.user.selectQuery('users',['*'],['ID = ' + str(id)])
	salt = user_list[0][6]
	#print salt
	hashed_pin = user_list[0][7]
	print(type(salt))
	print(type(hashed_pin))
	#print "hashed_pin from database:  " + hashed_pin
	if hashed_pin == "" and salt=="":
		print('generating new pwd')
		newPin=createNewPassword(newPin)
		obj.user.updateQuery('users',["SALT = '" + newPin['salt'] + "'"],['ID = ' + str(id)])
		obj.flag = 1
		return newPin['hash']
	else:
		pin = pin + salt
		newPin = newPin + salt
		entered_pin = SHA256.new(pin).hexdigest()
		newPin = SHA256.new(newPin).hexdigest()
		#print "entered_pin:	" + entered_pin
		if hashed_pin == entered_pin:
			obj.flag = 1
			#print "newPin:	" + newPin
			return newPin
		else:
			obj.flag = 0
			return ''

def createNewPassword(text):
    password = {}
    #changed the salt algo to be ascii
    password['salt'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
    # print salt
    password['salt'].encode('utf-8')
    text.encode('utf-8')
    text = text + password['salt']
    #text.encode('utf-8')
    hash_object = hashlib.sha256(text.encode('utf-8'))
    password['hash'] = hash_object.hexdigest()
    return password



def main():
	obj = resetPin('test.db')
	#print obj.compareEnteredPin(1,'1234','hello')

if __name__ == '__main__':
    main()
