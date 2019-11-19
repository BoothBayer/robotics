import pygame
import datetime
import os
from time import sleep
os.environ["SDL_VIDEODRIVER"] = "dummy"

def clear():
        os.system('clear')

pygame.init()
pygame.joystick.init()

while True:
	for event in pygame.event.get():
		if event.type == pygame.JOYBUTTONDOWN:
			pass
#			print("Button:" + str(event.button) + " pressed")
#		if event.type == pygame.JOYBUTTONUP:
#			print("Button:" + str(event.button) + " released")
#		if event.type == pygame.JOYAXISMOTION:
#			print("Axis:{} {} ".format(event.axis, event.value))

	joystick_count = pygame.joystick.get_count()
	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()

	buttons = joystick.get_numbuttons()
	for i in range(buttons):
		button = joystick.get_button(i)
		print("Button {:>2} value: {}".format(i,button))

	hats = joystick.get_numhats()
	for i in range(hats):
		hat = joystick.get_hat(i)
		print("Hat {} value: {}".format(i, str(hat)))

	axes = joystick.get_numaxes()
	for i in range(axes):
		axes = joystick.get_axis(i)
		print("Axis: {} value: {}".format(i, axes))
	sleep(0.2)
	clear()
pygame.quit()

