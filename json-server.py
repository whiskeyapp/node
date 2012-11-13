from txjsonrpc.web import jsonrpc
from twisted.web import server
from twisted.internet import reactor

class Math(jsonrpc.JSONRPC):
    def jsonrpc_add(self,  a,  b):
        return a + b 
        
reactor.listenTCP(8007,  server.Site(Math()))
reactor.run()
