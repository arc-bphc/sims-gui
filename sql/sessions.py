from .insert_data_users import db
import datetime
import os
class manageSession:
	def __init__(self,dbname):
		self.user = db(dbname)
		self.log=open('/home/pi/late_entries.txt','r+')
		
	def login(self,userID):
		current=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
		previous_entry = self.user.selectQuery('login',['LOGIN'],['ID='+str(userID),'LOGOUT IS NULL'])
		if not previous_entry==[]:
			login_date=datetime.datetime.strptime(previous_entry[0][0], "%d-%m-%Y %H:%M:%S").date()
			
			if datetime.datetime.now().date()>login_date:
				self.user.updateQuery('login',['LOGOUT = "' + current + '"'],['ID = ' + str(userID)])
				name = self.user.selectQuery('users',['NAME'],['ID=%d'%userID])[0][0]
				print(name)
				self.log.seek(0,2)
				self.log.write(name+' login:'+previous_entry[0][0]+' logout:'+current+'\n')
				self.log.flush()
				os.fsync(self.log.fileno())
			else:
				return
		self.user.insertTuple('login',[userID, current],['ID','LOGIN'])
		
				

	def logout(self,userID):
		self.user.updateQuery('login',['LOGOUT = "' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + '"'],['ID = ' + str(userID)])


def main():
	obj = manageSession('SIMS.db')
	# obj.logout(5)

if __name__ == '__main__':
    main()
