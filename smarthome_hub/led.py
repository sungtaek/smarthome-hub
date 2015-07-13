import logging
import json
import RPi.GPIO as GPIO
from agent import Agent

logger = logging.getLogger(__name__)

class Led(Agent):
    GPIO_NUM_LED = 12

    def __init__(self, name):
        super(Led, self).__init__(name)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GPIO_NUM_LED, GPIO.OUT)

    def do_action(self, action):
        if action['command'] == 'on':
            logger.info('led on!')
            GPIO.output(self.GPIO_NUM_LED, True)
            return 200, 'Success'
        if action['command'] == 'off':
            logger.info('led off!')
            GPIO.output(self.GPIO_NUM_LED, False)
            return 200, 'Success'
        return 400, 'Unknown command'

