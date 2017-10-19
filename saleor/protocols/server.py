import sys
import os
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.application import service, internet
from twisted.internet.ssl import DefaultOpenSSLContextFactory

sys.path.append('.')

from base.search import SearchAPI

# default port in case of the env var not was properly set.
WEBSOCKET_PORT = 8005

proxy_port = int(os.environ.get('WEBSOCKET_PORT', WEBSOCKET_PORT))
ssl_port = 443
application = service.Application('TOPSPIN_WEBSOCKET')

search = SearchAPI()

root = Resource()
root.putChild("search", search)

site = Site(root)

# server = internet.TCPServer(proxy_port, site)
server = internet.SSLServer(ssl_port, site, DefaultOpenSSLContextFactory('/etc/nginx/ssl/topspin_in/server.key',
                                                                         '/etc/nginx/ssl/topspin_in/ssl-bundle.crt'))
server.setServiceParent(application)
