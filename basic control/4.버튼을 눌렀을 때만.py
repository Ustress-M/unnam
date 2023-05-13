import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sw1 = 5

GPIO.setup(sw1, GPIO.IN, GPIO.PUD_DOWN)

oldsw = 0
newsw = 0
try:
	
	while True:
		newsw = GPIO.input(sw1)
		
		if newsw != oldsw:
			oldsw = newsw
			print('button Click')
			time.sleep(0.2)

except KeyboardInterrupt:
	pass

GPIO.cleanup()


