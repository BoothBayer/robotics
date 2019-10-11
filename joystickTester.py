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
lsY = 2
lsX = 2
rsY = 2
rsX = 2
lT = 2
rT = 2
roundMe = 4
xB = 2
oB = 2
sB = 2
tB = 2
lSh = 2
rSh = 2
sB = 2
stB = 2
pB = 2
lSB = 2
rSB = 2
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
	if(lsY != round(leftstickY, roundMe)):
		print("leftstickY: {}".format(round(leftstickY, roundMe)))
		lsY= round(leftstickY, roundMe)
	if(lsX != round(leftstickX, roundMe)):
		print("leftstickX: {}".format(round(leftstickX, roundMe)))
		lsX = round(leftstickX, roundMe)
	if(rsY != round(rightstickY, roundMe)):
		print("rightstickY: {}".format(round(rightstickY, roundMe)))
		rsY = round(rightstickY, roundMe)
	if(rsX !=round(rightstickX, roundMe)):
		print("rightstickX: {}".format(round(rightstickX, roundMe)))
		rsX = round(rightstickX, roundMe)
	if(xB != xButton):
		print("xButton {}".format(xButton))
		xB = xButton
	if(oB != oButton):
		print("oButton {}".format(oButton))
		oB = oButton
	if(tB != trButton):
		print("trButton {}".format(trButton))
		tB = trButton
	if(sB != sqButton):
		print("sqButton {}".format(sqButton))
		sB = sqButton
	if(leftShoulder):
		print("leftShoulder {}".format(leftShoulder))
		lSh = leftShoulder
	if(rightShoulder):
		print("rightShoulder {}".format(rightShoulder))
		rSh = rightShoulder
	if(lT != round(leftTrigger, roundMe)):
		print("Ltrigger {}".format(round(leftTrigger, roundMe)))
		lT = round(leftTrigger, roundMe)
	if(rT != round(rightTrigger, roundMe)):
		print("Rtrigger {}".format(round(rightTrigger, roundMe)))
		rT = round(rightTrigger, roundMe)
	if(selectButton):
		print("Select Button {}".format(selectButton))
		sB = selectButton
	if(startButton):
		print("Start Button {}".format(startButton))
		stB = startButton
	if(playButton):
		print("Play Button {}".format(playButton))
		pB = playButton
	if(leftSButton):
		print("Leftstick Button {}".format(leftSButton))
		lSB = leftSButton
	if(rightSButton):
		print("Rightstick Buttone {}".format(rightSButton))
		rSB = rightSButton
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
