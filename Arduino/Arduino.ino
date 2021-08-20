#define DAC_PIN A0 // Make code a bit more legible

void setup() {
  analogReadResolution(12); // Set analog input resolution to max, 12-bits
  SerialUSB.begin(115200);
  SerialUSB.flush();
}

void loop() {
  // Read A1 (connected to A0), and convert that
  // 12-bit ADC value to a voltage between 0 and 3.3.
  float voltage = analogRead(A1) * 3.3 / 4096.0; //crossing the 3.3 and 4096.8 will show first data
  SerialUSB.println(voltage); // Print the voltage.
}
