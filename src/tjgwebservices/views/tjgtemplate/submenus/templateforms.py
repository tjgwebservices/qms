#!/usr/bin/env python3

class FormObject(object):
	templatetext = ""
	templateform = []

	def formPage(self,  title):
			self.templateform = []
			self.templateform.append('<div><p>'+title+'</p></div>')
			self.templateform.append('<div>')
			self.templateform.append('<form action="/formsubmission" method="POST">')
			self.templateform.append('<label for="pageName">Page Name:</label><br>')
			self.templateform.append('<input type="text" id="pageName" name="pageName" placeholder="Page Name"><br>')
			self.templateform.append('<label for="pageGroup">Page Group:</label><br>')
			self.templateform.append('<input type="text" id="pageGroup" name="pageGroup" placeholder="Page Group"><br>')
			self.templateform.append('<input type="submit" value="Submit" />')
			self.templateform.append('<br />')
			self.templateform.append('</form>')
			self.templateform.append('</div>')
			return self.templateform

	def __init__(self, arg):
		self.templatetext =""
		self.templatemodule = []
		self.arg = arg
		self.version = "0.0.0.1"
