# Made by Kai Aldag on September 30, 2015

# Imports
import RPi.GPIO as GPIO
import time

# Setup

GPIO.setmode(GPIO.BOARD)

out_chan_list = 11

GPIO.setup(out_chan_list, GPIO.OUT)
GPIO.output(out_chan_list, 0)

in_chan_list = 20

#GPIO.setup(in_chan_list, GPIO.IN)
#GPIO.input(in_chan_list, 1)

# Application

should_run = True
light_on = True

while should_run:
	#if GPIO.input(20):
	#	print("Channel 20 is on!")
	#else:
	#	print("Channel 20 is off :( ")
	if light_on:
		GPIO.output(out_chan_list, light_on)
		light_on = False
	else:
		GPIO.output(out_chan_list, light_on)
		light_on = True
	time.sleep(1)

GPIO.cleanup()

