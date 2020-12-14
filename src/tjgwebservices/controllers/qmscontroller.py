#!/usr/bin/env python3

from tjgwebservices.views.tjgtemplate.templateqms import *
from tjgwebservices.controllers.utils.loggerinitializer import *
from tjgwebservices.views.tjgtemplate.sheetobjects import TemplateSheets


class QMSController():
    def writeToResponse(self, text):
        self.handler.wfile.write(bytes(str(text), "utf-8")) 
     
    def writeToClose(self):
        if not self.handler.wfile.closed:
            self.handler.wfile.flush()

    def buildQMSTemplate(self): 
        tmo = TemplateQMSObject(self.argpath)
        self.writeToResponse(tmo.templatetext)
        self.writeToClose()
            
    def __init__(self,  handler1, arg1):
        ts = TemplateSheets()
        self.argpath = arg1.split('?')[0]
        logging.info("Argument Path: "+self.argpath)
        self.handler = handler1
        if self.argpath in ts.paths:
            self.buildQMSTemplate()

