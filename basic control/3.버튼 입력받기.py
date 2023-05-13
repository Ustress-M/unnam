import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sw1 = 5

GPIO.setup(sw1, GPIO.IN, GPIO.PUD_DOWN)

try:
	
	while True:
		sw1Value= GPIO.input(sw1)
		print(sw1Value)
		
		time.sleep(1.0)

except KeyboardInterrupt:
	pass
	

GPIO.cleanup()


'''
문제점 -> 버튼을 눌르고 있으면 계속 인식함. 작업 계속되버림.
버튼을 눌렀을 때만 값이 표시되게.

'''
