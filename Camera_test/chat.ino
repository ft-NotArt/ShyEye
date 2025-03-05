#include <Wire.h>

void setup() {
  Serial.begin(115200);
  delay(2000);  // Wait for the serial monitor to open
  Serial.println("I2C Scanner");

  Wire.begin();  // Initialize I2C communication
  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    if (Wire.endTransmission() == 0) {
      // If the device responds, it means it’s present on the bus
      Serial.print("Device found at address 0x");
      Serial.println(address, HEX);
    }
  }
  Serial.println("End of I2C Scanner");
}

void loop() {
  // Empty loop
}
