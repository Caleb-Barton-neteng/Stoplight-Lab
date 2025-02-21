# Troubleshooting Guide for Stoplight Control Web App

This guide provides troubleshooting tips for issues you might encounter while setting up and using the **Stoplight Control Web App**, which controls LEDs on a Raspberry Pi breadboard.

---

## 1. **Troubleshooting the Circuit Wiring**

### **Common Issues with Wiring the Circuit**
- **LED Not Lighting Up**:
  - **Check Connections**: Ensure each LED's long leg (anode) is connected to the correct GPIO pin, and the short leg (cathode) is connected to a ground (GND) pin.
  - **Verify Resistor Placement**: Ensure you have placed a current-limiting resistor (e.g., 220Ω) in series with each LED to avoid damaging the components.
  - **Wrong GPIO Pin**: Ensure the GPIO pins you are using in the code match the pins to which the LEDs are physically connected. The default pins in this setup are GPIO 17, GPIO 18, and GPIO 27. If looking at the physical pin, the numbers are from the top (SD Card) side of the PI from left to right 1 odd numbers on the left, even on the right. In this case the pin numbers are 11, 12 and 13 as shown in the README.md. 

---

## 2. **Troubleshooting the Web Application**

### **App Not Starting**
- **Ensure Flask is Installed**: The Flask web framework is required for the app to run. The commands for this can be found in the README.md file. 
- **Ensure gpiozero is Installed**: This is how the program interactes with the GPIO pins.
