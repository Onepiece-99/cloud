from wsgiref.simple_server import make_server
from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import Integer, Float


class DivideService(ServiceBase):
   @rpc(Integer, Integer, _returns=Integer)
   def mul_numbers(self, num1, num2):
      return num1 * num2

class CalculationService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add_numbers(self, num1, num2):
        return num1 + num2
   
    @rpc(Integer, Integer, _returns=Integer)
    def sub_numbers(self, num1, num2):
        return num1 - num2

soap_app = Application([CalculationService,DivideService],
                       tns='example.soap',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

wsgi_app = WsgiApplication(soap_app)

host = 'localhost' #or'127.0.0.1'
port = 10000 #or'7567'

server = make_server(host, port, wsgi_app)
print(f"Listening on {host}:{port}")
server.serve_forever()
