#!encoding=utf8
from SimpleXMLRPCServer import SimpleXMLRPCServer

def echo(s):
    return "*** %s ***"%s 
server = SimpleXMLRPCServer(("10.25.52.151", 4000))#确定URL和端口
print "Listening on port 4000..."
server.register_function(echo, "echo") #注册is_even函数
server.serve_forever()#启动服务器,并使其对这个连接可用
