import pyb

def main():
	led1 = pyb.LED(1)
	while True:
		led1.toggle()
		pyb.delay(1000)

if __name__ == "__main__":
	main()