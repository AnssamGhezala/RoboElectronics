from pyb import Pin,Timer,LED,ADC #import the libraries we need
import pyb

#API/Guide
#https://docs.micropython.org/en/latest/pyboard/pyboard/quickref.html


## You need to setup the touch sensor using ADC here
## You need to setup the external LED using GPIO here


#Setup pins for motor
motorForward  = Pin('X2', Pin.OUT_PP)
motorBackward  = Pin('X3', Pin.OUT_PP)
## Setup PWM pin for the motor on pin X1

#Setup internal LED pins
internalLEDR = LED(1)
internalLEDY = LED(3)
internalLEDG = LED(2)

def turnOnMotor(sensorValue):
  ch.pulse_width_percent(math.fabs(sensorValue / 2)) # control the speed based on the absolute value read from sensor 
  if(sensorValue < -2):
    ## Turn the external LED on
    ## Turn only the internal green LED on
    ## Make motor go backward
  elif(sensorValue > 2):
    ## Turn the external LED on
    ## Turn only the internal red LED on
    ## Make motor go forward
  else:
    ## Turn the external LED on
    ## Turn motors off

while True:
  ## read the tilt value from acclerometer 
  ## turn on and off and motor based on the value read


