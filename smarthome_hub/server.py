from socketIO_client import SocketIO, LoggingNamespace
import logging
from namespace import HubNamespace
from led import Led

logger = logging.getLogger(__name__)

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.proxies = {}

    def set_proxy(self, protocol, url):
        self.proxies[protocol] = url
        logger.info('set proxy %s=%s' % (protocol, url))
    
    def start(self):
        logger.info('Server started [%s:%d]...' % (self.host, self.port))
        self.socket = SocketIO(self.host, self.port, proxies=self.proxies)
        self.namespace = self.socket.define(HubNamespace)
        self.namespace.set_home('sungtaek')
        self.namespace.add_agent(Led('led'))
        self.socket.wait()

