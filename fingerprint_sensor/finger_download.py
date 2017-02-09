import serial
import time

ser=serial.Serial('/dev/serial0',baudrate=57600)




header=[0xef,0x01]

address=[0xff,0xff,0xff,0xff]



def genImg():
    genImg_header=[0x01,0x00,0x03,0x01,0x00,0x05]

    command=header+address+genImg_header
    ser.write(bytearray(command))
    
    __,s=read_packet()

    result=s[9]
    return int(ord(result))


def Img2Tz(buf):

    Img2Tz_header1=[0x01, 0x00, 0x04, 0x02, buf, 0x00, 0x08]
    Img2Tz_header2=[0x01, 0x00, 0x04, 0x02, buf, 0x00, 0x09]

    if buf == 0x01:
        command=header+address+Img2Tz_header1

    elif buf ==0x02:
        command=header+address+Img2Tz_header2

    else:
        pass

    ser.write(bytearray(command))

    __,s=read_packet()

    result=s[10]
    return int(ord(result))


def RegModel():

    RegModel_header=[0x01, 0x00, 0x03, 0x05, 0x00, 0x09]

    command=header+address+RegModel_header

    ser.write(bytearray(command))

    __,s=read_packet()

    result=s[9]

    return int(ord(result))

def UpChar(buf_ID=0x01):

    UpChar_header=[0x01, 0x00, 0x04 ,0x08, buf_ID, 0x00, 0x0e]

    command=header+address+UpChar_header

    ser.write(bytearray(command))

    __,s=read_packet()

    result=s[9]

    return int(ord(result))

def DownChar(data,buf_ID=0x01):

    DownChar_header=[0x01, 0x00, 0x04 ,0x09, buf_ID, 0x00, 0x0f]

    command=header+address+DownChar_header

    ser.write(bytearray(command))

    __,s=read_packet()

    ret=s[9]

    return int(ord(ret))

def Match():

    Match_header=[0x01, 0x00, 0x03 ,0x03, 0x00, 0x07]

    command=header+address+Match_header

    ser.write(bytearray(command))

    __,s=read_packet()

    ret=s[9]

    return int(ord(ret))


def enroll():
    time.sleep(1)
    print "enroll fingerprint:"

    print "put your finger to the sensor"
    while True:
        if genImg()==0:
            break

    print "fingerprint accepted"
    if(Img2Tz(0x01)==0):
        print "img to text complete"
    else:
        print "conversion of first image failed"

    print "put your finger to the sensor once more"
    while True:
        if genImg()==0:
            break
    if(Img2Tz(0x02)==0):
        print "img to text complete"
    else:
        print "conversion of second image failed"

    return RegModel()

def read_packet():
    while ser.inWaiting()<9:
        pass

    s=ser.read(9)

    if ([hex(ord(c)) for c in s[0:6]] != [hex(c) for c in (header+address)]):
        print "data not in sync"
        return False, None

    pack_length= int(ord(s[7])*256) + int(ord(s[8]))

    while abs(ser.inWaiting())<pack_length:
        pass

    s= s+ ser.read(pack_length)

    return True, s


if __name__=='__main__':

    fname=raw_input('Enter file name: ')
    f=open(fname,'rb')

    data=f.read()

    ret=DownChar(data)

    if(ret== 0x0):
        print 'transferring data to sensor'
    else:
        print 'unable to transfer data'

    ser.write(data)

    UpChar()

    s=''
    
    while ser.inWaiting()!=0:

        ret,fdata=read_packet()

        if ret == 0:
            break

        s=s+fdata

    if s==data:
        print 'template matching with file'

    print "put your finger to the sensor"
    while True:
        if genImg()==0:
            break
    print "fingerprint accepted"
    if(Img2Tz(0x02)==0):
        print "img to text complete"

    if Match()==0:
        print 'finger matching'
    else:
        print 'finger not matched'

    

        

    
