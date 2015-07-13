import sys
import logging
from server import Server

logger = logging.getLogger(__name__)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)

def help():
    logger.error('Usage: %s host port [http_proxy]' % str(sys.argv[0]))

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    if len(argv) < 3:
        help()
        sys.exit(2)

    host = str(argv[1])
    port = int(argv[2])

    server = Server(host, port)
    if len(argv) > 3:
        server.set_proxy('http', str(argv[3]))

    server.start()


if __name__ == '__main__':
    main()
