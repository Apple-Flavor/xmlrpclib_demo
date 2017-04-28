#!encoding=utf8
import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://10.25.52.151:4000/")
print "%s" % str(proxy.echo("Hello"))#客户端调用XML-RPC函数
print "%s" % str(proxy.echo("World!"))
