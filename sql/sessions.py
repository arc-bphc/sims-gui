from .insert_data_users import db

class manageSession:
	def __init__(self,dbname):
		self.user = db(dbname)
		
	def login(self,userID):
		self.user.insertTuple('login',[str(userID)]