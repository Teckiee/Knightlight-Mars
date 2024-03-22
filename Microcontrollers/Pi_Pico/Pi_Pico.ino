#include <PCA95x5.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SoftwareSerial.h>
#include "pico/multicore.h"

#define TX_PIN 13 // next pcb version swaps these
#define RX_PIN 12
SoftwareSerial HostCommsSerial(RX_PIN, TX_PIN);

#define RX_BUF_SIZE 128
volatile char rx_buffer[RX_BUF_SIZE];
volatile int rx_index = 0;

const int I2C_esp32 = 0x50 ;
const int I2C_pico = 0x51 ;

PCA9535 ioexBtns1;

int btn1sc=0;
int btn2sc=0;
int btn3sc=0;
int btn4sc=0;
int btn5sc=0;
int btn6sc=0;
long int btnioex1SC = 0 ;
long int btnioex2SC = 0 ;

#define TFT_DC   9                                                       // data/command line

#define TFT_Res1  2                                                       // reset line (optional, pass -1 if not used)
#define TFT_CS1   3                                                       // chip select line
Adafruit_ST7735 tft1 = Adafruit_ST7735(TFT_CS1, TFT_DC, TFT_Res1);
#define TFT_Res2  6
#define TFT_CS2   7
Adafruit_ST7735 tft2 = Adafruit_ST7735(TFT_CS2, TFT_DC, TFT_Res2);
#define TFT_Res3  8
#define TFT_CS3   10
Adafruit_ST7735 tft3 = Adafruit_ST7735(TFT_CS3, TFT_DC, TFT_Res3);
#define TFT_Res4  28
#define TFT_CS4   27
Adafruit_ST7735 tft4 = Adafruit_ST7735(TFT_CS4, TFT_DC, TFT_Res4);
#define TFT_Res5  26
#define TFT_CS5   22
Adafruit_ST7735 tft5 = Adafruit_ST7735(TFT_CS5, TFT_DC, TFT_Res5);
#define TFT_Res6  21
#define TFT_CS6   20
Adafruit_ST7735 tft6 = Adafruit_ST7735(TFT_CS6, TFT_DC, TFT_Res6);

#define BLACK   0x0000
#define WHITE   0xFFFF
#define BLUE    0x07FF
#define RED     0xFFE0 
#define GREEN   0xF81F
#define CYAN    0xFFE0
#define MAGENTA 0x07E0
#define YELLOW  0xF800 
#define ORANGE  0xFE00  
#define POISON  0x68FF
uint16_t skyBlue = 0x001F;

unsigned long currentMillis = millis();
unsigned long previousMillis = 0;
unsigned long previousDisplayMillis = 0;
const long interval = 330;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  // Configure the UART settings
  //uart_set_hw_flow(UART_ID, false, false);
  //uart_set_format(UART_ID, 8, 1, UART_PARITY_NONE);
  //uart_set_fifo_enabled(UART_ID, false);
  
  HostCommsSerial.begin(115200);
  
  multicore_launch_core1(receive_from_host);
  
  Wire.begin();
  Wire.begin(I2C_pico);
  Wire.onReceive(receiveEvent);
  ioexBtns1.attach(Wire,0x20);
  ioexBtns1.polarity(PCA95x5::Polarity::ORIGINAL_ALL);

  ioexBtns1.direction(PCA95x5::Port::P00,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P01,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P02,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P03,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P04,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P05,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P06,PCA95x5::Direction::IN);
  ioexBtns1.direction(PCA95x5::Port::P07,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P10,PCA95x5::Direction::IN);
  ioexBtns1.direction(PCA95x5::Port::P11,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P12,PCA95x5::Direction::IN);
  ioexBtns1.direction(PCA95x5::Port::P13,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P14,PCA95x5::Direction::IN);
  ioexBtns1.direction(PCA95x5::Port::P15,PCA95x5::Direction::OUT);
  ioexBtns1.direction(PCA95x5::Port::P16,PCA95x5::Direction::IN);
  ioexBtns1.direction(PCA95x5::Port::P17,PCA95x5::Direction::OUT);

  ioexBtns1.write(PCA95x5::Port::P00,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P01,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P02,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P03,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P04,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P05,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P07,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P11,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P13,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P15,PCA95x5::Level::L);
  ioexBtns1.write(PCA95x5::Port::P17,PCA95x5::Level::L);

   
  Serial.println(F("Booted PCAs"));
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;

    //Serial.print("X: ");
    //Serial.print(" Y: ");
    //Serial.print(" Z: ");
  }
  

// 0/0 = [16]
// 0/1 = [15]
// 0/2 = [14]
// 0/3 = [13]
// 0/4 = [12]
// 0/5 = [11]
// 0/6 = [10]
// 0/7 = [9]
// 1/0 = [8]
// 1/1 = [7]
// 1/2 = [6]
// 1/3 = [5]
// 1/4 = [4]
// 1/5 = [3]
// 1/6 = [2]
// 1/7 = [1]

  btnioex1SC = ioexBtns1.read();
  int ioexBtns1binary[16] = {} ;
  long int num = btnioex1SC ;
  for (int i = 16; i > 0; i--) {
    ioexBtns1binary[i] = num%2;
    num = num/2;
  }
