from flask import Flask
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time
app = Flask(__name__)

#Orange wire from the servo, the RED and BLACK wire are connected to 5V and GND
#GPIO library, all pins are defined by GPIO number
factory = PiGPIOFactory()
servoPin = 17
servo = Servo(servoPin, max_pulse_width=1.9/1000,  min_pulse_width=0.4/1000,pin_factory=factory)
#Define the first url, you can 'consume' it by typing "curl YOUR_PI_IP:5000/shoot"
@app.route('/shoot')
def shoot():
    servo.max() #Use a number between 0-2200, this is the pulse width and sets the position of the servo
    time.sleep(0.2) #wait 100ms
    servo.mid()
    return "made the shot"
if __name__ == '__main__':
    #Use 0.0.0.0 so that the serve is accessible from outside the Pi
    app.run(host='0.0.0.0', debug=True, port=5000)
