from flask import Flask
from gpiozero import LED
app = Flask(__name__)


led = LED(3) # pins are defined by GPIO number

#Define the first resource, you can 'consume' it by typing "curl YOUR_PI_IP:5000/ledOn"


#Define the second resource, you can 'consume' it by typing "curl YOUR_PI_IP:5000/ledOff"


if __name__ == '__main__':
    #Use 0.0.0.0 so that the serve is accessible from outside the Pi
    app.run(host='0.0.0.0', debug=True, port=5000)
