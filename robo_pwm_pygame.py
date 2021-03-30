# import curses and GPIO
import pygame
import RPi.GPIO as GPIO
import os #added so we can shut down OK
import time #import time module


from datetime import datetime

#Open a Pygame window to allow it to detect keyboard presses
screen = pygame.display.set_mode([240, 160])

#set GPIO numbering and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)

#setup PWM control
GPIO.setup(12,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
speedleft = GPIO.PWM(12,100)
speedright = GPIO.PWM(32,100)
speedleft.start(100)
speedright.start(100)

try:
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
				elif event.key == pygame.K_s:
					os.system ('sudo shutdown now') # shutdown right now!
				elif event.key == pygame.K_RIGHT:
					GPIO.output(7,True)
					GPIO.output(11,False)
					GPIO.output(13,False)
					GPIO.output(15,True)
				elif event.key == pygame.K_LEFT:
					GPIO.output(7,False)
					GPIO.output(11,True)
					GPIO.output(13,True)
					GPIO.output(15,False)
				elif event.key == pygame.K_UP:
					GPIO.output(7,False)
					GPIO.output(11,True)
					GPIO.output(13,False)
					GPIO.output(15,True)
				elif event.key == pygame.K_KP9:
					speedright.ChangeDutyCycle(33)
					speedleft.ChangeDutyCycle(100)
					GPIO.output(7,False)
					GPIO.output(11,True)
					GPIO.output(13,False)
					GPIO.output(15,True)
					speedright.ChangeDutyCycle(100)
				elif event.key == pygame.K_KP7:
					speedright.ChangeDutyCycle(100)
					speedleft.ChangeDutyCycle(33)
					GPIO.output(7,True)
					GPIO.output(11,True)
					GPIO.output(13,True)
					GPIO.output(15,False)
				elif event.key == pygame.K_DOWN:
					GPIO.output(7,True)
					GPIO.output(11,False)
					GPIO.output(13,True)
					GPIO.output(15,False)
				elif event.key == pygame.K_1:
					speedleft.ChangeDutyCycle(33)
					speedright.ChangeDutyCycle(33)
				elif event.key == pygame.K_2:
					speedleft.ChangeDutyCycle(66)
					speedright.ChangeDutyCycle(66)
				elif event.key == pygame.K_3:
					speedleft.ChangeDutyCycle(100)
					speedright.ChangeDutyCycle(100)
			elif event.type == pygame.KEYUP:
				GPIO.output(7,False)
				GPIO.output(11,False)
				GPIO.output(13,False)
				GPIO.output(15,False)
			             
finally:
    #GPIO cleanup
    GPIO.cleanup()



