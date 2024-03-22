#include <Wire.h>

const int I2C_esp32 = 0x50 ;
const int I2C_pico = 0x51 ;

const int I2C_SDA = 21 ;
const int I2C_SCL = 22 ;

void setup() {
  // put your setup code here, to run once:
  //Wire.begin(I2C_SDA, I2C_SCL);
  Wire.begin(I2C_esp32);  // Listening Address
  Serial.begin(115200);
  Wire.onReceive(receiveEvent);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("1");
  while (Wire.available()) {
    char c = Wire.read(); // Read the incoming byte
    Serial.print(c); // Print the received byte to serial monitor
  }
  delay(100);
}
void Send_I2C(String msg){   
  Wire.beginTransmission(I2C_pico);
  Wire.write(msg.c_str());
  Wire.endTransmission();
}
void receiveEvent(int numBytes) {
  String data = "";
  while(1 < Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    data += (char)c;
  }
  char c = Wire.read(); // receive byte as a character
  data += (char)c;
  Serial.println(data);         // print the integer
  parseData(data);
}
void parseData(String data) {      // split the data into its parts
  const byte numChars = 80;
  char messageHeader[numChars] = {0};
  char messageData[numChars] = {0};

  
  // Length (with one extra character for the null terminator)
  int str_len = data.length() + 1; 
  
  // Prepare the character array (the buffer) 
  char char_array[str_len];
  
  // Copy it over 
  data.toCharArray(char_array, str_len);

  char * strtokIndx; // this is used by strtok() as an index

  strtokIndx = strtok(char_array,",");
  strcpy(messageHeader, strtokIndx);

  strtokIndx = strtok(NULL,",");
  strcpy(messageData, strtokIndx);
  
  Serial.print("header: ");
  Serial.print(messageHeader);
  Serial.print(" data: ");
  Serial.println(atoi(messageData));

  if(messageHeader[0] == 'C'){
        
  } else if(messageHeader[0] == 'P'){
    
  } else if(messageHeader[0] == 'T'){
    
  } else if(messageHeader[0] == 'R'){
    
  } else if(messageHeader[0] == 'S'){
    
  }

}
