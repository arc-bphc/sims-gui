from insert_data_users import db
import hashlib

class loginWithPin:
	def __init__(self,dbname):
		self.user = db(dbname)

	def AuthenticateUser(self, id, enteredPin):
		return(comparePin(self,id,enteredPin));

		

def comparePin(obj,id,enteredPin):
	#print pin
	user_list = obj.user.selectQuery('users',['*'],['ID = ' + str(id)])
	salt = user_list[0][6]
	hashed_pin = user_list[0][7]
	salt=salt.encode('utf-8')
	enteredPin=enteredPin.encode('utf-8')
	enteredPin = enteredPin + salt
	entered_pin = hashlib.sha256(enteredPin).hexdigest()
	if hashed_pin == entered_pin:
		return 1
	else:
		return 0	


# def main():
# 	obj = loginWithPin('SIMS.db')
# 	print (obj.AuthenticateUser(1,'1234'));

# if __name__ == '__main__':
#     main()

