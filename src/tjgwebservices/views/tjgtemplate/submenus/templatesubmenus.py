#!/usr/bin/env python3
from .templateforms import FormObject

class TemplateSubMenuObject(object):
	templatetext = ""
	templatemodule = []
  
  
	def printTemplate(self):
		if self.arg == "/home":
			self.templatemodule = self.forms.formRegistration(self.forms)
		elif self.arg == "/page":
			self.templatemodule = self.forms.formPage(self.forms,"Page")
 

	def createForm(self, action, method,elements ):	
		formmodule = []
		formmodule.append('<form action="'+action+'" method="'+method+'" >')
		formmodule.extend(elements)
		formmodule.append('</form>')        
		return formmodule

	def createInputElement(self, type, idname, value):
		inputmodule = []
		inputmodule.append('<input type="'+type+'" id="'+idname+'" name="'+idname+'" value="'+value+'" />')
		return inputmodule

	def __init__(self, arg):
		self.templatetext =""
		self.templatemodule = []
		self.arg = arg
		self.version = "0.0.0.1"
		self.forms = FormObject
