# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
from time import sleep
import os
import pygame
import Adafruit_PCA9685
os.environ["SDL_VIDEODRIVER"] = "dummy"
print("Preparing - 5seconds")
sleep(1)
#pygame.init()

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
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

while True:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        pygame.event.get()
        #if event.type == pygame.QUIT:
            #done = True
        if joystick_count != 0:
		leftstickX = gamepad.get_axis(0)
		leftstick = gamepad.get_axis(1)
		rightstickX = gamepad.get_axis(2)
		rightstick = gamepad.get_axis(3)
		Abutton = gamepad.get_button(0)
		Bbutton = gamepad.get_button(1)
		Xbutton = gamepad.get_button(2)
		Ybutton = gamepad.get_button(3)
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
        else:
		leftstick = 0
		rightstick = 0
		Lservo = 0
		Rservo = 0

	#set pins here
	frontLeft = 3
	backLeft = 2
	frontRight = 6
	backRight = 11

	#Prevents thejoystick from "floating" and makes sure values do not exceed [-1,1]
        def JoyStick(y):
            if abs(y) < 0.05:
                return 0
            elif y < -1:
                return -1
            elif y > 1:
                return 1
            else:
                return y

	#sets the throttle on the domain of [-1,1] and puts it into a pwm value
	def setThrottle(x):
		if(x > 1):
			return 1
		elif(x < -1):
			return -1
		else:
			Speed = (222.5 * x + 377.5)
			return Speed

	#Function for handling movement
	def setMove(x):
		rightThrottle = setThrottle(x * -1)
		leftThrottle = setThrottle(x) #MIN=155 #MAX=600 #setThrottle(x * -1)
		pwm.set_pwm(frontRight, 0, int(rightThrottle))
		pwm.set_pwm(backRight, 0, int(rightThrottle))
		pwm.set_pwm(frontLeft, 0, int(leftThrottle))
		pwm.set_pwm(backLeft, 0, int(leftThrottle))

	def setStrafe(x):
		rightThrottle = setThrottle(x * -1)
		leftThrottle = setThrottle(x) #MIN=155 #MAX=600 #setThrottle(x * -1)
		pwm.set_pwm(frontRight, 0, int(rightThrottle))
		pwm.set_pwm(backRight, 0, int(leftThrottle))
		pwm.set_pwm(frontLeft, 0, int(rightThrottle))
		pwm.set_pwm(backLeft, 0, int(leftThrottle))
	#Function for handling turning
	def setTurn(x):
		allThrottle = setThrottle(x * -1)
		pwm.set_pwm(frontRight, 0, int(allThrottle))
		pwm.set_pwm(backRight, 0, int(allThrottle))
		pwm.set_pwm(frontLeft, 0, int(allThrottle))
		pwm.set_pwm(backLeft, 0, int(allThrottle))

	#Function for handling arm
	def setArm(x):
		throttle = setThrottle(x)
		pwm.set_pwm(7, 0, int(throttle))

	#CONTROL
	if(Abutton): #DOWN
		setArm(0.2)
	elif(Bbutton): #UP
		setArm(-0.3)
	else:
		setArm(-0.05)

        if((JoyStick(leftstickX) > 0.2) or (JoyStick(leftstickX) < -0.2)):
		setTurn(JoyStick(leftstickX))
        elif((JoyStick(rightstick) > 0.2) or (JoyStick(rightstick) < -0.2)):
		setStrafe(JoyStick(rightstick))
	else:
		setMove(JoyStick(leftstick))
