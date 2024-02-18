#include <PCA95x5.h>
#include <Wire.h>
PCA9535 ioexBtns1;

int btnSel1sc=0;
int btnSel2sc=0;
int btnSel3sc=0;
int btnSel4sc=0;
int btnSel5sc=0;
int btnSel6sc=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Wire.begin();
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

  Wire.onReceive(receiveEvent);
   
  Serial.println(F("Booted PCAs"));
}

void loop() {
  // put your main code here, to run repeatedly:

}
