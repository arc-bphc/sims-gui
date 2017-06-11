#include<SoftwareSerial.h>

SoftwareSerial esp(10,11);

boolean debug=true;
boolean msg=true;

boolean esp_reset=false;
boolean esp_init=false;
boolean wifi_connected=false;
boolean server_connected=false;
boolean esp_setup=false;

long updateTime=0;
int update_fails=0;

int shelf_id=0xF2;

String userpin="025678";

String ssid="TP-LINK";
String pwd="12345678";

int debugOut(String S){
  if(debug)
    return Serial.println(S);
  else
    return -1;
}

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

int msgOut(String S){
  if(msg)
    return Serial.println(S);
  else
    return -1;
}

void clearEsp(){
  while(esp.available()){
    esp.read();
  }
}

boolean resetEsp(){
  msgOut("resetting..");
  digitalWrite(8,LOW);
  delay(10);
  digitalWrite(8,HIGH);
  delay(2000);
  clearEsp();
  int count=0;
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

//attempts executing a command.No of repeats specified in attempts
//returns:
//1:success
//2:failed
//-1:timeout
int executeCommand(String Command,String &response,int attempts=3){
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

boolean isWifiConnectedEsp(String ssid,String pwd,int strength=0){
  String response= "";
  if(checkCommandStatus("AT+CWJAP?",ssid,response)){
    return true;
  }
  else
    return false;
}

boolean wifiConnectEsp(String ssid,String pwd){
  
  if(isWifiConnectedEsp(ssid,pwd)){
    debugOut("connected to wifi");
    return true;
  }
  String response="";
  
  int ret=executeCommand("AT+CWJAP=\""+ssid+"\",\""+pwd+"\"",response);
  if(ret==1){
    return true;
  }
  else if(ret==-1){
    return false;
  }
  else{
    return false;
  }
}

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

boolean isServerConnectedEsp(String ip){
  String response="";
  if(checkCommandStatus("AT+CIPSTATUS",ip,response)){
    debugOut("connected to "+ip);
    return true;
  }
  else
    return false;
}

boolean connectToServerEsp(String ip,String port){
  String response="";
  
  executeCommand(("AT+CIPCLOSE=0"),response,1);
     
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
//returns(boolean):
//  True-if data sen
//  False-failed
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
  delay(1);
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

boolean requestList(String &pin,String &reply){
  if(!isServerConnectedEsp("192.168.0.101")){
    server_connected=false;
    return false; 
  } 
  
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

boolean initServer(){
  server_connected=false;
  clearEsp();
  if(!connectToServerEsp("192.168.0.101","8080"))
    return false;
  String reply="";
  writeDataEsp(shelf_id);
  readDataEsp(reply,200);
  debugOut(String(byte(reply[0])));
  if(byte(reply[0])==0x01){ 
    debugOut("");
    server_connected=true;
    return true;
  }
  else
    return false;
}

boolean pingServer(){
  if(server_connected){
    long t1=millis();
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

boolean updateEsp(){
  if(((millis()-updateTime)%2000)==0){
    if(!isWifiConnectedEsp(ssid,pwd)){
      esp_init=false;
      wifi_connected=false;
    }
  }
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

void espStatus(){
  if(!updateEsp()){
    update_fails++;
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
  delay(1000);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  espStatus();
  if(Serial.available()){
    int choice=Serial.parseInt();
    switch(choice){
      case 1:
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
      case 2:{
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
