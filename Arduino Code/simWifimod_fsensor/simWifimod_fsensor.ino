 
/* This program sets up wifi and connects to server 
 * starts a loop which pings the server every 30s 
 * if ping fails, tries reconnecting
 * The intial setup of the wifi module is done by setupEsp(), called in arduino setup()
 * espStatus() is called in arduino loop(), which calls updateEsp() 
 * which tries pinging,else reconnects 
 */
#include<SoftwareSerial.h>
#include "FPS_GT511C3M.h"
#define esp Serial2

//SoftwareSerial esp(10,11);
FPS_GT511C3 fps(false);
//enables debug and messages on Serial
boolean debug=true;
boolean msg=true;

//boolean variables for initial setup
boolean esp_reset=false;
boolean esp_init=false;
boolean wifi_connected=false;
boolean server_connected=false;

//this variable when false, causes updateEsp() to call setupEsp()
//this is useful when wifi/server etc fails. setupEsp() will try reconnectiing
boolean esp_setup=false;

//store time in ms after last ping
long updateTime=0;
//no of times updateEsp() failed
int update_fails=0;

//this identifies the module to the server
int shelf_id=0xFF;

//user id and pin 
//to be sent to server to fetch items list
String userpin="025678";

//ssid and pwd for wifi
String ssid="ARC";
String pwd="bphc@arc";

//ip of server
String server_ip="192.168.0.105";

//to output debug messages to serial
int debugOut(String S){
  if(debug)
    return Serial.println(S);
  else
    return -1;
}
//overloaded version
int debugOut(char *S,int len){
  if(debug){
    String message="";
    for(int i=0;i<len;++i)
      message+=S[i];
    return Serial.println(message);
  }
  else
    return -1;
}
int debugOut(byte *S,int len){
  String message="";
  for(int i=0;i<len;++i){
    message+=String(S[i])+" ";
  }
  return debugOut(message);
}
//to output message on Serial
int msgOut(String S){
  if(msg)
    return Serial.println(S);
  else
    return -1;
}

//clear esp input buffer
void clearEsp(){
  while(esp.available()){
    esp.read();
  }
}

void clearSensor(){
  while(_serial.available()){
    _serial.read();
  }
}

//to reset esp module
boolean resetEsp(){
  msgOut("resetting..");
  digitalWrite(22,LOW);
  delay(10);
  digitalWrite(22,HIGH);
  delay(2000);
  clearEsp();
  int count=0;
  //sends AT to esp module and gets response
  while(testEsp()!=1){
    if(count>3){
      return false;
    }
    count++;
    delay(1000);
  }
  return true;
}

//Test esp module by sending:"AT" 
//returns:
//1:OK
//0:busy
//-1:<no response>
int testEsp(){
  String response="";
  esp.println("AT");
  delay(5);
  long startTime=millis();
  while((millis()-startTime)<10){
    if(esp.available())
      response+=(char)esp.read();
    if(response.indexOf("OK")!=-1){
      return 1;
    }
    else if(response.indexOf("busy")!=-1){
      debugOut(response);
      return 0;
    }
    else
      continue; 
  }
  debugOut(response);
  return -1;  
}

//executes commands for checking status of wifi,server etc
//searches the response for checkword
//if checkword found,returns true
//response: stores response after executing command
boolean checkCommandStatus(String Command,String checkword,String &response){
  long startTime;
  clearEsp();
  //check if esp is ready to receive commands
  int count=0;
  esp.println(Command);
  startTime=millis();
  response="";
  while(1){
    if(esp.available())
      response+=(char)esp.read();
    if(response.indexOf(checkword)!=-1){
      delay(5);
      clearEsp();
      return true;
    }
    else if(response.indexOf("FAIL")!=-1){
      break;
    }
    else if(response.indexOf("ERROR")!=-1){
      break;
    }
    else if((millis()-startTime)>100){
      break;
    } 
  }
  return false;
}

//attempts executing a command
//returns:
//1:success
//2:failed
//-1:timeout
//arguments:
//command: command to execute
//store: to store response after executing command
int executeCommand(String Command,String &response){
  long startTime;
  clearEsp();
  //check if esp is ready to receive commands
  int count=0;
  while(testEsp()!=1){
    if(count>2){
      return -1;
    }
    count++;
    delay(2000);
  }
  count=0;
  esp.println(Command);
  startTime=millis();
  response="";
  while(1){
    if(esp.available())
      response+=(char)esp.read();
    if(response.indexOf("OK")!=-1){
      return 1;
    }
    else if(response.indexOf("FAIL")!=-1){
      return 0;
    }
    else if(response.indexOf("ERROR")!=-1){
      break;
    }
    else if((millis()-startTime)>2000){
      int ret=testEsp();
      if(ret==0){ 
        startTime=millis(); 
        count++;
        continue;
      }
      else{
        return -1;                         
      }
    }
    else if(count>4){
      return -1;
    }
    else
      continue;
  }
  return -1;
}  

