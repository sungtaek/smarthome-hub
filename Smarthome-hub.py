#!/usr/bin/env python

import sys
from socketIO_client import SocketIO, LoggingNamespace
import RPi.GPIO as GPIO
import logging
import json

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class HubNamespace(LoggingNamespace):
    def initialize(self):
        logger.info('smarthub started...')

    def on_connect(self):
        super(HubNamespace, self).on_connect()

        account = {}
        account['home'] = 'sungtaek'
        account['agent'] = 'led'

        self.emit('join', account)

    def on_action(self, *args):
        logger.info('on_action!')
        action = args[0]
        logger.info(action)

        if action['target'] == 'led' and action['command'] == 'on':
            led_on()
        elif action['target'] == 'led' and action['command'] == 'off':
            led_off()
        else:
            logger.info('uknown action')

        result = {}
        result['source'] = action['source']
        result['target'] = action['target']
        result['code'] = 200
        result['message'] = 'Success'
        self.emit('result', result)

    def on_join(self, *args):
        logger.info('on_action!')
        account = args[0]
        logger.info(account)


def start_server(host, port):
    logger.info('connect to %s:%d' % (host, port))
    sock = SocketIO(host, port, HubNamespace, proxies={'http':'http://10.251.33.42:8080'})
    sock.wait()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

def led_on():
    logger.info('led on!')
    GPIO.output(12, True)

def led_off():
    logger.info('led off!')
    GPIO.output(12, False)

host = str(sys.argv[1])
port = int(sys.argv[2])
start_server(host, port) 
