# made by Kai Aldag on September 30, 2015

# Imports
import RPi.GPIO as GPIO
import sys
import time

# Setup

GPIO.setmode(GPIO.BOARD)

blue_chan = 11
red_chan = 13

GPIO.setup([blue_chan, red_chan], GPIO.OUT)
GPIO.output([blue_chan, red_chan], 0)

push_button_chan = 15

GPIO.setup(push_button_chan, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Application

should_run = True
current = "Blue"

try:
	interval = int(sys.argv[1])
except IndexError:
	interval = 0.5
except ValueError:
	interval = 0.5

def handle_push(chan):
	if (GPIO.input(push_button_chan) == 1):
		global should_run
		should_run = not should_run
		GPIO.output([blue_chan, red_chan], 1)
		time.sleep(1.25)
		GPIO.output([blue_chan, red_chan], 0)

GPIO.add_event_detect(push_button_chan, GPIO.RISING, callback=handle_push)

try:
	while True:
		while should_run:
			if current == "Blue":
				GPIO.output(blue_chan, 1)
				GPIO.output(red_chan, 0)
				current = "Red"
			else:
				GPIO.output(red_chan, 1)
				GPIO.output(blue_chan, 0)
				current = "Blue"
			time.sleep(interval)
except KeyboardInterrupt:
	GPIO.cleanup()