//checks if wifi is connected
//arguments:
//ssid: wifi name
//pwd: password
//strength: signal strength<not used>
boolean isWifiConnectedEsp(String ssid,String pwd,int strength=0){
  String response= "";
  if(checkCommandStatus("AT+CWJAP?",ssid,response)){
    return true;
  }
  else
    return false;
}

//connect to wifi
//arguments:
//ssid: wifi hotspot name
//pwd: password
boolean wifiConnectEsp(String ssid,String pwd){
  if(isWifiConnectedEsp(ssid,pwd)){
    msgOut("connected to wifi");
    return true;
  }
  String response="";
  if(executeCommand("AT+CWJAP=\""+ssid+"\",\""+pwd+"\"",response)==1){
    return true;
  }
  else{
    msgOut("wifi connect failed");
    debugOut(response);
    return false;
  }
}

//set esp mode to station and enable multiple connections
boolean setModesEsp(){
  String response="";
  if(!checkCommandStatus("AT+CWMODE?","1",response)){
    debugOut("Setting connection mode to station");
    if(executeCommand("AT+CWMODE=1",response)!=1){
      return false;
    }
  }
  if(checkCommandStatus("AT+CIPMUX?","1",response)){
    return true;
  }
  else{
    if(executeCommand("AT+CIPMUX=1",response)==1){
      return true;
    }
    else{
      return false;
    }
  }
}

//checks if connected to server
//ip: ip of server
boolean isServerConnectedEsp(String ip){
  String response="";
  if(checkCommandStatus("AT+CIPSTATUS",ip,response)){
    debugOut("connected to "+ip);
    return true;
  }
  else
    return false;
}

//connects to server
//arguments:
//ip: ip address of server
//port: port to connect to
boolean connectToServerEsp(String ip,String port){
  String response="";
  executeCommand(("AT+CIPCLOSE=0"),response);
  if(executeCommand(String("AT+CIPSTART=")+"0,\"TCP\",\""+ip+"\","+port,response)==1){
    msgOut("connected to "+ip);
    return true;
  }
  else{
    debugOut(response);
    return false;
  }
}

//sends data to the server 
//connection to server must be made before function call
//arguments:
//  byte *:data to send
//  len: data length
boolean writeDataEsp(byte dat[],int len){
  clearEsp();
  String command="AT+CIPSEND=0,"+String(len);
  esp.println(command);
  long startTime=millis();
  String response="";
  while(1){
    if(esp.available())
      response+=(char)esp.read();
    if(response.indexOf(">")!=-1){
      break;
    }
    else if(response.indexOf("ERROR")!=-1){
      return 0;
    }
    else if((millis()-startTime)>100){
      return false;
    }
  }
  esp.write(dat,len);
  startTime=millis();
  while(1){
    if(esp.available())
      response+=(char)esp.read();
    if(response.indexOf("OK")!=-1){
      return true;
    }
    else if(response.indexOf("ERROR")!=-1){
      return 0;
    }
    else if((millis()-startTime)>100){
      return false;
    }
  }
}

//overloaded function to send string data
boolean writeDataEsp(String &dat,int len){
  byte data[len];
  for(int i=0;i<len;++i)
    data[i]=byte(dat[i]);
  debugOut((char*)data,len);
  return writeDataEsp(data,len);
}

//overloaded function to send a single byte
boolean writeDataEsp(byte dat){
  return writeDataEsp(&dat,1);
}

//to read any data send to the esp from the server
//server connection should be made before function call
//returns: 
//  int:no of bytes received.-1 if no data received
//arguments:
//  resp(byte array): data received from server in bytes
//  timeout(long): timeout in microseconds before returning -1
int readDataEsp(String &resp, long timeout=2000){
  String response="";
  long startTime=millis();
  while(1){
    if(esp.available())
        response+=(char)esp.read();
    if(response.indexOf("+IPD")!=-1){
      debugOut("data received");
      break;
    }
    else if((millis()-startTime)>timeout){
        debugOut("no data available");
        debugOut(response);
        return -1;                           
    }
    else
      continue;
  }
  response="";
  delay(1);
  if(esp.available()<5)
    return -1;
  for(int i=0;i<3;++i)
    esp.read();
  char ch;
  while(esp.available()){
    ch=(char)esp.read();
    if(ch==':')
      break;
    response+=ch;
  }
  int data_size=response.toInt();

  debugOut(String(data_size)+" bytes received");
  delay(10);
  response="";
  for(int i=0;i<data_size;++i){
    if(esp.available()){
        response+=(char)esp.read();      
    }
    else{
      debugOut("data corrupt");
      debugOut(response);
      return -2;
    }
    
  }
  
  resp="";
  resp=response;
  Serial.println(resp.length());
  return int(data_size);
  
}

