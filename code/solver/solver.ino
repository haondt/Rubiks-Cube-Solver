#define TIME 250
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
int servonums[8] = {4, 5, 0, 1, 8, 9, 14, 15}; // uses indexes from diagram
int servomins[8] = {330, 335, 240, 350, 250, 350, 260, 365}; // uses indexes from diagram,  engage/horizontal pos
int servomaxs[8] = {570, 570, 480, 580, 470, 585, 490, 605}; //uses indexes from diagram, disengage/vertical pos
// engage = min, disengage = max
// vertical (from front to back) = max, horizontal (side to side) = min
char instructions[100] = {0};
int led = 13;
void setup() {
  
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);

  yield();
  delay(1000);
  
  //open up solver
  for(int i=0;i<8;i++){
    // sets each servo to disengage and vertical pos
    pwm.setPWM(servonums[i], 0, servomaxs[i]);
    delay(TIME);
  }
  readCube();
}

void loop() {
  // command format: [servonum],[pos]
  // pos 0 = disengage/vertical
  // pos 1 = engage/horizontal
  // eg: 0,1 ; 5,0 ; 2,1
  if(Serial.available()){
    int iCounter = 0;
    while(Serial.available()){
      instructions[iCounter] = Serial.read();
      iCounter++;
    }
  }
  /*
  for(int i=1;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomins[i]);
    delay(TIME);
  }
  for(int i=1;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomaxs[i]);
    delay(TIME);
  }
  for(int i=0;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomins[i]);
    delay(TIME);
  }
  for(int i=0;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomaxs[i]);
    delay(TIME);
  }*//*
  for(int i=1;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomins[i]);
    delay(TIME);
  }
  for(int i=1;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomaxs[i]);
    delay(TIME);
  }
  for(int i=0;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomins[i]);
    delay(TIME);
  }
  for(int i=0;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomaxs[i]);
    delay(TIME);
  }*/
  /*
  delay(1000);
  Serial.write(c);
  delay(1000);
  Serial.write(1);
  */
  
}

void readCube(){
  for(int i=0;i<8;i+=2){
    pwm.setPWM(servonums[i], 0, servomins[i]);
    delay(TIME);
  }
}

