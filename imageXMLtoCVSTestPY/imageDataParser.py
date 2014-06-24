#!/usr/bin/python
import csv
import json
from xml.dom import minidom

class imageDataParser():
	'Class for retieving and parsing JSON, CSV, and XML'
	def __init__(self,filePath): 
		self.filePath = filePath;

	def fileParseXML(self):
		try:
		   with open(self.filePath): #verify file is there	   
		   	# Open a file
			xmldoc = minidom.parse(self.filePath)
			itemlist = xmldoc.getElementsByTagName('image')
			commentName = ''
			Loacation = ''
			imageData = ''

			for image in itemlist :
				comment = image.getElementsByTagName('comment')[0]
				comment_name_text = comment.getElementsByTagName('name')[0].firstChild.nodeValue

				if(comment_name_text == "Patient 1 Liver Tumer"):
					commentName = comment_name_text
					Loacation = image.getElementsByTagName('location')[0].firstChild.nodeValue
			
			imageData = commentName,': ',Loacation		
			return Loacation

		except IOError:
		   print 'Oh dear. File:',filePath,' not found.'
	#end fileParseXML function

	def fileParseCSV(self):
		try:
		   with open(self.filePath, "rb") as csvFile: #verify file is there
		   	# Open a file
			input_file = csv.DictReader(csvFile)
			commentName = ''
			Loacation = ''

			for row in input_file:
				if(row["comment_name"] == " Patient 1 Liver Tumer"):
					commentName = row["comment_name"]
					Loacation = row["location"]

			#print commentName,': ',Loacation
			return Loacation

		except IOError:
		   print 'Oh dear. File:',self.filePath,' not found.'
	#end fileParseCSV function

	def fileParseJSON(self):
		try:
		   with open(self.filePath) as jsonFile: #verify file is there
		   	# Open a file
			#input_file = jsonFile.read()
			j = json.load(jsonFile)
			commentName = ''
			Loacation = ''

			for nodes in j:
				if(nodes['image']['annotations']['comment']['name'] == "Patient 0 Brain Tumer"):
					commentName = str(nodes['image']['annotations']['comment']['name'])
					Loacation = str(nodes['image']['location']) 

			return Loacation

		except IOError:
		   print 'Oh dear. File:',self.filePath,' not found.'
	#end fileParseJSON function
#end ImageDataParser class
