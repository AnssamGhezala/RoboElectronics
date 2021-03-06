import json
import gpiozero
import time
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from flask import Flask, render_template, request, abort
from flask_restful import abort, Api

factory = PiGPIOFactory()

# Define Motor Configuration
# Used for controlling forwards and backwards.
motor_1 = gpiozero.Motor(15, 14,pwm=False,pin_factory=factory)
# Used for controlling direction.
motor_2 = gpiozero.Motor(23, 24,pwm=False, pin_factory=factory)

#Define servo
servoPin = 17 #GPIO
servo = Servo(servoPin, max_pulse_width=1.9/1000,  min_pulse_width=0.4/1000,pin_factory=factory)

speed = 0.5
pwm = gpiozero.PWMOutputDevice(3,initial_value=speed, pin_factory=factory)


# Setup the server.
app = Flask(__name__)
api = Api(app)

speed = 0.5

# Application routing.
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/set_speed', methods=['GET'])
def set_speed():
    speed = float(request.args.get('speed'))
    print(speed)
    if(speed > 1 or speed < 0):
        abort(400)
    else:
        pwm._write(speed)
        return "set"


# API for controlling the robot.
@app.route('/command', methods=['POST'])
def process_command():
    valid_commands = ['forward', 'backward', 'left', 'right', 'stop','shoot']
    data = json.loads(request.data.decode('utf8'))
    command = data.get('command')

    # Abort if POST request is invalid.
    if command is None or command not in valid_commands:
        abort(400)
    else:
        _control_motor(command)
        return "done"
 
def shoot():
    servo.max() #Use a number between 0-2200, this is the pulse width and sets the position of the servo
    time.sleep(0.2) #wait 100ms
    servo.mid()
    return "made the shot"


def _control_motor(command):
    if command == 'forward':
        motor_2.forward()
        motor_1.forward()
    elif command == 'backward':
        motor_2.backward()
        motor_1.backward()
    elif command == 'left':
        motor_1.stop()
        motor_2.forward()
    elif command == 'right':
        motor_1.forward()
        motor_2.stop()
    elif command == 'stop':
        motor_1.stop()
        motor_2.stop()
    elif command == 'shoot':
        shoot()
    else:
        abort(500)






if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
