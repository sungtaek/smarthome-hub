from socketIO_client import SocketIO, LoggingNamespace
import logging
import json
from agent import Agent

logger = logging.getLogger(__name__)

class HubNamespace(LoggingNamespace):
    def initialize(self):
        self.agents = []

    def set_home(self, home):
        self.home = home

    def add_agent(self, agent):
        self.agents.append(agent)
        return len(self.agents)
    
    def on_connect(self):
        super(HubNamespace, self).on_connect()

        for agent in self.agents:
            account = {}
            account['home'] = self.home
            account['agent'] = agent.get_name()
            self.emit('join', account)
            logger.info('send join -> %s' % (json.dumps(account)))

    def on_action(self, *args):
        action = args[0]
        logger.info('recv action <- %s' % (json.dumps(action)))

        for agent in self.agents:
            if action['target'] == agent.get_name():
                code, message = agent.do_action(action)
                result = {}
                result['source'] = action['source']
                result['target'] = action['target']
                result['code'] = code
                result['message'] = message
                self.emit('result', result)
                logger.info('send result -> %s' % (json.dumps(result)))
                break
            
    def on_join(self, *args):
        account = args[0]
        logger.info('recv join <- %s' % (json.dumps(account)))

    def on_leave(self, *args):
        account = args[0]
        logger.info('recv leave <- %s' % (json.dumps(account)))
