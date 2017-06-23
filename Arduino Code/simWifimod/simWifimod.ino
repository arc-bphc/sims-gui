/* This program sets up wifi and connects to server 
 * starts a loop which pings the server every 30s 
 * if ping fails, tries reconnecting
 * The intial setup of the wifi module is done by setupEsp(), called in arduino setup()
 * espStatus() is called in arduino loop(), which calls updateEsp() 
 * which tries pinging,else reconnects 
 */
#include<SoftwareSerial.h>

#define esp Serial3

//SoftwareSerial esp(10,11);

//enables debug and messages on Serial
boolean debug=true;
boolean msg=true;

//boolean variables for initial setup
boolean esp_reset=false;
boolean esp_init=false;
boolean wifi_connected=false;
boolean server_connected=false;
boolean esp_setup=false;

//store time in ms after last ping
long updateTime=0;
//no of times updateEsp() failed
int update_fails=0;

//this identifies the module to the server
int shelf_id=0xF2;

//user id and pin 
//to be sent to server to fetch items list
String userpin="025678";

//ssid and pwd for wifi
String ssid="ARC";
String pwd="bphc@arc";

//ip of server
String server_ip="192.168.0.100";

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
      return true;
    }
    else if(response.indexOf("FAIL")!=-1){
      return false;
    }
    else if(response.indexOf("ERROR")!=-1){
      return false;
    }
    else if((millis()-startTime)>100){
      return false;
    }
  
  }
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
        continue;
      }
      else{
        return -1;                         
      }
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
    debugOut("connected to wifi");
    return true;
  }
  String response="";
  if(executeCommand("AT+CWJAP=\""+ssid+"\",\""+pwd+"\"",response)){
    return true;
  }
  else{
    return false;
  }
}

//set esp mode to station and enable multiple connections
boolean setModesEsp(){
  String response="";
  if(!checkCommandStatus("AT+CWMODE?","1",response)){
    debugOut("Setting connection mode to station");
    if(!executeCommand("AT+CWMODE=1",response)){
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
  if(executeCommand(String("AT+CIPSTART=")+"0,\"TCP\",\""+ip+"\","+port,response)){
    msgOut("connected to "+ip);
    return true;
  }
  else{
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
  debugOut("data:");
  if(response!=""){
    debugOut(response);
    resp=response;
    return int(data_size);
  }
  
  
  return -1;
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
    else
      return true;
  }
  else{
    debugOut("data refused");
    return false;
  }
}

//fn to setup esp module
boolean setupEsp(){
  if(!esp_setup){
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
  if(esp_init){
    wifi_connected=wifiConnectEsp(ssid,pwd);
    delay(100);
    if(wifi_connected){
      debugOut("wifi connected");
      //tries connecting to server
      //setupEsp() returns true even if
      //server connection fails
      if(!initServer())
        msgOut("server failed");
      clearEsp();
      if(wifi_connected){
        msgOut("setup complete");
        return true;
      }
    }
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
    String response="";
    readDataEsp(response);
    Serial.println(int(response[0]));
    if(byte(response[0])==0x01){
      Serial.println(millis()-t1);
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
  //checks wifi connection every 2s
  if(((millis()-updateTime)%2000)==0){
    if(!isWifiConnectedEsp(ssid,pwd)){
      esp_init=false;
      wifi_connected=false;
    }
  }
  //tries pinging server every 30s
  if((millis()-updateTime)>30000){
    clearEsp();
    updateTime=millis();
    if(!esp_setup){
      esp_setup=setupEsp();
      return esp_setup;
    }
    else if((!esp_init) || (!wifi_connected)){
      return setupEsp();
    }
    else if(!server_connected){
      if(initServer())
        return true;
    }
    else{
      if(!pingServer()){
        if(initServer())
          return true;
      }
      else{
        return true;
      }
    }
    
    return false;
  }
  return true;
  
}

//fn called in loop, to check esp status
void espStatus(){
  if(!updateEsp()){
    update_fails++;
    //resets esp if updateEsp() fails 10 times
    if(update_fails>=10){
      update_fails=0;
      esp_setup=false;
    }
  }
  else
    update_fails=0;
}

void setup() {
  // put your setup code here, to run once:
  esp.begin(57600);
  Serial.begin(115200);
  pinMode(8,OUTPUT);
  esp_setup=setupEsp();
  updateTime=millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  espStatus();
  
  if(Serial.available()){
    char choice=Serial.read();
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
