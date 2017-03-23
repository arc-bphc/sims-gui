from insert_data_users import *


class purchaseRequests:

	def __init__(self,dbname):
		self.user = db(dbname)

	def addToTable(self, userId, project, price, item, date):
		self.user.insertTuple('purchase', [userId,project,price,item,date])
		return 1



# def main():
# 	obj = purchaseRequests('test.db')
# 	obj.addToTable(1,'SIMS',3000,'Raspi',123)


# if __name__ == '__main__':
#     main()