int readDataEsp(byte *resp,long timeout=2000){
  String response="";
  long startTime=millis();
  while(1){
    if(esp.available())
        response+=(char)esp.read();
    if(response.indexOf("+IPD")!=-1){
      debugOut("data received");
      break;
    }
    else if((millis()-startTime)>timeout){
        debugOut("no data available");
        debugOut(response);
        return -1;                           
    }
    else
      continue;
  }
  response="";
  delay(1);
  if(esp.available()<5)
    return -1;
  for(int i=0;i<3;++i)
    esp.read();
  char ch;
  while(esp.available()){
    ch=(char)esp.read();
    if(ch==':')
      break;
    response+=ch;
  }
  int data_size=response.toInt();

  debugOut(String(data_size)+" bytes received");
  delay(10);
  for(int i=0;i<data_size;++i){
    if(esp.available()){
        resp[i]=(char)esp.read();      
    }
    else{
      debugOut("data corrupt");
      debugOut(resp,i+1);
      return -2;
    }
    
  }
  debugOut("data:");
  debugOut(resp,data_size);
  return data_size;  

}

//to request list of items from server
//arguments:
//pin: user pin
//reply: list of items returned by server
boolean requestList(String &pin,String &reply){
  if(!isServerConnectedEsp(server_ip)){
    server_connected=false;
    return false; 
  } 
  //0x10 is byte code for fetching data
  writeDataEsp(0x10);
  reply="";
  readDataEsp(reply,100);
  if(byte(reply[0])==0x01){
    debugOut("request acknoledged");
    writeDataEsp(pin,6);
    int dsize=readDataEsp(reply);
    if(byte(reply[0])==0x08){
      debugOut("wrong shelf");
      return false;
    }
    else{
      Serial.println(reply);
      return true;
    }
  }
  else{
    debugOut("data refused");
    return false;
  }
}

//fn to setup esp module
boolean setupEsp(){
  if(!esp_reset){
    esp_init=false;
    wifi_connected=false;
    server_connected=false;
    esp_reset=resetEsp();
    delay(100);
    if(esp_reset){
      debugOut("reset done");
    }
  }
  if((esp_reset) && !(esp_init)){
    if(esp_reset && setModesEsp())
      esp_init=true;
    else
      esp_init=false;
    if(esp_init)
      debugOut("init done");
  }
  if(esp_init && !(wifi_connected)){
    wifi_connected=wifiConnectEsp(ssid,pwd);
    delay(100);
  }
  if(wifi_connected && !(server_connected)){
      msgOut("wifi connected");
      //tries connecting to server
      //setupEsp() returns true even if
      //server connection fails
      if(!initServer())
        msgOut("server failed");
  }
  if(server_connected){
        msgOut("setup complete");
        return true;
  }
  msgOut("setup failed");
  return false;
}

// function to establish comm with server
boolean initServer(){
  server_connected=false;
  clearEsp();
  if(!connectToServerEsp(server_ip,"8080"))
    return false;
  String reply="";
  //sends shelf id to server for authentication
  writeDataEsp(shelf_id);
  readDataEsp(reply);
  debugOut(String(byte(reply[0])));
  if(byte(reply[0])==0x01){ 
    debugOut("");
    server_connected=true;
    return true;
  }
  else
    return false;
}

//fn to ping server
boolean pingServer(){
  if(server_connected){
    long t1=millis();
    //send byte code for pinging
    writeDataEsp(0x20);
    byte response[2];
    if(readDataEsp(response)!=-1){
      debugOut("new:"+String(int(response[0]))+" delete:"+String(int(response[1])));
      if(int(response[0])){
        for(int i=0;i<int(response[0]);++i){
          //writeDataEsp(0x01);
          byte reply;
          if(readDataEsp(&reply)!=-1){
            setFingerTemplate(int(reply));
          }
          else
            debugOut("template not received");
        }
      }
      if(int(response[1])){
        for(int i=0;i<int(response[1]);++i){
          byte reply;
          if(readDataEsp(&reply)!=-1){
            deleteEnrollment(int(reply));
          }
          else
            debugOut("template delete failed");
        }
      }
      debugOut("pinged");
      return true;
    }
  }
  debugOut("ping failed");
  return false; 
}

