import time
import threading
from flask import Flask, render_template, jsonify
from stoplight import StopLight

app = Flask(__name__)
stoplight = StopLight()

# Use a threading Event to control stop/start
stop_event = threading.Event()

@app.route('/cycle_green_to_red', methods=['GET'])
def cycle_green_to_red():
    stop_event.clear()  # Allow execution
    threading.Thread(target=stoplight.normal_cycle, args=(stop_event,)).start()
    return render_template('index.html')

@app.route('/race_cycle', methods=['GET'])
def race_cycle():
    stop_event.clear()  # Allow execution
    threading.Thread(target=stoplight.race_cycle, args=(stop_event,)).start()
    return render_template('index.html')

@app.route('/reset', methods=['GET'])
def reset():
    stop_event.set()  # Stop execution
    stoplight.turn_off_all_lights()
    return render_template('index.html')
	
@app.route('/get_light_status', methods=['GET'])
def get_light_status():
    return jsonify({"light": stoplight.get_light_status()})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        pass
