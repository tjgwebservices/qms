#!/usr/bin/env python3

from xml.dom import minidom
from tjgwebservices.models.menumodel import MenuDoc
from tjgwebservices.models.webmodel import WebDoc
from tjgwebservices.views.tjgtemplate.sheetobjects import TemplateSheets
from tjgwebservices.views.tjgtemplate.submenus.templatesubmenus import TemplateSubMenuObject

class TemplateQMSObject(object):
    templatetext = ""
    templatemodule = []

    doc = minidom.parse('tjgwebservices/views/static/xml/menu.xml')
    m = MenuDoc(doc)
    
    mi = m.retrieveMainMenu()
    si = m.retrieveSubMenu()
    ssi = m.retrieveSubSubMenu()
    mis = {}
    sis = {}
    ssis = {}
    
    for i in mi:
        mis[int(i[0][0])] = {'name':i[0][1], 'link':i[0][2], 'submenu':i[0][3]}
    for i in si:
        sis[int(i[0][0])] = {'name':i[0][1], 'link':i[0][2], 'parentmenu':i[0][3], 'submenu':i[0][4]}
    for i in ssi:
        ssis[int(i[0][0])] = {'name':i[0][1], 'link':i[0][2], 'parentmenu':i[0][3]}
        
    menu_items = mis
    sub_menu_items = sis
    sub_sub_menu_items = ssis
    
    
    def __init__(self,arg):
        self.arg = arg
        doc = minidom.parse('tjgwebservices/views/static/xml/website.xml')
        w = WebDoc(doc)
        self.version = w.retrieveValue("version")
        self.headingtitle=w.retrieveValue("headingtitle")
        self.headingdescription=w.retrieveValue("headingdescription")
        self.headingkeywords=w.retrieveValue("headingkeywords")
        self.headingauthor=w.retrieveValue("headingauthor")
        self.navigationtitle1=w.retrieveValue("navigationtitle1")
        self.navigationtitle2=w.retrieveValue("navigationtitle2")
        self.headertitle1=w.retrieveValue("headertitle1")
        self.headertitle2=w.retrieveValue("headertitle2")
        ts = TemplateSheets()
        hd = ''.join(self.printHeading(self.headingtitle, self.headingdescription,  self.headingkeywords,  self.headingauthor))
        bs = ''.join(self.printBodyStart())
        nb = ''.join(self.printNavBar())
        mi = ''.join(self.print_menu_items(self.menu_items, self.sub_menu_items, self.sub_sub_menu_items))
        nc = ''.join(self.printNavClose())
        ms = ''.join(self.printMainSection())
        if self.arg in ts.paths:
            sm = ''.join(TemplateSubMenuObject(self.arg).printTemplate())
            #sm = "\n\n\n<div>"+str(self.arg)+"</div>\n\n\n"    
        else:
            sm = "\n\n\n<div>Index Page</div>\n\n\n"
        if self.arg == "/conference":
            vs = ''.join(self.printVideoSection()) 
        else:
            vs = ''
        if self.arg == "/conference":
            fs = ''.join(self.printConferenceFooter())
        else:
            fs = ''.join(self.printFooter())
        self.templatetext= hd+bs+nb+mi+nc+ms+sm+vs+fs   

    def print_menu_items(self, menu_items, sub_menu_items, sub_sub_menu_items):
            first = True
            last = False
            menuitems = []
            for k1,v1 in menu_items.items():
                if v1['submenu']=='yes':
                    menuitems.append('        <li><span class="dropdown1"><a href="'+v1['link']+'">'+v1['name']+"</a>\n")
                    menuitems.append('			<span class="dropdown1-content">')
                    for k2,v2 in sub_menu_items.items():
                        if v2['parentmenu'] == k1:
                            for k3,v3 in sub_sub_menu_items.items():
                                if v3['parentmenu'] == k2:
                                    if first == True:
                                        menuitems.append(''+"\n")
                                        first = False
                                    menuitems.append('<a href="'+v3['link']+'">'+v3['name']+"</a>\n")
                            #        last = True
                            #if last == True:
                            menuitems.append("")
                            menuitems.append('<a href="'+v2['link']+'">'+v2['name']+'</a>'+"\n")
                    menuitems.append('</span></span></li>')
                else:
                    menuitems.append('        <li><a href="'+v1['link']+'">'+v1['name']+"</a></li>\n")
            return menuitems

    

    def printHeading(self, title, description, keywords, author):
        heading = []
       # heading.append('Content-type: text/html; charset=utf-8\n\n')
        heading.append('<!DOCTYPE html>')
        heading.append('<html>')
        heading.append('<head>')
        heading.append('<meta charset="utf-8">')
        heading.append('<title>'+title+'</title>')
        heading.append('<meta name="description" content="'+description+'" />')
        heading.append('<meta name="keywords" content="'+keywords+'" />')
        heading.append('<meta name="author" content="'+author+'">')
        heading.append('<meta name="robots" content="index, follow">')
        heading.append('<meta name="revisit-after" content="3 month">')
        heading.append('<meta name="viewport" content="width=device-width, initial-scale=1" />')
        heading.append('<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">')
        heading.append('<link rel="icon" type="image/png" sizes="96x96" href="/images/favicon.ico">')
        heading.append('<link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">')
        heading.append('<link rel="stylesheet" href="/static/css/home.css?v='+self.version+'" />')
        heading.append('</head>')
        return heading

    def printBodyStart(self):
        body = []
        body.append('<body class="mainpage">')
        return body 

    def printNavBar(self):
        navstart = []
        navstart.append('<!-- Navbar (sit on top) -->')
        navstart.append('<div class="top">')
        navstart.append('  <ul class="navbar" id="navbar">')
        navstart.append('    <li>')
        navstart.append('      <a href="#home">'+self.headingtitle+'</a>')
        navstart.append('    </li>')
        navstart.append('    <!-- Right-sided navbar links -->')
        navstart.append('      <!--a href="#home"><i class="fa fa-home"></i></a-->')
        navstart.append('  </ul>')
        navstart.append('  <ul class="navbar">')
        return navstart
 
    def printNavClose(self):
        navclose = []
        navclose.append('    </ul>')
        navclose.append('	<ul class="navbar">')
        navclose.append('	    <li><a href="javascript:void(0)" onclick="navmenu(\'login\');">Login</a></li>')
        navclose.append('	    <li><a href="javascript:void(0)" onclick="navmenu(\'post\');">Post</a></li>')
        navclose.append('	    <li><a href="javascript:void(0)" onclick="navmenu(\'signup\');">Sign Up</a></li>')
        navclose.append('	    <li><a href="javascript:void(0)" onclick="navmenu(\'subscribe\');">Subscribe</a></li>')
        navclose.append('	    <li><a href="javascript:void(0)" onclick="navmenu(\'options\');">Options</a></li>')        
        navclose.append('   </ul>')
        navclose.append('	<ul class="navbar">')
        navclose.append('        <li><h5>'+self.navigationtitle1+'&nbsp;&nbsp;&nbsp;</h5></li>')
        navclose.append('        <li><h5>'+self.navigationtitle2+'&nbsp;&nbsp;&nbsp;</h5></li>')
        navclose.append('   </ul>')
        navclose.append('</div>')
        return navclose

    def printMainSection(self):
        mainsection = []
        mainsection.append('					<nav class="sidenavbar" style="display:none" id="sidenav">')
        mainsection.append('  <a href="javascript:void(0)" onclick="menu_close()">Close X</a>')
        mainsection.append('								<a href="#home">Home</a>')
        mainsection.append('								<a href="#contact">Contact</a>')
        mainsection.append('					</nav>')
        mainsection.append('			<div id="page-wrapper">')
        mainsection.append('<header class="bannerbkgnd" id="home">')
        mainsection.append('  <div class="bannerbox">')
        mainsection.append('							<h1>'+self.headingtitle+'</h1>')
        mainsection.append('    <span>'+self.headingdescription+'</span><br>')
        mainsection.append('    <img src="images/logo.png" alt="Logo" />')
        mainsection.append('    <span>'+self.headertitle1+'</span>')
        mainsection.append('							<h3>'+self.headertitle2+'</h3>')
        mainsection.append('  </div> ')
        mainsection.append('  <div id="carousel">')
        mainsection.append('<br /><br />')
        mainsection.append('  </div>')
        mainsection.append('</header>')
        return mainsection
        
    def printVideoSection(self):
        videosection = []
        videosection.append('<div id="conferenceroom">')
        videosection.append('<video id="selfView">')
        videosection.append('</video>')
        videosection.append('<video id="remoteView">')
        videosection.append('</video>')
        videosection.append('</div>')
        videosection.append('<table id="eventTable">')
        videosection.append('<tr><td></td><td></td></tr>')
        videosection.append('<tr><td></td><td></td></tr>')        
        videosection.append('</table>')
        return videosection


    def printConferenceFooter(self):
        footersection = []
        footersection.append('</div>')
        footersection.append('		<div id="footer">')
        footersection.append('		<section id="banner">')
        footersection.append('			<div class="inner">')
        footersection.append('				<h2>'+self.headingtitle+'</h2>')
        footersection.append('				<div class="logo"> <img src="images/logo.png" width="100" height="100" alt="Logo" /></div>')
        footersection.append('			</div>')
        footersection.append('		</section>')
        footersection.append('				<ul class="copyright">')
        footersection.append('					<li>2020 &copy; <a href="//tjgwebservices.com">'+self.headingtitle+'.</a></li>')
        footersection.append('				</ul>')
        footersection.append('		</div>')
        footersection.append('		</div>')
        footersection.append('</body>')
        footersection.append('<script src="/static/js/script.js?v='+self.version+'"></script>')
        footersection.append('<script src="/static/js/home.js?v='+self.version+'"></script>')
        footersection.append('</html>')
        return footersection
        
    def printFooter(self):
        footersection = []
        footersection.append('</div>')
        footersection.append('		<div id="footer">')
        footersection.append('		<section id="banner">')
        footersection.append('			<div class="inner">')
        footersection.append('				<h2>'+self.headingtitle+'</h2>')
        footersection.append('				<div class="logo"> <img src="images/logo.png" width="100" height="100" alt="Logo" /></div>')
        footersection.append('			</div>')
        footersection.append('		</section>')
        footersection.append('				<ul class="copyright">')
        footersection.append('					<li>2020 &copy; <a href="/">'+self.headingtitle+'.</a></li>')
        footersection.append('				</ul>')
        footersection.append('		</div>')
        footersection.append('		</div>')
        footersection.append('</body>')
        footersection.append('<script src="/static/js/home.js?v='+self.version+'"></script>')
        footersection.append('</html>')
        return footersection
