#!/usr/bin/python
print "Open File, Read and Transfer Image Data"
fileName = 'img/lena256_PGM.pgm'

try:
   with open(fileName): #verify file is there
   	# Open a file
	openFile = open(fileName, "r")
	contents = openFile.read()

	print "Name of the file: ", openFile.name
	print "Contents: ",contents
	
	#create new file
	filePut = open('img/rawImageNew.pgm', 'w+')
	#add data
	filePut.write(contents)

	openFile.close()
	filePut.close()
	print 'File:', filePut.name, ' created.'
except IOError:
   print 'Oh dear. File:',fileName,' not found.'
