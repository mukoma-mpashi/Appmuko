
#include <SPI.h>
#include <AIR430BoostETSI.h>

// Define local and remote addresses
#define ADDRESS_LOCAL 0x02
#define ADDRESS_REMOTE 0x01



struct SensorData {
  float temperature;
  float moisture;
};


struct ControlCommand {
  int cmd; // Command identifier
};

// Commands
#define CMD_ON 1
#define CMD_OFF 0

// Global data
struct SensorData sensorData;
struct SensorData txSensorData;
struct ControlCommand rxControl;

void setup() {
  Radio.begin(ADDRESS_LOCAL, CHANNEL_1, POWER_MAX);
  txSensorData.temperature = 0.0; // Initialize to 0
  txSensorData.moisture = 0.0;    // Initialize to 0

  
  Serial.begin(9600);
  pinMode(RED_LED, OUTPUT); 
  digitalWrite(RED_LED, LOW); 
}

void loop() {

  if (!Radio.busy()) {
//place holders  for when i actually connect the sensors  
// for now  sending to the hub which i manually enter     
    txSensorData.temperature = 25.0; 
    txSensorData.moisture = 60.0;     

  
    Radio.transmit(ADDRESS_REMOTE, (unsigned char*)&txSensorData, sizeof(txSensorData));
  }

  
  if (Radio.receiverOn((unsigned char*)&rxControl, sizeof(rxControl), 1000) > 0) {
    
    if (rxControl.cmd == CMD_ON) {
      turnPumpOn();
    } else if (rxControl.cmd == CMD_OFF) {
      turnPumpOff();
    }
  }

  
  delay(1000);
}

void turnPumpOn() {
  Serial.println("Turning pump ON");

  digitalWrite(RED_LED, HIGH); 
}

void turnPumpOff() {
  
  Serial.println("Turning pump OFF");
  digitalWrite(RED_LED, LOW); 
}
