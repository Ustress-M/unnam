import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sw_list = (5,6,13,19)

GPIO.setup(sw_list, GPIO.IN, GPIO.PUD_DOWN)

oldsw = [0, 0, 0, 0]
newsw = [0, 0, 0, 0]

cnt = [0,0,0,0]
try:
	
	while True:
		
		for x in range(0, 4):
			newsw[x] = GPIO.input(sw_list[x])
			if newsw[x] != oldsw[x]:
				oldsw[x] = newsw[x]
							
				if newsw[x] == 1:
					cnt[x] = cnt[x] +1
					print(f'버튼 {x+1}번이 눌린 횟수는 {cnt[x]}번 입니다.. ')
					time.sleep(0.2)

except KeyboardInterrupt:
	pass

GPIO.cleanup()


