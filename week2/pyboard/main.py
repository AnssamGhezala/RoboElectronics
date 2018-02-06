from pyb import Pin,LED,ADC #import the libraries we need
import pyb

#API/Guide
#https://docs.micropython.org/en/latest/pyboard/pyboard/quickref.html


## You need to setup the touch sensor using ADC here
## You need to setup the external LED using GPIO here

#Setup pins for motor
motorForward  = Pin('X2', Pin.OUT_PP)
motorBackward  = Pin('X3', Pin.OUT_PP)

#Setup internal LED pins
internalLEDR = LED(1)
internalLEDY = LED(3)
internalLEDG = LED(2)

def turnOnLED(sensorValue):
  if(sensorValue < 3000):
    ## Turn the external LED off
    ## Turn only the internal green LED on
    ## Turn off all motors
  else:
    ## Turn the external LED on
    ## Turn only the internal red LED on
    ## Turn off all motors


while True:
  ## read the touchsensor value, should returns a value for 0 - 4095 
  ## turn on or turn off the led and motor based on the value read


