#include <SoftwareSerial.h>
#define DEBUG true
#define ledPin 13

String income_wifi = "";
 
SoftwareSerial esp01(2,3); 
 
void setup() {
  Serial.begin(9600);
  esp01.begin(9600); // your esp's baud rate might be different
  pinMode(ledPin, OUTPUT);
  sendData("AT+RST\r\n",2000,DEBUG); // reset module
  sendData("AT+CWMODE=2\r\n",1000,DEBUG); // configure as access point (working mode: AP+STA)
  sendData("AT+CWSAP=\"ESP-01\",\"1234test\",11,0\r\n",1000,DEBUG); // join the access point
  sendData("AT+CIFSR\r\n",1000,DEBUG); // get ip address
  sendData("AT+CIPMUX=1\r\n",1000,DEBUG); // configure for multiple connections
  sendData("AT+CIPSERVER=1,80\r\n",1000,DEBUG); // turn on server on port 80
}
 
void loop() {
  if (esp01.available()) { 
    if (esp01.find("+IPD,")) {
      income_wifi = esp01.readStringUntil('\r');
      String wifi_temp = income_wifi.substring(income_wifi.indexOf("GET /")+5, income_wifi.indexOf("HTTP/1.1")-1);
      if(wifi_temp == "on"){  // wifi_temp는 지역변수로서 "if (esp01.find("+IPD,")){} 함수를 나가면 초기화됨.
        digitalWrite(ledPin, HIGH);
      }
      else if(wifi_temp == "off"){  
        digitalWrite(ledPin, LOW);  
      }
      else {
        Serial.println(wifi_temp); 
      }
    }
  }
}
 
String sendData(String command, const int timeout, boolean debug) {
  String response = "";
  esp01.print(command); // send the read character to the esp01
  long int time = millis();
  while( (time+timeout) > millis()) {
    while(esp01.available()) {  // The esp has data so display its output to the serial window 
      char c = esp01.read(); // read the next character.
      response+=c;
    }
  }
  if(debug) Serial.print(response);
  return response;
}
