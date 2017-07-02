from .insert_data_users import db

class loginWithPin:
	def __init__(self,dbname):
		self.user = db(dbname)

	def ComparePin():

