from insert_data_users import *
from view_cart import *
from Crypto.Hash import SHA256
import socket
 
userID = 0

def getItemList(userID):
	obj = view_cart('test.db')
	print (userID)
	return obj.getItemList(userID)

def ComparePin(data):
	database = db('test.db')
	user = []
	user = data.split(',',1)
	userID = user[0]
	enteredPin = user[1]
	user_list = database.selectQuery('users',['*'],['ID = ' + str(userID)])
	salt = user_list[0][6]
	hashedPin = user_list[0][7]
	enteredPin = enteredPin.encode('utf-8')
	salt = salt.encode('utf-8')
	enteredPin = enteredPin + salt
	enteredPin = SHA256.new(enteredPin).hexdigest()
	if enteredPin == hashedPin:
		itemList = getItemList(userID)
		data = ",".join(itemList)
		return data
	else:
		return "incorrect pin"




def Main():
    
    host = "192.168.0.111"
    port = 3000
     
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
            data = ComparePin(data)

            # data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()