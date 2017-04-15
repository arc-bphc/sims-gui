from insert_data_users import *
from view_cart import *
from Crypto.Hash import SHA256
import socket
 
userID = 0

def ComparePin(data):
	database = db('test.db')
	user = []
	user = data.split(',',1)
	userID = user[0]
	enteredPin = user[1]
	user_list = database.selectQuery('users',['*'],['ID = ' + str(userID)])
	salt = user_list[0][6]
	hashedPin = user_list[0][7]
	enteredPin = enteredPin + salt
	# print (enteredPin)
	# enteredPin.encode('utf-8')
	# print (enteredPin)
	enteredpin = SHA256.new(enteredPin).hexdigest()
	if enteredpin == hashedPin:
		return 1
	else:
		return 0

def getItemList():
	obj = view_cart('test.db')
	return obj.getItemList(userID)


def Main():
    
    host = "192.168.0.111"
    port = 6000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("userID, pin entered by user: " + str(data))
            flag = ComparePin(data)
            if flag == 1:
            	itemList = getItemList()
            	data = ",".join(itemList)
            else:
            	data = "incorrect pin"

            # data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()