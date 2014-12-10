#!/usr/bin/python
import pprint
import json
import urllib2

def getUSGS_json():
	print "Fetch data from URL"

	fileName = 'data/usgsEarthquacks_12Hrs.json'
	url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
	data = urllib2.urlopen(url)

	if data:
		try:
			with open(fileName) as jsonGetData:
				filePut = open(fileName, 'w+')
				#add data
				filePut.write(data)
				filePut.close()

				j = json.load(jsonGetData)
				print j
		except Exception, e:
			print e
			raise
		else:
			pass
		finally:
			pass
	#end if
#end getUSGS_json

getUSGS_json()