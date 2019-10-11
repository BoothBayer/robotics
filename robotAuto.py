# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
from time import sleep
import os
import Adafruit_PCA9685
print("AUTONOMOUS MODE LOADING...")
sleep(1)
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#Connections should be marked here, number next to variable corresponds to socket plugged into. REMEMBER: Green is Ground(G)
frontLeft = 4
backleft = 8
frontRight = 0
backRight = 15

#The throttle function allows a value from -1 to 1 to be input and translated into the required pwm value
def setThrottle(x):
	if(x > 1):
		return 1
	elif(x < -1):
		return -1
	else:
		Speed = (234.5 * x + 391.5) #max of 626hz and min of 157hz
		return Speed

#Simplified function for movement, no longer requiers repeating commands
def setMove(x):
	print("STATUS: Moving at",x)
	rightThrottle = setThrottle(x)
	leftThrottle = setThrottle(x * -1)
	pwm.set_pwm(frontRight, 0, rightThrottle)
	pwm.set_pwm(backRight, 0, rightThrottle)
	pwm.set_pwm(frontLeft, 0, leftThrottle)
	pwm.set_pwm(backLeft, 0, leftThrottle)
def setTurn(x):
	print("STATUS: Turning at {}",x)
	allThrottle = setThrottle(x)
	pwm.set_pwm(frontRight, 0, allThrottle)
	pwm.set_pwm(backRight, 0, allThrottle)
	pwm.set_pwm(frontLeft, 0, allThrottle)
	pwm.set_pwm(backLeft, 0, allThrottle)


#Because motors are mounted facing different directions from one side of the robot to the other, they run opposite directions when given the same value.
#Because of this problem one set of motors runs inversely to the other and is given an opposite value...
#For forward movement rightSide is positive and leftSide is negative, for turning set both sides to positive.

print("-----AUTONOMO-----")

print("Forward for 0.5 seconds at 50% Throttle")
setMove(0.5)
sleep(0.5)
print("STOP")
setMove(0)
sleep(0.2)
print("Turn for 1.5 seconds at 50% Throttle")
setTurn(0.5)
sleep(1.5)
print("STOP")
setMove(0)
sleep(0.3)
quit()


#TURNING MOVEMENT
#LmotorR = setThrottle(JoyStick(leftstickX) * 1)
#LmotorL = setThrottle(JoyStick(leftstickX) * 1)
#pwm.set_pwm(frontRight, 0, int(LmotorR)) #front right
#pwm.set_pwm(backRight, 0, int(LmotorR)) #back right
#pwm.set_pwm(frontLeft, 0, int(LmotorL))  #front left
#pwm.set_pwm(backLeft, 0, int(LmotorL))  #back left
#FORWARD BACKWARD MOVEMENT
#LmotorR = setThrottle(JoyStick(leftstick)) #(225 * JoyStick(leftstick) + 376)
#LmotorL = setThrottle(JoyStick((leftstick) * -1)) #(-225 * JoyStick(leftstick) + 376)
#pwm.set_pwm(frontRight, 0, int(LmotorR)) #front right
#pwm.set_pwm(backRight, 0, int(LmotorR)) #back right
#pwm.set_pwm(frontLeft, 0, int(LmotorL))  #front left
#pwm.set_pwm(backLeft, 0, int(LmotorL))  #back left
#quit()
