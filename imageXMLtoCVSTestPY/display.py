#!/usr/bin/python
import logging
import time
from imageDataParser import imageDataParser
from imgProcess import imgProcess

class display(imageDataParser):
	def __init__(self):
		fileNameXML = 'data/xmlImageData.xml'
		fileNameCSV = 'data/xmlImageData.csv'
		fileNameJSON = 'data/xmlImageData.json'
		imagePathXML = ''
		imagePathCSV = ''
		imagePathJSON = ''

		start1 = time.clock() *1000
		imageDataParser.__init__(self,fileNameXML) #pass file name into the class 
		#Then call the method after instantiation
		imagePathXML = imageDataParser.fileParseXML(self) #retrieve 1 image 
		stop1 = time.clock() *1000 

		start2 = time.clock() *1000
		imageDataParser.__init__(self,fileNameCSV)
		for x in range(0, 19):
			imagePathCSV = imageDataParser.fileParseCSV(self) #retrieve 10 images
		stop2 = time.clock() *1000

		start3 = time.clock() *1000
		imageDataParser.__init__(self,fileNameJSON)
		for x in range(0, 11):
			imagePathJSON = imageDataParser.fileParseJSON(self) #retrieve 10 images
		stop3 = time.clock() *1000

		#Calculate execution time
		XML_time = stop1 - start1
		CSV_time = stop2 - start2
		JSON_time = stop3 - start3

		print '---Welcome to ImaJin 0.1---\n'
		print 'Data Format Execution Speeds in Milliseconds:\r'
		print 'XML ',XML_time,'ms \r'
		print 'CSV ',CSV_time,'ms \r'
		print 'JSON ',JSON_time,'ms \r'

		self.displayImg(XML_time,CSV_time,JSON_time,imagePathXML,imagePathJSON,imagePathCSV)
	#end constructor

	def displayImg(self,XML_time,CSV_time,JSON_time,imagePathXML,imagePathJSON,imagePathCSV):
		#begin to process fastest time and image as a proof of concept
		if(int(XML_time) < int(CSV_time)) or (int(XML_time) < int(JSON_time)):
			img = imgProcess(imagePathXML)
			img.rotate()
			print 'XML image path processed.'
		elif(int(JSON_time) < int(CSV_time)) and (int(JSON_time) < int(XML_time)):
			img = imgProcess(imagePathJSON)
			img.rotate()
			print 'JSON image path processed.'
		else:	
			img = imgProcess(imagePathCSV)
			img.rotate()
			print 'CSV image path processed.'
	#end displayImg
#end class display
display()
