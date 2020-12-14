#!/usr/bin/env python3

import sqlite3
import email.parser
import binascii

class FormController():
    formpaths = ["/formsubmission","/pagesubmission" ]
    querypaths = ["/dbcreate", "/dbselect"]
    
    def encode_multipart_formdata(fields):
        boundary = binascii.hexlify(os.urandom(16)).decode('ascii')
        body = (
            "".join("--%s\r\n"
                    "Content-Disposition: form-data; name=\"%s\"\r\n"
                    "\r\n"
                    "%s\r\n" % (boundary, field, value)
                    for field, value in fields.items()) +
            "--%s--\r\n" % boundary
        )
        content_type = "multipart/form-data; boundary=%s" % boundary
        return body, content_type        
        
    def decode_parser(self, my_multipart_data):
        msg = email.parser.BytesParser().parsebytes(my_multipart_data)
        print({
            part.get_param('name', header='content-disposition'): part.get_payload(decode=True)
            for part in msg.get_payload()
        })        
        
    def __init__(self,  handler1, arg1,  data):
        self.argpath = arg1.split('?')[0]
        self.handler = handler1
        if self.argpath in self.formpaths:
            self.form_process(data)
        elif self.argpath in self.querypaths:
            self.db_query()

    def db_query(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('SELECT * FROM pages')
        conn.close()
        data = c.fetchone()
        self.writeToResponse(data)

    def db_create(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE pages
                     (id integer PRIMARY KEY, 
                     pageName text, 
                     pageGroup text)''')
        conn.commit()
        conn.close()
        self.writeToResponse(data)

    def form_process(self, data):
        pagename = data["pageName"][0]
        pagegroup = data["pageGroup"][0]
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute("INSERT INTO pages VALUES (?,?)",  pagename,  pagegroup)
        conn.commit()       

class MIMEFormdata(nonmultipart.MIMENonMultipart):
    def __init__(self, keyname, *args, **kwargs):
        super(MIMEFormdata, self).__init__(*args, **kwargs)
        self.add_header(
            "Content-Disposition", "form-data; name=\"%s\"" % keyname)

