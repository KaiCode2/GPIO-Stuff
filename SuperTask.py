# made by Kai Aldag on Decembtre 8, 2015

# Imports
import RPi.GPIO as GPIO
import time

# Setup

GPIO.setmode(GPIO.BOARD)

led_chan = 11

GPIO.setup(led_chan, GPIO.OUT)
GPIO.output(led_chan, 0)

# Application

total_time = 60
interval = 30
half = lambda x: x/2
current_led_status = True

try:
	while True:
            GPIO.output(led_chan, current_led_status)
            current_led_status != current_led_status
            time.sleep(interval)
            interval = half(total_time)
except KeyboardInterrupt:
	GPIO.cleanup()
