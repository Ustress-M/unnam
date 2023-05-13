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
������ -> ��ư�� ������ ������ ��� �ν���. �۾� ��ӵǹ���.
��ư�� ������ ���� ���� ǥ�õǰ�.

'''
