import RPi.GPIO as GPIO
import time
 
BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
 
p = GPIO.PWM(buzzer, 1.0) # 초기 주파수를 1Hz로 설정
p.start(90.0) # 듀티비를 90%로 높여 설정함(음 구분이 더 잘되고 조금 더 부드럽게 들림)

scale = [ 262 , 294  , 330 ,  349 , 392 ,  440 ,   494 ]
twinkle = [ 1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, 
            5, 5, 4, 4, 3, 3, 2, 5, 5, 4, 4, 3, 3, 2, 
            1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1 ]
try :
    for i in range(0, 42):
        p.ChangeFrequency(scale[twinkle[i]])
        if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
            time.sleep(1.0)   # 2분음표 부분을 모두 1초로 출력
        else :
            time.sleep(0.5)   # 기타 4분음표는 모두 0.5초로 출력함 
    p.stop()
 
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()