#!/usr/bin/python

import sqlite3

class db:
    def __init__(self, dbName):
        self.databaseName = dbName
        try:
            self.conn = sqlite3.connect(self.databaseName)
            self.cursor = self.conn.cursor()
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
            whereClause = ','.join(whereClause)
            query = 'select ' + placeholder + ' from ' + table + ' where ' + whereClause
        print query
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def updateQuery(self, table, values, whereClause = []):
        values = ','.join(values)
        if len(whereClause) == 0:
            query = 'update ' + table + ' set ' + values
        else:
            whereClause = ','.join(whereClause)
            query = 'update ' + table + ' set ' + values + ' where ' + whereClause
            print query
        self.conn.execute(query)
        self.conn.commit()

def main():
    tempBase = db('arc.db')
#    tempBase.updateQuery('arc_users', ['user_id = 45', "name = 'arcuser0'"], ['user_id = 25'])
#    tempBase.insertTuple('arc_users', [65, "arcuserX"], ['user_id', 'name'])
if __name__ == '__main__':
    main()
