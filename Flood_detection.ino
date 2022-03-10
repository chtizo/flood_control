#include <dht.h>
#include<Servo.h>
 //Horizontal Servo

dht DHT;
Servo servoHor;
#define DHT11_PIN 3

int x;
int prevX;

byte sensorInterrupt = 0;  // 0 = digital pin 2
byte sensorPin       = 2;
const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor
// The hall-effect flow sensor outputs approximately 4.5 pulses per second per
// litre/minute of flow.
float calibrationFactor = 4.5;

volatile byte pulseCount;  

float flowRate;
bool count = false;

unsigned long oldTime;

void setup()
{
  
  // Initialize a serial connection for reporting values to the host
  Serial.begin(9600);
   servoHor.attach(9); //Attach Horizontal Servo to Pin 6
  servoHor.write(90);
  // Set up the status LED line as an output
  pinMode(pingPin, OUTPUT);
   pinMode(echoPin, INPUT);
  
  pinMode(sensorPin, INPUT);
  digitalWrite(sensorPin, HIGH);

  pulseCount        = 0;
  flowRate          = 0.0;
  oldTime           = 0;

  // The Hall-effect sensor is connected to pin 2 which uses interrupt 0.
  // Configured to trigger on a FALLING state change (transition from HIGH
  // state to LOW state)
  attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
}

/**
 * Main program loop
 */
void loop()
{
   if(Serial.available() > 0)
   {
    
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      servoHor.write(x);
    }
   }
  if (Serial.available() == 0)
{
   if((millis() - oldTime) > 1000)    // Only process counters once per second
  { 
    // Disable the interrupt while calculating flow rate and sending the value to
    // the host
    detachInterrupt(sensorInterrupt);
        
    // Because this loop may not complete in exactly 1 second intervals we calculate
    // the number of milliseconds that have passed since the last execution and use
    // that to scale the output. We also apply the calibrationFactor to scale the output
    // based on the number of pulses per second per units of measure (litres/minute in
    // this case) coming from the sensor.
    flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;
    
    // Note the time this processing pass was executed. Note that because we've
    // disabled interrupts the millis() function won't actually be incrementing right
    // at this point, but it will still return the value it was set to just before
    // interrupts went away.
    oldTime = millis();
    
    // Divide the flow rate in litres/minute by 60 to determine how many litres have
    // passed through the sensor in this 1 second interval, then multiply by 1000 to
    // convert to millilitres.
    

    int chk = DHT.read11(DHT11_PIN);

    
    // Print the flow rate for this second in litres / minute
    Serial.print("F");
    Serial.print(int(flowRate));  // Print the integer part of the variable
    Serial.print("|");
 

    // Reset the pulse counter so we can start incrementing again
    pulseCount = 0;
    
    // Enable the interrupt again now that we've finished sending output
    attachInterrupt(sensorInterrupt, pulseCounter, FALLING);

    
    
  }
    long duration = distance_calculate(); 
   //Serial.println(duration);
    long cm = microsecondsToCentimeters(duration);
    
    
    Serial.print("W");
    Serial.print(cm);
    Serial.print("|");
    Serial.print("T");
    Serial.print(DHT.temperature);
    Serial.print("|");
    Serial.print("H");
    Serial.print(DHT.humidity);
    Serial.print("#");
    
    Serial.print("\n");
    delay(1000);
}
}



/*
Insterrupt Service Routine
 */
void pulseCounter()
{
  // Increment the pulse counter
  pulseCount++;
}

long distance_calculate() {
long duration;
   
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   
   duration = pulseIn(echoPin, HIGH);
   return duration;
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

void Pos()
{
  if(prevX != x )
  {
    //tune this range to generate map
    int servoX = map(x, 0, 640, 0, 179); 
    servoX = min(servoX, 179);
    servoX = max(servoX, 0);
    servoHor.write(servoX);
   }
}
