from multiprocessing import Process
import socket
import time
import sqlite3
import hashlib
import random

#connect to database
database_path='./../sql/'
db=sqlite3.connect(database_path+'SIMS.db')
cursor=db.cursor()

#base class for all exceptions
class Error(Exception):
    pass

#class for database related errors
class dbError(Error):
    def __init__(self,msg):
        self.message="Database error:"+str(msg)
        
#class for connection related errors
class connError(Error):
    def __init__(self,msg):
        self.message="Connection error:"+str(msg)


def executeDB(command,arguments=None,conn=False,except_raise=True):
    '''    
    fn to execute db commands and retrieve results
    params:command:<String>: Sql command to execute
           arguments:<iterable> optional arguments for sql commands
           conn:<boolean> selects connError or dbError
           except_raise:<boolean> controls exception rasising
    returns:<List of tuples> response of sql query
    '''
    response=cursor.execute(command,arguments).fetchall()
    if response==[] and except_raise:
        if conn:
            raise connError('no results found for:'+command+str(arguments))
        else:
            raise dbError('no results found for:'+command+str(arguments))
    else:
        return response

def createPassword(text,salt):
    '''
    fn to encode userpin into hashed format
    to compare with database
    params:
        text: pin to encode
        salt: salt to use for encoding
    returns hashed password
    '''
    salt=salt.encode('utf-8')
    text=text.encode('utf-8')
    text = text + salt
    #text.encode('utf-8')
    hash_object = hashlib.sha256(text)
    password = hash_object.hexdigest()
    return password	

def createItemsList(id_no,shelf_no,null_val):
    '''
    get transaction details(item_id,quantity) from database based on id_no for withdraw and return, specified by null_val
    uses item_id it to to get item details for each item and parses all the items and details to a string
    arguments:
    id_no:<int> user id no for the transaction
    shelf_no:<int> shelf number
    null_val:<str> 'NOT NULL' or 'NULL' to obtain list of items to withdraw/return
    returns: <str> item details of all items in the transacition
    '''
    try:
        transaction=executeDB('select ITEM_ID,QUANTITY from transactions where ID=(?) AND WITHDRAW_DATETIME IS '+null_val,[id_no])
        item_ids=[]
        quantity=[]
        #split o/p of sql query: transaction
        for i in transaction:
            item_ids.append(i[0])
            quantity.append(i[1])
        item_details=[]
        #get item details for each item from transaction
        #based on item_id and shelf_no
        for i in item_ids:
            result=executeDB('select NAME,RFID,BOX_NO from inventory where ITEM_ID=(?) AND SHELF_NO=(?)',[i,shelf_no],except_raise=False)
            #when an item isn't there in shelf 
            if result==[]:
                #helps when sending quantity
                item_details=item_details+['']
            else:
                item_details=item_details+result
        items_string=''
        #generator which gives index for each successive
        #item in item_details
        index=(i for i in range(len(item_details)))
        #item_details made into a string
        #quantity is added using the generator
        #for '' in item_details, generator is called simply to increment index
        for i in item_details:
            if i!='':
                items_string=items_string+','.join([i[0],i[1],str(i[2]),str(quantity[next(index)])])+'#'
            else:
                next(index)
        return items_string
    except (dbError,connError):
        return ''

def clientHandler(conn,address):
    '''
    fn to handle a new client connection
    started as a seperate process
    params:    conn<socket> new connection
               address:<string>
    returns: void
    '''
    try:
        conn.settimeout(1)
        #first the client id is received
        client_id=conn.recv(1024)
        if client_id=='':
            raise connError('blank client id')
        #the bytes object is converted to an integer
        client_id=bytes(client_id)[0]
        #retrieve shelf no corresponding to client_id
        shelf_no=executeDB('SELECT SHELF_ID FROM shelf WHERE CODE=(?)',[client_id],True)
        shelf_no=shelf_no[0][0]
        print("connected to"+str(address),"shelf no:"+str(shelf_no))
        conn.send(bytearray([0x01]))
        #start timer
        time1=int(time.perf_counter())
        while True:
            try: 
                # the loop will exit if left unresponsive for 45s
                if((int(time.perf_counter())-time1)>45):
                    print("time elapsed:"+str(int((time.perf_counter()-time1))))
                    break
                
                #check for incoming data
                dat=conn.recv(1024)
                if len(dat)==0:
                    continue

                #ping
                elif dat[0]==0x20:
                    conn.send(bytearray([0x01]))
                    time1=int(time.perf_counter())
                    print("received ping")

                #retrieve data   
                elif dat[0]==0x10:
                    conn.send(bytearray([0x01]))
                    #receive user password/messaage
                    msg=conn.recv(1024)
                    if len(msg)!=6:
                        raise connError('message corrupt')
                    msg=msg.decode()
                    print('message:'+msg)
                    #split into id_no and password
                    id_no=int(msg[:2])
                    pwd=msg[2:]
                    del msg
                    #retrieve password from db based on id_no
                    salt,password=executeDB('select SALT,HASHED_PASSWORD from users where ID=(?)',[id_no],True)[0]
                    if (password!=createPassword(pwd,salt)):
                            raise connError('password not matching')
                    
                    items_string=createItemsList(id_no,shelf_no,'NULL')+'&'
                    items_string=items_string+createItemsList(id_no,shelf_no,'NOT NULL')
                    if items_string=='&' or items_string==None:
                        raise dbError("no data from db")
                    else:
                        print("sending data:"+items_string)
                        conn.send((items_string).encode())
                else:
                    continue
            #handling possible and allowed errors
            except dbError as err:
                print(err.message)
                conn.send(bytearray([0x08]))
                continue
            except connError as err:
                print(err.message)
                conn.send(bytearray([0x09]))
            except socket.timeout:
                continue
            
    except connError as err:
        print(err.message)
        conn.send(bytearray([0x02]))
    except socket.timeout:
        raise connError('no id received')
        
    finally:
        conn.close()

if __name__=='__main__':
    '''
    this block is required since each process executes the script file
    anything outside the block gets redundantly executed
    '''
   
    try:
        host=''
        port=8080

        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen(10)
        #to store all new processes
        processes=[]
        while True:
            print("accepting conns:")
            conn,address=s.accept()
            #starts a new process
            conn_handler=Process(target=clientHandler,args=(conn,address))
            processes.append(conn_handler)
            conn_handler.start()
    finally:
        s.close()


