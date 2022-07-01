import socket
import tornado.web
import tornado.ioloop
from threading import Thread 

ip = "192.168.43.59"
port = 25565

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip,port))

server.listen(5)

t = "0";


def dataserver():
    while True:

        client,addr = server.accept()
        print("connect",addr)
        data = client.recv(30)
        data = (int(data,)/10);
        global t
        t = str(data)
        print("recive:",data)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("connect")
        self.render("index.html")

class temphandler(tornado.web.RequestHandler):
    def get(self):
        global t
        self.write(t)

def mainwebpage():
    return tornado.web.Application([
        (r"/",MainHandler),
        (r"/temp",temphandler)
        ])
tcpcore = Thread(target = dataserver)
def webpage():
    tcpcore.start()
    app = mainwebpage()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(80)
    server.start()
    tornado.ioloop.IOLoop.current().start()
    




webcore = Thread(target = webpage())
webcore.start()
webcore.join()    

    


    

