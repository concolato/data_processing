#!/usr/bin/python
import os
from PIL import Image

class imgProcess():
	def __init__(self, filePath):
		self.filePath = filePath.strip()
	#end

	def rotate(self):
		try:
		   with open(self.filePath) as imageFile: #verify file is there
		   	
		   	FullfileName = os.path.basename(self.filePath)
		   	fileName = os.path.splitext(FullfileName)[0]
		   	newImage = 'img/rotate_'+fileName+'.png' #create new image file based on action taken

		   	if os.path.isfile(newImage):
				os.remove(newImage)
		  		print '\nOld File:',newImage,' Deleted/Replaced.\n'
			else:    ## Delete old file on re-run ##
				print '\nGenerating New Image File.'
		   	
		   	src_im = Image.open(imageFile)
			angle = 45
			size = 275, 275
			
			dst_im = Image.new("RGBA", (400,300), "blue" )
			im = src_im.convert('RGBA')
			rot = im.rotate( angle, expand=1 ).resize(size)
			dst_im.paste( rot, (50, 20), rot )
			dst_im.save(newImage)

			src_im.show() #show old stored image and newly processed image
		   	dst_im.show()
		except IOError:
		   print 'Oh dear. File:',self.filePath,' not found.'
	#end
#end class imgProcess