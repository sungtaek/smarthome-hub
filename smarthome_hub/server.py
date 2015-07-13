from socketIO_client import SocketIO, LoggingNamespace
import logging
from namespace import HubNamespace

logger = logging.getLogger(__name__)

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.proxies = {}

    def set_proxy(self, protocol, url):
        self.proxies.append(protocol, url)
        logger.info('set proxy %s=%s' % (protocol, url))

    def start(self):
        logger.info('Server started [%s:%d]...' % (self.host, self.port))
        self.socket = SocketIO(self.host, self.port, HubNamespace, proxies=self.proxies)
        self.socket.wait()


