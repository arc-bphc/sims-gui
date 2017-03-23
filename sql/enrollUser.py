from insert_data_users import *
from Crypto.Hash import SHA256
import Crypto.Random

class enrollUser:
	def __init__(self):
		self.user = db('sql/test.db')

	def enrollNewUser(self,name,emailID,phoneCall,phoneWhatsapp,roomNo,pin,fingerID):
		password = self.createPassword(pin)
		self.user.insertTuple('users', [name, emailID, phoneCall, phoneWhatsapp, roomNo, password['salt'], password['hash'], fingerID],['NAME','EMAIL_ID','PHONE_CALL','PHONE_WHATSAPP','ROOM_NO','SALT','HASHED_PASSWORD','FINGERPRINT_ID'])

	def createPassword(self,text):
		password = {}
		password['salt'] = Crypto.Random.get_random_bytes(5)
		text = text + password['salt']
		password['hash'] = SHA256.new(text).hexdigest()
		return password


def main():
	obj = enrollUser()
	obj.enrollNewUser('arnav','habibi@alahuakbar.com','9110000000','9665333384','s123','1234',123)

if __name__ == '__main__':
    main()