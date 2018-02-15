try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import time

GPIO.setmode(GPIO.BCM) #Using the GPIO naming convention

ledPin = 20
GPIO.setup(ledPin, GPIO.OUT) #GPIO 2, Pin 03

def main():
    ledState = False
    try:
        while True:
            if (not ledState):
                GPIO.output(ledPin, GPIO.HIGH)
                ledState = True
            else:
                GPIO.output(ledPin,GPIO.LOW)
                ledState = False
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
if __name__ == "__main__":
    main()
