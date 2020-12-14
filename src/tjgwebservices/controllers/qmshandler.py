#!/usr/bin/env python3
import http.server
import urllib.parse
from .qmscontroller import QMSController
from .socketcontroller import SocketController
from .formcontroller import FormController
from tjgwebservices.views.tjgtemplate.sheetobjects import TemplateSheets

class QMSHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
    def do_GET(self):
        ts = TemplateSheets()		
        self.csspaths = ts.csspaths
        self.jspaths = ts.jspaths
        self.fullpath = self.path
        pathurl = self.path.split('?')[0]
        pathprefix = "tjgwebservices/views"
        if pathurl  in ts.paths:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            QMSController(self,self.path)
        elif pathurl in ts.csspaths:
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            filepath = pathprefix +self.path
            filepath = filepath.split('?')[0]
            self.wfile.write(bytes(str(
                "".join(open(filepath,'r').readlines())
                ), "utf-8")) 
        elif pathurl  in ts.jspaths:
            self.send_response(200)
            self.send_header("Content-type", "text/js")
            self.end_headers()
            filepath = pathprefix +self.path
            filepath = filepath.split('?')[0]
            self.wfile.write(bytes(str(
                "".join(open(filepath,'r').readlines())
                ), "utf-8")) 
        elif pathurl[:6] == "images" or pathurl[:7] == "/images":
            if pathurl[:6] == "images":
                filepath = pathurl[7:]
            if pathurl[:7] == "/images":
                filepath = pathurl[8:]
            imageprefix = "tjgwebservices/views/static/img/"
            templatepath = imageprefix +filepath
            f = open(templatepath, 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        elif pathurl  in ts.socketpaths:
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            SocketController(self,self.path)
        elif pathurl[:8] == "/socket/":
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            SocketController(self,self.path)
        elif pathurl[:7] == "/topic/":
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            SocketController(self,self.path)
    
    def do_POST(self):
        #fields = parse_qsl(body)[1]
        pathurl = self.path.split('?')[0]
        content_length = int(self.headers['Content-Length'])
        if pathurl[:8] == "/socket/":
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            SocketController(self,self.path)
        elif pathurl[:7] == "/topic/":
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            SocketController(self,self.path)
        elif pathurl[:7] == "/socket":
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            SocketController(self,self.path)
        elif pathurl[:6] == "/topic":
            self.send_response(200)
            self.send_header("Content-type", "text/html;charset=utf-8")
            #self.send_header("Content-Length",  content_length)
            self.end_headers()        
        else:
            body = self.rfile.read(content_length)
            responsestring = body.decode('utf-8').splitlines()
            responsefields = urllib.parse.parse_qs(responsestring[0])
            if responsefields['pageName']:
                fc = FormController(self, pathurl,  responsefields)
            elif responsefields[0]=="test=test":
                fc=FormController(self, pathurl, responsefields)
                fc.db_init()
            
        
        
        

