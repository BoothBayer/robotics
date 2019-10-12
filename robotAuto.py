# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
from time import sleep
import os
import Adafruit_PCA9685
from pyfiglet import Figlet
ascii = Figlet(font='starwars', width=900)
print(ascii.renderText('Autonomo'))
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
		#Formulas for getting above function: [(max-min)/2]x[(max)-((max-min)/2)]
		#626-157=469/2=234.5 | 626-234.5=391.5
		return Speed

#Because motors are mounted facing different directions from one side of the robot to the other, they run opposite directions when given the same value.
#Because of this problem one set of motors runs inversely to the other and is given an opposite value...
#For forward movement rightSide is positive and leftSide is negative, for turning set both sides to positive.

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
#Another Abstraction for previous two functions
def setAction(action, speed, time): #Action = 1; Move #Action = 0;Turn
	if(action): #1 or 0
		setMove(speed)
		if(time > 0): #If no timer set, just perform action
			sleep(time) #DO ACTION FOR THIS MANY SEONDS
			setMove(0) #Once action completes cease movement
	else:
		setTurn(speed)
		if(time > 0):
			sleep(time)
			setTurn(0)
#------------------------------------------------------------------------------------------------------#
#---------------------------------------Code-Begins-Here-----------------------------------------------#
#------------------------------------------------------------------------------------------------------#
ascii = pyfiglet.figlet_format("Autonomo")
print(ascii)
print("-----AUTONOMO-----")
#setAction(action,speed,time)
print("Forward for 0.5 seconds at 50% Throttle")
setAction(1, 0.5, 0.5)
print("Turn for 1.5 seconds at 50% Throttle")
setAction(0, 0.5, 1.5)
sleep(0.3)
setMove(0)
quit()
