import cv2
import numpy as np
from motor코드 import *


def main():
	camera = cv2.VideoCapture(0)
	camera.set(3, 160)
	camera.set(4, 120)
	
	while(camera.isOpened()):
		ret, frame = camera.read() 
		frame = cv2.flip(frame, -1)
		cv2.imshow('normal', frame)
		
		crop_img = frame[60: 120, 0:160]
		
		gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
		
		blur = cv2.GaussianBlur(gray, (5,5), 0)
		
		ret, thresh1 = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY_INV)
		
		mask = cv2.erode(thresh1, None, iterations=2) #이미지를 압축 팽창하여 노이즈 없애기
		mask = cv2.dilate(mask, None, iterations=2)
		cv2.imshow('Mask', mask)
		
		contours, hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE) #미지 윤곽선 검출
		
		if len(contours) >0: #'''출된 윤곽선이 있다면'''
			c = max(contours, key = cv2.contourArea) #'''윤곽선의 최대큰 값을 반환함.'''
			M = cv2.moments(c) #'''윤곽선에서 모멘트 계산'''
			
			cx = int(M['m10'] / M['m00'])#'''x축의 중심을 구한다. '''
			cy = int(M['m01'] / M['m00'])#'''y축의 중심을 구한다.'''
			
			if cx >= 95 and cx <= 125:
				print('Turn Left')
				motor_left(40)
			elif cx >= 39 and cx <=65:
				print('Turn rtight')
				motor_right(40)
			else:
				print('go')
				motor_go(40)
			
			cv2.line(crop_img, (cx, 0), (cx, 720), (255, 0, 0), 1) #'''#x축의 중심을 출력한다.'''
			cv2.line(crop_img, (0, cy), (1280, cy), (255, 0, 0), 1) #'''#y축의 중심을 출력한다.'''
			
			cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 1)
			print(cx)
			'''
			#선이 중심 보다 오른쪽에 있을 때는 39~65
			#선이 중심 보다 왼쪽에 있을 때는 95~125
			'''
		
		
		if cv2.waitKey(1) == ord('q'):
			break
			
	cv2.destoryAllWindows()
	
if __name__ == '__main__':
	main()
	
