#!/usr/bin/env python3

from http.server import HTTPServer
from tjgwebservices.controllers.qmshandler import QMSHandler

hostName = "127.0.0.1"
serverPort = 8080

if __name__ == "__main__": 
    webServer = HTTPServer((hostName, serverPort), QMSHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
