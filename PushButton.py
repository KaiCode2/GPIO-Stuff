# Made by Kai Aldag

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def handle_push(channel):
	if (GPIO.input(15) == 1):
		print("Push on channel %s" %channel)

GPIO.add_event_detect(15, GPIO.RISING, callback=handle_push)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

