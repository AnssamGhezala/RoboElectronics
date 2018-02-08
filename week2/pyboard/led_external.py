# import pyb
# from pyb import Pin

led = Pin('X5', Pin.OUT_PP)
ledState = false
def main():
	while True:
	 	if( not ledState):
	 		led.high()
	 		ledState = true
	 	else:
	 		led.low()
	 		ledState = false

if __name__ == "__main__":
	main()