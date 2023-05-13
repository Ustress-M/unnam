import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sw1 = 5

GPIO.setup(sw1, GPIO.IN, GPIO.PUD_DOWN)

oldsw = 0
newsw = 0
cnt = 0 
try:
	
	while True:
		newsw = GPIO.input(sw1)
		
		if newsw != oldsw:
			oldsw = newsw
			
			if newsw == 1:
				cnt =cnt+1
				print('button Click', cnt)
			time.sleep(0.1)

except KeyboardInterrupt:
	pass

GPIO.cleanup()


