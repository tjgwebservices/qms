#!/usr/bin/env python3

from tjgwebservices.views.tjgtemplate.templateqms import *
from tjgwebservices.controllers.utils.loggerinitializer import *

class SocketController():
    def writeToResponse(self, text):
        self.handler.wfile.write(bytes(str(text), "utf-8")) 
     
    def writeToClose(self):
        if not self.handler.wfile.closed:
            self.handler.wfile.flush()

    def sendEventStreamResponse(self): 
            self.wfile.write(b'name: ')
            self.wfile.write('sockettest')
            self.wfile.write(b'\r\n')
            self.wfile.write(b'data: ')
            self.wfile.write("[{'name':'sockettest'}]")
            self.wfile.write(b'\r\n')
            self.wfile.write(b'\r\n')
            self.writeToClose()
            
    def __init__(self,  handler1, arg1):
        self.argpath = arg1.split('?')[0]
        logging.info("Argument Path: "+self.argpath)
        self.handler = handler1
        if self.argpath in []:
            self.sendEventStreamResponse()

