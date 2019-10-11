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
		Xbutton = gamepad.get_button(3)
		Ybutton = gamepad.get_button(4)
		Lshoulder = gamepad.get_button(6)
		Rshoulder = gamepad.get_button(7)
		Ltrigger = gamepad.get_button(8)
		Rtrigger = gamepad.get_button(9)
		Backbutton = gamepad.get_button(10)
		Startbutton = gamepad.get_button(11)
		LeftstickButton = gamepad.get_button(13)
		RightstickButton = gamepad.get_button(14)
		UpDpad = gamepad.get_button(12)
		DownDpad = gamepad.get_button(13)
		LeftDpad = gamepad.get_button(14)
		RightDpad = gamepad.get_button(15)
        else:
		leftstick = 0
		rightstick = 0
		Lservo = 0
		Rservo = 0

	#set pins here
	frontLeft = 4
	backleft = 8
	frontRight = 0
	backRight = 15

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
			Speed = (234.5 * x + 391.5)
			return Speed

	#Function for handling movement
	def setMove(x):
		rightThrottle = setThrottle(x)
		leftThrottle = setThrottle(x * -1)
		pwm.set_pwm(frontRight, 0, rightThrottle)
		pwm.set_pwm(backRight, 0, rightThrottle)
		pwm.set_pwm(frontLeft, 0, leftThrottle)
		pwm.set_pwm(backLeft, 0, leftThrottle)

	#Function for handling turning
	def setTurn(x):
		allThrottle = setThrottle(x)
		pwm.set_pwm(frontRight, 0, allThrottle)
		pwm.set_pwm(backRight, 0, allThrottle)
		pwm.set_pwm(frontLeft, 0, allThrottle)
		pwm.set_pwm(backLeft, 0, allThrottle)

	#CONTROL
        if((JoyStick(leftstickX) > 0.2) or (JoyStick(leftstickX) < -0.2)):
		setTurn(JoyStick(leftstickX))
        else:
		setMove(JoyStick(leftstick))

#        def Throttle(x):
 #           if(x > 1):
  #              return 1
   #         elif(x < -1):
    #            return -1
     #       else:
      #          Speed = (234.5 * x + 391.5)
       #         return Speed

#        #Green is GROUND and Yellow is SIGNAl
#        LmotorR = (225 * Throttle(JoyStick(leftstick)) + 376)
#        LmotorL = (-225 * Throttle(JoyStick(leftstick) + 376))
#        if((JoyStick(leftstickX) > 0.2) or (JoyStick(leftstickX) < -0.2)):
#         #TURNING MOVEMENT
#	    LmotorR = Throttle(JoyStick(leftstickX) * 1) #(225 * JoyStick(leftstickX) + 376)
#            LmotorL = Throttle(JoyStick(leftstickX) * 1) #(225 * JoyStick(leftstickX) + 376)
#            pwm.set_pwm(0, 0, int(LmotorR)) #front right
#            pwm.set_pwm(15, 0, int(LmotorR)) #back right
#            pwm.set_pwm(4, 0, int(LmotorL))  #front left
#            pwm.set_pwm(8, 0, int(LmotorL))  #back left
#        else:
#        #FORWARD BACKWARD MOVEMENT
#	    LmotorR = Throttle(JoyStick(leftstick)) #(225 * JoyStick(leftstick) + 376)
#            LmotorL = Throttle(JoyStick((leftstick) * -1)) #(-225 * JoyStick(leftstick) + 376)
#            pwm.set_pwm(0, 0, int(LmotorR)) #front right
#            pwm.set_pwm(15, 0, int(LmotorR)) #back right
#            pwm.set_pwm(4, 0, int(LmotorL))  #front left
#            pwm.set_pwm(8, 0, int(LmotorL))  #back left
