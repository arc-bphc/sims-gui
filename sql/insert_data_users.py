#!/usr/bin/python

import sqlite3
from Crypto.Hash import SHA256
import Crypto.Random
import os.path
from os import listdir, getcwd
#from IPython.core.display import Image

#-------------SQLite functions----------------------------------

class db:
    def __init__(self, dbName):
        self.databaseName = dbName
        try:
            self.conn = sqlite3.connect(self.databaseName)
            self.cursor = self.conn.cursor()
            self.conn.text_factory = str
            #self.execute('.header on')
            #self.execute('.mode column')
        except:
            print 'Error in connecting to database'

    def __del__(self):
        self.conn.close()

    def insertTuple(self, table, values, parameters = []):
        placeholder = '(' + ','.join('?'*len(values)) + ')'
        #print placeholder
        if len(parameters) == 0:
            query = 'insert into ' + table + ' values ' + placeholder
            self.conn.execute(query, values)
        else:
            parameterPlaceholder = '(' + ','.join(parameters) + ')'
            query = 'insert into ' + table + parameterPlaceholder + ' values ' + placeholder
            self.conn.execute(query, values)
        self.conn.commit()

    def selectQuery(self, table, col, whereClause = []):
        placeholder = ','.join(col)
        if len(whereClause) == 0:
            query = 'select ' + placeholder + ' from ' + table
        else:
            whereClause = ' AND '.join(whereClause)
            query = 'select ' + placeholder + ' from ' + table + ' where ' + whereClause
        # print whereClause
        # print query
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def viewItemInfo(self, itemId):
        itemInfo = []
        itemInfo = self.selectQuery('inventory', ['*'], ['ITEM_ID = ' + str(itemId)])
        return itemInfo

    def selectDistinctQuery(self, table, col, whereClause = []):
        placeholder = ','.join(col)
        if len(whereClause) == 0:
            query = 'select distinct ' + placeholder + ' from ' + table
        else:
            whereClause = ' AND '.join(whereClause)
            query = 'select distinct ' + placeholder + ' from ' + table + ' where ' + whereClause
        #print query
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def updateQuery(self, table, values, whereClause = []):
        values = ','.join(values)
        if len(whereClause) == 0:
            query = 'update ' + table + ' set ' + values
        else:
            whereClause = ' AND '.join(whereClause)
            query = 'update ' + table + ' set ' + values + ' where ' + whereClause
            #print query
        self.conn.execute(query)
        self.conn.commit()

    def deleteQuery(self, table, whereClause = []):
    	if len(whereClause) == 0:
    		query = 'delete from ' + table
    		# print query
    		ans = raw_input("Are you sure you want to delete all the records from the table? (y/n):")
    		if ans == 'y':
    			self.conn.execute(query)
    			self.conn.commit()
    		else:
    			return
    	else:
    		whereClause = ' AND '.join(whereClause)
    		query = 'delete from ' + table + ' where ' + whereClause
    		#print query
    		self.conn.execute(query)
    		self.conn.commit()

    def copyToHistory(self, whereClause):
    	whereClause = ' AND '.join(whereClause)
    	query = 'insert into history select * from transactions where ' + whereClause
	self.conn.execute(query)
	self.conn.commit()


#----------------------------Hashing and encrypting passwords-------------------------------

def createNewPassword(text):
    password = {}
    password['salt'] = Crypto.Random.get_random_bytes(5)
    # print salt
    text = text + password['salt']
    password['hash'] = SHA256.new(text).hexdigest()
    return password

#-------------------------------------------------------------------------------------------
# def main():

#     #add a new user into the users table
#     new_user = db('test.db')
#     text = raw_input("enter new pin:	")
#     password = createNewPassword(text)
#     with open('cover.jpg', 'rb') as input_file:
#         image = input_file.read()
#     new_user.insertTuple('users', [1, "yashdeep","yashdeep97@gmail.com",'9010712068','9665333384','BM036',password['salt'],password['hash'],image])#, ['ID','NAME','EMAIL_ID','PIN','PHONE_CALL','PHONE_WHATSAPP','ROOM_NO'])
#     # print new_user.selectQuery('users',['*'],['ID = 1'])
#     print "\n"

#     #add withdrawn item to transaction database
#     new_user.insertTuple('transactions', [1, "yashdeep",1,3,"2017-02-21 12:30:12","2017-02-21 12:33:13"], ['ID','NAME','ITEM_ID','QUANTITY','ISSUE_DATETIME','WITHDRAW_DATETIME'])
#     print new_user.selectQuery('transactions',['*'],['ID = 1'])
#     print "\n"

# #     #on return of item
#     # new_user.updateQuery('transactions',["RETURN_DATETIME = '2017-02-21 14:50:13'"],['ID = 1'])
# #     print new_user.selectQuery('transactions',['*'],['ID = 1'])
# #     print "\n"

# #     #To-docopy row with returned item to history table
# #     new_user.copyToHistory(['ID = 1'])
# #     print new_user.selectQuery('history',['*'],['ID = 1'])
# #     print "\n"

# #     #delete withdrawn item
# #     new_user.deleteQuery('transactions',['ID = 1'])
# #     print new_user.selectQuery('transactions',['*'])
# #     print "\n"

#     #add item to inventory
#     new_user.insertTuple('inventory', [1, "arduino",123456789112,1,2,'microcontroller',5])


# if __name__ == '__main__':
#     main()
