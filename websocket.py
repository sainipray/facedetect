import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        from sub_app.py_files.detect import get_face_detect_data
        image_data = get_face_detect_data(message)
        if not image_data:
            image_data = message
        self.write_message(image_data)
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/websocket', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()