## **How It Works**

### **Backend (Flask + GPIO)**

- `app.py` initializes the Flask server and sets up routes for controlling the stoplight.
- `StopLight` class manages the state of the LEDs using GPIO.
- Two cycling modes:
  - **Normal Cycle:** Green -> Yellow -> Red (each lasting 5 seconds)
  - **Race Cycle:** Red -> Yellow (short delay) -> Green
- The `reset` endpoint stops the cycle and turns off all lights.

### **Frontend (HTML + JavaScript + CSS)**

- The web page displays the stoplight with three circles representing red, yellow, and green lights.
- JavaScript polls `/get_light_status` every second to update the UI.
- Buttons trigger API requests to start/stop cycles.

## **State Machine Diagram**

Below is a detailed state machine diagram based on the `StopLight` class logic:

```
             +------------+
             |    OFF     |
             +------------+
                   |
                   v
             +------------+
             |   GREEN    |
             +------------+
                   |
                   v
             +------------+
             |  YELLOW    |
             +------------+
                   |
                   v
             +------------+
             |    RED     |
             +------------+
                   |
                   v
             +------------+
             |    OFF     |
             +------------+
                   |
                   v
             +------------+
             |  RACE RED  |
             +------------+
                   |
                   v
             +------------+
             |  RACE YEL  |
             +------------+
                   |
                   v
             +------------+
             |  RACE GREEN |
             +------------+
                   |
                   v
             +------------+
             |    OFF     |
             +------------+
```

### **State Transitions:**
- **Normal Cycle:** OFF → GREEN → YELLOW → RED → OFF
- **Race Cycle:** OFF → RACE RED → RACE YELLOW → RACE GREEN → OFF
- **Reset can be triggered at any state, leading directly to OFF**

## **Future Improvements**

- Add more advanced animations for the lights.
- Implement user-defined timing settings.
- Create a mobile-friendly UI.

## **Contributing**

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## **License**

This project is licensed under the MIT License.

