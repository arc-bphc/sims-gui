from insert_data_users import db
import datetime

class manageSession:
	def __init__(self,dbname):
		self.user = db(dbname)
		
	def login(self,userID):
		self.user.insertTuple('login',[userID,	datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],['ID','LOGIN'])


def main():
	obj = manageSession('SIMS.db')
	obj.login(5)

if __name__ == '__main__':
    main()
