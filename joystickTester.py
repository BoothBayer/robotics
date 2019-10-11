# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
from time import sleep
import os
import pygame
#import Adafruit_PCA9685
os.environ["SDL_VIDEODRIVER"] = "dummy"
print("Preparing - 5seconds")
sleep(1)
#pygame.init()

# Initialise the PCA9685 using the default address (0x40).
#pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
#pwm.set_pwm_freq(60)
pygame.init()
print("...STARTING...")

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()

def clear():
	os.system('clear')
clear()
lsY = 0
lsX = 0
rsY = 0
rsX = 0
lT = 0
rT = 0
while True:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        pygame.event.get()
        #if event.type == pygame.QUIT:
            #done = True
        if joystick_count != 0:
		#on ps2 X=b0 O=b1 Triangle=b2 Square=b3
		#Lshoulder=b4 Rshoulder=b5
		#LTriggerB=b6 RtriggerB=b7
		#Select=b8 Start=b9
		#PlayStation=b10
		#LeftButton=b11 RightButton=b12
		#DpadUp=b13 DpadDown=b14 DpadLeft=b15 DpadRight=b16
		#leftstickY=a1
		#leftstickX=a0
		#rightstickY=a4
		#rightstickX=a3
		#leftShoulder=a2
		#rightShoulder=a5
		xButton = gamepad.get_button(0)
		oButton = gamepad.get_button(1)
		trButton = gamepad.get_button(2)
		sqButton = gamepad.get_button(3)
		leftShoulder = gamepad.get_button(4)
		rightShoulder = gamepad.get_button(5)
		leftBTrigger = gamepad.get_button(6)
		rightBTrigger = gamepad.get_button(7)
		selectButton = gamepad.get_button(8)
		startButton = gamepad.get_button(9)
		playButton = gamepad.get_button(10)
		leftSButton = gamepad.get_button(11)
		rightSButton = gamepad.get_button(12)
#		dpadUp = gamepad.get_button(13)
#		dpadDown = gamepad.get_button(14)
#		dpadLeft = gamepad.get_button(15)
#		dpadRight = gamepad.get_button(16)
		leftstickY = gamepad.get_axis(1)
		leftstickX = gamepad.get_axis(0)
		rightstickY = gamepad.get_axis(4)
		rightstickX = gamepad.get_axis(3)
		leftTrigger = gamepad.get_axis(2)
		rightTrigger = gamepad.get_axis(5)

        else:
		leftstick = 0
		rightstick = 0
		Lservo = 0
		Rservo = 0
	sleep(0.1)
#	clear()
	if(lsY != round(leftstickY, 4)):
		if(abs(leftstickY) > 0): print("leftstickY: {}".format(round(leftstickY,4)))
		lsY= round(leftstickY, 4)
	if(lsX != round(leftstickX, 4)):
		if(abs(leftstickX) > 0): print("leftstickX: {}".format(round(leftstickX,4)))
		lsX = round(leftstickX, 4)
	if(rsY != round(rightstickY, 4)):
		if(abs(rightstickY) > 0): print("rightstickY: {}".format(round(rightstickY,4)))
		rsY = round(rightstickY, 4)
	if(rsX !=round(rightstickX,4)):
		if(abs(rightstickX) > 0): print("rightstickX: {}".format(round(rightstickX,4)))
		rsX = round(rightstickX,4)
	if(xButton): print("xButton {}".format(xButton))
	if(oButton): print("oButton {}".format(oButton))
	if(trButton): print("trButton {}".format(trButton))
	if(sqButton): print("sqButton {}".format(sqButton))
	if(leftShoulder): print("leftShoulder {}".format(leftShoulder))
	if(rightShoulder): print("rightShoulder {}".format(rightShoulder))
	if(lT != round(leftTrigger,4)):
		if(abs(leftTrigger) > 0): print("Ltrigger {}".format(round(leftTrigger,4)))
		lT = round(leftTrigger,4)
	if(rT != round(rightTrigger,4)):
		if(abs(rightTrigger) > 0): print("Rtrigger {}".format(round(rightTrigger,4)))
		rT = round(rightTrigger,4)
	if(selectButton): print("Back Button {}".format(selectButton))
	if(startButton): print("Start Button {}".format(startButton))
	if(playButton): print("Play Button {}".format(playButton))
	if(leftSButton): print("Leftstick Button {}".format(leftSButton))
	if(rightSButton): print("Rightstick Buttone {}".format(rightSButton))
#		leftstickX = gamepad.get_axis(0)
#		leftstick = gamepad.get_axis(1)
#		rightstickX = gamepad.get_axis(2)
#		rightstick = gamepad.get_axis(3)
#		Abutton = gamepad.get_button(0)
#		Bbutton = gamepad.get_button(1)
#		Xbutton = gamepad.get_button(3)
#		Ybutton = gamepad.get_button(4)
#		Lshoulder = gamepad.get_button(6)
#		Rshoulder = gamepad.get_button(7)
#		Ltrigger = gamepad.get_button(8)
#		Rtrigger = gamepad.get_button(9)
#		Backbutton = gamepad.get_button(10)
#		Startbutton = gamepad.get_button(11)
#		LeftstickButton = gamepad.get_button(13)
#		RightstickButton = gamepad.get_button(14)
#		UpDpad = gamepad.get_button(12)
#		DownDpad = gamepad.get_button(13)
#		LeftDpad = gamepad.get_button(14)
#		RightDpad = gamepad.get_button(15)