// ------------------------------------------------------------ ioexBtns1 1
  if(btn1sc != ioexBtns1binary[2]){
    btn1sc = ioexBtns1binary[2];
    if (btn1sc == 1){
      Serial.println("Button 1-1 Down");
      ioexBtns1.write(PCA95x5::Port::P17,PCA95x5::Level::H);
      sendtohost("btn1-1,down");
    } else if (btn1sc == 0){
      Serial.println("Button 1-1 Up");
      ioexBtns1.write(PCA95x5::Port::P17,PCA95x5::Level::L);
      sendtohost("btn1-1,up");
    }
  }
// ------------------------------------------------------------ ioexBtns1 2
    if(btn2sc != ioexBtns1.read(PCA95x5::Port::P14)){
      btn2sc = ioexBtns1.read(PCA95x5::Port::P14);
      if (btn2sc == 1){
        Serial.println("Button 1-2 Down");
        ioexBtns1.write(PCA95x5::Port::P15,PCA95x5::Level::H);
        sendtohost("btn1-2,down");
      } else if (btn2sc == 0){
        Serial.println("Button 1-2 Up");
        ioexBtns1.write(PCA95x5::Port::P15,PCA95x5::Level::L);
        sendtohost("btn1-2,up");
      }
    }
// ------------------------------------------------------------ ioexBtns1 3
    if(btn3sc != ioexBtns1binary[6]){
      btn3sc = ioexBtns1binary[6];
      if (btn3sc == 1){
        Serial.println("Button 1-3 Down");
        ioexBtns1.write(PCA95x5::Port::P13,PCA95x5::Level::H);
        sendtohost("btn1-3,down");
      } else if (btn2sc == 0){
        Serial.println("Button 1-3 Up");
        ioexBtns1.write(PCA95x5::Port::P13, PCA95x5::Level::L);
        sendtohost("btn1-3,up");
      }
    }
}
void sendtohost(String data){
  // Length (with one extra character for the null terminator)
  int str_len = data.length() + 1; 
  
  // Prepare the character array (the buffer) 
  char char_array[str_len];
  
  // Copy it over 
  data.toCharArray(char_array, str_len);
  Send_I2C(data);
  HostCommsSerial.println(char_array);
}
void Send_I2C(String msg){   
  Wire.beginTransmission(I2C_esp32);
  Wire.write(msg.c_str());
  Wire.endTransmission();
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
  
  //Serial.print("header: ");
  //Serial.print(messageHeader);
  //Serial.print(" data: ");
  //Serial.println(atoi(messageData));

  if(messageHeader[0] == 'E'){
    
  } else if(messageHeader[0] == 'F'){
    
  } else if(messageHeader[0] == 'X'){
    
  } else if(messageHeader[0] == 'Y'){
    
  } else if(messageHeader[0] == 'Z'){
    
  }

}
void receiveEvent(int numBytes) {
  String data = "";
  while(1 < Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    data += (char)c;
  }
  char c = Wire.read(); // receive byte as a character
  data += (char)c;
  //Serial.println(data);         // print the integer
  parseData(data);
}
void receive_from_host() {
  String receivedData;
  while (true) {
    if (HostCommsSerial.available() > 0) {
      char receivedByte = HostCommsSerial.read();
      receivedData += receivedByte;
      if (receivedByte == '\n') {
        // Decode the received data as UTF-8 and print it
        //String decodedData = receivedData.decodeUTF8();
        Serial.print("Received: ");
        Serial.print(receivedData);
        
        // Clear the receivedData string for the next message
        receivedData = "";
      }
    }
  }
}
void displayDetails(){   
  previousDisplayMillis = currentMillis;
  tft1.enableDisplay(true);
  
  //tft.fillRect (120,35,30,5,GREEN);                                                                   // color bar 01
   //tft.fillRect (120,45,30,5,RED);                                                                     // color bar 02
   //tft.fillRect (120,55,30,5,YELLOW);                                                                  // bcolor ar 03
   //tft.fillRect (120,65,30,5,POISON);                                                                  // color bar 04
   //tft.fillRect (120,75,30,5,MAGENTA);                                                                 // color bar 05
   //tft.fillRect (120,85,30,5,YELLOW);                                                                  // color bar 06
   //tft.fillRect (120,95,30,5,ORANGE);                                                                  // color bar 07
   char wordText[] = "Hi!" ;
   DrawText(5,5,wordText,1,6); //Write text to screen
   
  //delay(1000);
}
void cleardisplay(){   
    //tm1637.display(3, 0x7f);   
    //tm1637.display(2, 0x7f);   
    //tm1637.display(1, 0x7f);   
    //tm1637.display(0, 0x7f);
    //digitalWrite(TFT_BL, LOW);
    //tft.enableDisplay(false);
}
void DrawText(int x, int y, char text[],int fSize, int Ssize){
  int spacing = 0;
  size_t len = strlen(text);
  for (int letter = 0; letter < len; letter++){
    tft1.drawChar(x+spacing,y,text[letter],skyBlue,BLACK,fSize);
    spacing+=Ssize;
  }
  /*for (int letter = 0; letter < len; letter++) {
    // Check if the text exceeds the screen width
    if (x + spacing + Ssize > screenWidth) {
      // If so, move to the next line
      y += fSize * 8; // Assuming 8 pixels per character height for the font size
      spacing = 0; // Reset spacing for the new line
    }
    // Draw the character
    tft.drawChar(x + spacing, y, text[letter], skyBlue, BLACK, fSize);
    spacing += Ssize;
  }*/
}
