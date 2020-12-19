#!/usr/bin/env python3


class MenuDoc(object):
	def __init__(self, doc):
		self.doc = doc

	def retrieveValue(self,value):
		return self.doc.getElementsByTagName(value)[0].childNodes[0].nodeValue.strip()

	def retrieveMainMenu(self):
		i = []
		items=self.doc.getElementsByTagName('mainmenu')[0].getElementsByTagName('item')
		for item in items:
			ei = []
			id = item.getAttribute('id')
			name = item.getElementsByTagName('name')[0].childNodes[0].nodeValue.strip()
			link = item.getElementsByTagName('link')[0].childNodes[0].nodeValue.strip()
			submenu = item.getElementsByTagName('submenu')[0].childNodes[0].nodeValue.strip()
			ei.append([id, name, link, submenu])
			i.append(ei)
		return i

	def retrieveSubMenu(self):
		i = []
		items=self.doc.getElementsByTagName('mainsubmenu')[0].getElementsByTagName('item')
		for item in items:
			ei = []
			id = item.getAttribute('id')
			name = item.getElementsByTagName('name')[0].childNodes[0].nodeValue.strip()
			link = item.getElementsByTagName('link')[0].childNodes[0].nodeValue.strip()
			parentmenu = item.getElementsByTagName('parentmenu')[0].childNodes[0].nodeValue.strip()
			submenu = item.getElementsByTagName('submenu')[0].childNodes[0].nodeValue.strip()
			ei.append([id, name, link, parentmenu, submenu])
			i.append(ei)
		return i

	def retrieveSubSubMenu(self):
		i = []
		items=self.doc.getElementsByTagName('subsubmenu')[0].getElementsByTagName('item')
		for item in items:
			ei = []
			id = item.getAttribute('id')
			name = item.getElementsByTagName('name')[0].childNodes[0].nodeValue.strip()
			link = item.getElementsByTagName('link')[0].childNodes[0].nodeValue.strip()
			parentmenu = item.getElementsByTagName('parentmenu')[0].childNodes[0].nodeValue.strip()
			ei.append([id, name, link, parentmenu])
			i.append(ei)
		return i

