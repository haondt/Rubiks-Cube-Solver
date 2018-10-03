
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
int servonums[8] = {4, 5, 0, 1, 8, 9, 14, 15}; // uses indexes from diagram
int servomins[8] = {330, 335, 240, 350, 250, 350, 260, 365}; // uses indexes from diagram
int servomaxs[8] = {570, 570, 480, 580, 470, 585, 490, 605}; //uses indexes from diagram
// engage = min, disengage = max
// vertical (from front to back) = max, horizontal (side to side) = min
void setup() {
  Serial.begin(9600);

  pwm.begin();
  pwm.setPWMFreq(60);

  yield();
  Serial.println("<Servo num 0-8>,<Pulse length 0-4096>");
}

void loop() {
  if(Serial.available()){
    char instructions[60];
    int index = 0;
    while(Serial.available()){
      instructions[index] = Serial.read();
      index++;
      delay(10);
    }
    instructions[index] = '\0';
    
    char servostr[10];
    char posstr[10];
    int servo = 0;
    int pos = 0;
    int flip = 0;
    int flippos = 0;
    for(int i=0;i<=index;i++){
      if(!flip){
        servostr[i] = instructions[i];
        if(instructions[i] == ','){
          servostr[i] = '\0';
          flip = 1;
          flippos = i+1;
        }
      }
      else{
        posstr[i-flippos] = instructions[i];
      }
    }
    servo = atoi(servostr);
    pos = atoi(posstr);
    Serial.println("Writing Servo " + String(servo) + " to position " + String(pos) + "...");
    pwm.setPWM(servo, 0, pos);
     /*
    int servo = Serial.parseInt();
    Serial.println("Servo: " + String(servo));
    while(!Serial.available());
    int pos = Serial.parseInt();
    Serial.println("Moving Servo " + String(servo) + " To position " + String(pos));
    */
  }
}