//fn to update esp connection status
//pings server, tries connecting if failed
boolean updateEsp(){
  clearEsp();
  updateTime=millis();
  if(!esp_setup){
    esp_setup=setupEsp();
    return esp_setup;
  }
  else{
    // try pinging server
    if(!pingServer()){
      // reconnect to server, if ping fails
      if(initServer())
        return true;
    }
    else{
      return true;
    }
  }
  // if function hasn't returned true by now, ping and server has failed
  esp_setup=false;
  return false;
}

//fn called in loop, to check esp status
void espStatus(){
  //checks wifi connection every 2s
  if(((millis()-updateTime)%2000)==0){
    if(!isWifiConnectedEsp(ssid,pwd)){
      wifi_connected=false;
      //to call setupEsp() when updateEsp() is called
      esp_setup=false;
    }
  }
  //tries pinging server every 30s
  if((millis()-updateTime)>30000){
    if(!updateEsp()){
      update_fails++;
      //resets esp if updateEsp() fails 10 times
      if(update_fails>=10){
        update_fails=0;
        //will cause esp to reset when updateEsp() is called
        esp_reset=false;
      }
    }
    else
      update_fails=0;
  }
}

boolean setFingerTemplate(int pos){
  clearEsp();
  clearSensor();
  debugOut("pos:"+String(pos));
  byte ftemplate[504];
  byte response[42];
  if(fps.CheckEnrolled(pos)){
    deleteEnrollment(pos);
  }
  int fail_count=0;
  int s=0;
  for(int i=0;i<12;++i){
    writeDataEsp(byte(i+1));
    delay(10);
    debugOut("receive:"+String(i));
    s=readDataEsp(response);
    if(s==-1){
      i--;
      continue;
    }
    for(int j=42*i,k=0;j<j+42,k<42;++j,++k)
      ftemplate[j]=response[k];
    fail_count=0; 
  }
  if(s!=-1){
    if(fps.SetTemplate(pos,ftemplate,false)){
       Serial.println("tmp sent");
    }
    else{
      debugOut("setTemplate failed");
      return false;
    }
    
    clearSensor();
    Serial.println("done");
  }
  if((fps.CheckEnrolled(pos)) && (s!=-1)){
    debugOut("Enrolled:"+String(pos));
    writeDataEsp(0x01);
    return true;
  }
  else{
    debugOut("template-setting error");
    writeDataEsp(0x00);
    return false;
  }
}
//boolean SetTemplate(){
//  byte command[]={0x55,0xAA,0x00,0x01,0x00,0x00,0x00,0x00,0x71,0x0,0x71,0x01};
//  _serial.write(command,12);
//  Serial.print("response:")
//  Serial.println(_serial.available());
//}
boolean deleteEnrollment(int pos){
  if(fps.DeleteID(pos)){
    debugOut("deleted:"+String(pos));
    return true;
  }
  else{
    debugOut("delete failed");
    return false;
  }
}
void setup() {
  // put your setup code here, to run once:
  esp.begin(57600);
  Serial.begin(115200);
  pinMode(8,OUTPUT);
  esp_setup=setupEsp();
  updateTime=millis();
  fps.Open();
  fps.SetLED(1);
  pingServer();
}

void loop() {
  // put your main code here, to run repeatedly:
  espStatus();
  
  if(Serial.available()){
    char choice=Serial.read();
    Serial.println(choice);
    switch(choice){
      case '1':
        {
          String list="";
          
          if(requestList(userpin,list)){
            //Serial.println(list);
            updateTime=millis();
          }
          else
            Serial.println("error");
          break;
        }
      case '2':{
        updateEsp();
        break;
      }
      case '3':{
        clearEsp();
        debugOut("index?");
        while(!Serial.available());
        int enroll_index=Serial.parseInt();
        writeDataEsp(0x70);
        String r="";
        readDataEsp(r);
        
        setFingerTemplate(enroll_index);
        break;
      }
      case '4':{
        clearEsp();
        debugOut("index?");
        while(!Serial.available());
        int delete_index=Serial.parseInt();
        deleteEnrollment(delete_index);
        break;
      }
      default:{
        Serial.println("junk");
        break;
      }
    } 
  }
    
//  while(Serial.available()){
//    esp.write(Serial.read());
//  }
//  delay(100);
//  while(esp.available()){
//    Serial.print((char)esp.read());
//  }
}
