// #include <Wire.h>

// // OV7670 pin definitions (modify if needed)
// #define VSYNC_PIN 2
// #define HREF_PIN 3
// #define PCLK_PIN 4
// #define XCLK_PIN 5

// // Data pins (D0-D7 connected to Arduino)
// int dataPins[] = {6, 7, 8, 9, 10, 11, 12, 13};

// // OV7670 Camera Initialization
// void setup() {
//     Serial.begin(115200);
//     delay(2000);
//     Serial.println("Serial begin");

//     Wire.begin();  // Initialize I2C
//     delay(500);
//     Serial.println("Wire begin");

//     Serial.println("I2C Scanner") ;
//     for (byte address = 1; address < 127; address++) {
//         Wire.beginTransmission(address);
//         if (Wire.endTransmission() == 0) {
//             Serial.print("Device found at 0x");
//             Serial.println(address, HEX);
//         }
//     }

//     Serial.println("End of I2C Scanner");

//     pinMode(LED_BUILTIN, OUTPUT);
//     for (int i = 0; i < 5; i++) {  // Blink LED 5 times
//         digitalWrite(LED_BUILTIN, HIGH);
//         delay(500);
//         digitalWrite(LED_BUILTIN, LOW);
//         delay(500);
//     }

//     Serial.println("Setup started...");  // Debug message

//     pinMode(VSYNC_PIN, INPUT);
//     pinMode(HREF_PIN, INPUT);
//     pinMode(PCLK_PIN, INPUT);
//     pinMode(XCLK_PIN, OUTPUT);

//     // Set data pins as input
//     for (int i = 0; i < 8; i++) {
//         pinMode(dataPins[i], INPUT);
//     }

//     // Initialize OV7670
//     Serial.println("Initializing Camera...");
//     if (!initCamera()) {
//         Serial.println("Camera init failed!");
//         while (1); // Stop if camera does not initialize
//     }
//     Serial.println("Camera Ready!");
// }

// // Function to Initialize Camera (Modify If Needed)
// bool initCamera() {
//     Wire.beginTransmission(0x21);  // OV7670 I2C address (check datasheet)
//     Wire.write(0x12);  // Register to reset the camera
//     Wire.write(0x80);  // Reset command
//     if (Wire.endTransmission() != 0) return false;
    
//     delay(100);
    
//     // Set camera to QVGA (320x240) or other settings if needed
//     Wire.beginTransmission(0x21);
//     Wire.write(0x12);
//     Wire.write(0x14);  // Set to QVGA
//     return (Wire.endTransmission() == 0);
// }

// // Capture a Frame
// void captureFrame() {
//     Serial.println("Capturing Frame...");
    
//     while (digitalRead(VSYNC_PIN) == LOW); // Wait for VSYNC high
//     while (digitalRead(VSYNC_PIN) == HIGH); // Wait for VSYNC low

//     // Read each pixel
//     for (int y = 0; y < 120; y++) { // Capture 120 rows (for QVGA)
//         while (digitalRead(HREF_PIN) == LOW);  // Wait for HREF high

//         for (int x = 0; x < 160; x++) { // Read 160 pixels per row
//             while (digitalRead(PCLK_PIN) == LOW); // Wait for PCLK high
//             int pixel = readPixel(); // Read pixel data
//             Serial.print(pixel);
//             Serial.print(" ");
//             while (digitalRead(PCLK_PIN) == HIGH); // Wait for PCLK low
//         }

//         Serial.println(); // New row
//     }

//     Serial.println("Frame Captured!");
// }

// // Read a Pixel from the Camera
// int readPixel() {
//     int pixel = 0;
//     for (int i = 0; i < 8; i++) {
//         pixel |= digitalRead(dataPins[i]) << i; // Read data pins
//     }
//     return pixel;
// }

// void loop() {
//     captureFrame();  // Capture and print pixel data
//     delay(5000); // Wait before capturing next frame
// }
