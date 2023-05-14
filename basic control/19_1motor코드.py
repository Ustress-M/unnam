import RPi.GPIO as GPIO

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24


def motor_go(speed):
	L_motor.ChangeDutyCycle(speed)
	GPIO.output(AIN1, False)
	GPIO.output(AIN2, True)
	R_motor.ChangeDutyCycle(speed)
	GPIO.output(BIN1, False)
	GPIO.output(BIN2, True)
	
def motor_right(speed):
	L_motor.ChangeDutyCycle(speed)
	GPIO.output(AIN1, False)
	GPIO.output(AIN2, True)
	R_motor.ChangeDutyCycle(speed)
	GPIO.output(BIN1, True)
	GPIO.output(BIN2, False)

def motor_left(speed):
	L_motor.ChangeDutyCycle(speed)
	GPIO.output(AIN1, True)
	GPIO.output(AIN2, False)
	R_motor.ChangeDutyCycle(speed)
	GPIO.output(BIN1, False)
	GPIO.output(BIN2, True)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup([PWMA, AIN1, AIN2], GPIO.OUT)
GPIO.setup([PWMB, BIN1, BIN2], GPIO.OUT)

L_motor=GPIO.PWM(PWMA, 100)
L_motor.start(0)

R_motor=GPIO.PWM(PWMB, 100)
R_motor.start(0)
