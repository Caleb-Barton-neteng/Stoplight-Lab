from gpiozero import LED
import time

class StopLight:
    def __init__(self, red_led=LED(17), yellow_led=LED(18), green_led=LED(27)):
        self.red_led = red_led
        self.yellow_led = yellow_led
        self.green_led = green_led
        self.current_light = "off"  # Track active light

    def normal_cycle(self, stop_event):
        self.turn_off_all_lights()
        while not stop_event.is_set():
            self.current_light = "green"
            self.green_light_on(5)
            if stop_event.is_set(): break
            
            self.green_light_off()
            self.current_light = "yellow"
            self.yellow_light_on(5)
            if stop_event.is_set(): break
            
            self.yellow_light_off()
            self.current_light = "red"
            self.red_light_on(5)
			self.red_light_off()
            if stop_event.is_set(): break

        self.turn_off_all_lights()
        self.current_light = "off"

    def race_cycle(self, stop_event):
        while not stop_event.is_set():
            self.turn_off_all_lights()
            if stop_event.is_set(): break
            
            self.current_light = "red"
            self.red_light_on(2)
            if stop_event.is_set(): break
            
            self.red_light_off()
            self.current_light = "yellow"
            self.yellow_light_on(1)
            if stop_event.is_set(): break
            
            self.yellow_light_off()
            self.current_light = "yellow"
            self.yellow_light_on(2)
            if stop_event.is_set(): break
            
            self.yellow_light_off()
            self.current_light = "green"
            self.green_light_on(5)
            if stop_event.is_set(): break

        self.turn_off_all_lights()
        self.current_light = "off"

    def turn_off_all_lights(self):
        self.green_led.off()
        self.yellow_led.off()
        self.red_led.off()
        self.current_light = "off"

    def get_light_status(self):
        return self.current_light
    
    def green_light_off(self):
        self.green_led.off()  # Turn off the LED
        return "GREEN LED is now OFF!"
        
    def green_light_on(self,sec):
        self.green_led.on()  # Turn on the LED
        time.sleep(sec)
        return "GREEN LED is now ON!"
        
    def yellow_light_off(self):
        self.yellow_led.off()  # Turn off the LED
        return "YELLOW LED is now OFF!"
        
    def yellow_light_on(self,sec):
        self.yellow_led.on()  # Turn on the LED
        time.sleep(sec)
        return "YELLOW LED is now ON!"
        
    def red_light_off(self):
        self.red_led.off()  # Turn off the LED
        return "RED LED is now OFF!"

    def red_light_on(self,sec):
        self.red_led.on()  # Turn on the LED
        time.sleep(sec)
        return "RED LED is now ON!"
