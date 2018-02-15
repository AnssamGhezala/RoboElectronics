import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motorForward = 2 #PIN3
motorBackward = 3 #PIN5
pwm = 4 #pin7

motorList = [motorForward,motorBackward]
GPIO.setup(motorList, GPIO.OUT)
GPIO.setup(pwm, GPIO.OUT)

dutycycle = 0
p = GPIO.PWM(pwm,50) #Setup the PWM to have 50 HZ
p.start(dutycycle) #start the pwm at 0% duty cycle

try:
    while True:
        GPIO.output(motorList, (GPIO.HIGH,GPIO.LOW))
        dutycycle = (dutycycle + 10) % 100
        p.ChangeDutyCycle(dutycycle)
        time.sleep(2)
except KeyboardInterrupt:
    print('interrupted!')
    p.stop()
    GPIO.output(motorList, (GPIO.LOW,GPIO.LOW))
    GPIO.cleanup()
