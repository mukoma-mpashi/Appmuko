#include <SPI.h>
#include <AIR430BoostETSI.h>
#include <Energia.h>
#include <WiFi.h>

char ssid[] = "HUAWEI-B315-5391";
char password[] = "790L48T2938";
char serverAddress[] = "192.168.8.100";
int port = 5000;
#define HUB_ADDRESS 0x01 // Hub's address

struct SensorData {
  float temperature;
  float moisture;
};

struct SensorData receivedSensorData;

void setup() {
  Radio.begin(HUB_ADDRESS, CHANNEL_1, POWER_MAX);
  receivedSensorData.temperature = 0.0;
  receivedSensorData.moisture = 0.0;
  Serial.begin(9600);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  if (Radio.receiverOn((unsigned char*)&receivedSensorData, sizeof(receivedSensorData), 1000) > 0) {
    // Process the received sensor data
    Serial.print("Received Sensor Data - Temperature: ");
    Serial.print(receivedSensorData.temperature);
    Serial.print("°C, Moisture: ");
    Serial.print(receivedSensorData.moisture);
    Serial.println("%");

    // Convert the received sensor data to a single payload
    String data = String(receivedSensorData.temperature, 2) + "," + String(receivedSensorData.moisture, 2) + "%";
    
    
    WiFiClient client;

    if (client.connect(serverAddress, port)) {
      Serial.println("Connected to Flask server");

      // Send the  data to /update_data route
      client.println("POST /update_data HTTP/1.1");
      client.println("Host: " + String(serverAddress));
      client.println("Content-Type: text/plain");
      client.print("Content-Length: ");
      client.println(data.length());
      client.println();
      client.println(data);
    } else {
      Serial.println("Connection failed");
    }
  }

  // Check for commands to control the pump
  WiFiClient client;
  if (client.connect(serverAddress, port)) {
    Serial.println("Connected to Flask server");

    // Send a GET request to /control_pump route
    client.println("GET /control_pump HTTP/1.1");
    client.println("Host: " + String(serverAddress));
    client.println();
  }

  delay(15000); 
}
