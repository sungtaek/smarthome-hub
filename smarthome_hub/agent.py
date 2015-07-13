import logging
import json

class Agent(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def do_action(self, action):
        ''' override this function '''

