import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin_list = [16, 20, 21, 26]

GPIO.setup(pin_list, GPIO.OUT)

try:
	
	while True:
		GPIO.output(pin_list, GPIO.HIGH)
		time.sleep(1.0)
		
		GPIO.output(pin_list, GPIO.LOW)
		time.sleep(1.0)

except KeyboardInterrupt:
	pass
	

GPIO.cleanup()
