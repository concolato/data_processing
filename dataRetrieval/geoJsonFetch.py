#!/usr/bin/python
import pprint, json, urllib2
import smtplib

def getUSGS_json():
	print "Fetch data from URL"

	fileName = 'data/usgsEarthquacks_24Hrs.json'
	url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
	
	try:
	    urllib2.urlopen(url)
	    filePut = open(fileName, 'w')
	    data = urllib2.urlopen(url).read()

	except urllib2.HTTPError, e:
	    print(e.code)

	    emailNotify(e.code, url)
	    data = 0
	except urllib2.URLError, e:
	    print(e.args)

	    emailNotify(e.args, url)
	    data = 0

	if data != 0: #validate url
		try:
			with open(fileName) as jsonGetData:				
				#add data
				filePut.write(data)
				filePut.close()

				j = json.load(jsonGetData)
				print "Json processed."
				return 1
		except Exception, e:
			print e
			emailNotify(e, url)

			raise
		else:
			pass
		finally:
			pass
	else:
		print url," Not available."
		return 0
#end getUSGS_json

def getGlobalCitiesWeather_jsonTest():
	print "Fetch data from Openweathermap API"

	baseAPIUrl = "http://api.openweathermap.org"
	fileName = 'data/globalCitiesWeather.json'
	#globalCities = 'data/globalCities.json'
	globalCities = 'data/testCountries.json'
	geodata = returnJson(globalCities)
	count = 0
	dataCheck = 1

	try:
	    urllib2.urlopen(baseAPIUrl)

	except urllib2.HTTPError, e:
	    print(e.code)

	    emailNotify(e.code, baseAPIUrl)
	    dataCheck = 0
	except urllib2.URLError, e:
	    print(e.args)

	    emailNotify(e.args, baseAPIUrl)
	    dataCheck = 0

	if dataCheck != 0: #validate url
		data = "["
		for datacapital_country in geodata:
			url = baseAPIUrl+'/data/2.5/weather?q='+datacapital_country['capital']+','+datacapital_country['country']+'&appid=getyourown&units=metric'
			data += urllib2.urlopen(url).read()
			#247
			if count >= 1:
				data += ""
			else:
				data += ","

			count += 1
			#print url

		data += "]"

		print data
		print count

		filePut = open(fileName, 'w')

		try:
			with open(fileName) as jsonGetCountriesData:				
				#add data
				filePut.write(data)
				filePut.close()

				#j = json.load(jsonGetCountriesData)
				print "Json processed."
				return 1
		except Exception, e:
			print e
			emailNotify(e, url)

			raise
		else:
			pass
		finally:
			pass
	else:
		print fileName+' failed to process for '+baseAPIUrl+'.'


def getGlobalCitiesWeather_json():
	print "Fetch data from API"

	fileName = 'data/globalCitiesWeather.json'
	globalCities = 'data/globalCities.json'
	cities = returnJson(globalCities)
	#Sample URL
	url = 'http://api.openweathermap.org/data/2.5/weather?q=london,uk&appid=getyourown&units=metric'
	
	try:
	    urllib2.urlopen(url)
	    filePut = open(fileName, 'w')
	    data = urllib2.urlopen(url).read()

	except urllib2.HTTPError, e:
	    print(e.code)

	    emailNotify(e.code, url)
	    data = 0
	except urllib2.URLError, e:
	    print(e.args)

	    emailNotify(e.args, url)
	    data = 0

	if data != 0: #validate url
		try:
			with open(fileName) as jsonGetData:				
				#add data
				filePut.write(data)
				filePut.close()

				j = json.load(jsonGetData)
				print "Json processed."
				return 1
		except Exception, e:
			print e
			emailNotify(e, url)

			raise
		else:
			pass
		finally:
			pass
	else:
		print url," Not available."
		return 0
#end getUSGS_json

def emailNotify(errorMsg, url):
	if url:
		sender = 'archturiasystems@gmail.com'
		receivers = ['claude.mercury@gmail.com']

		message = """From: From Person <from@fromdomain.com>
		To: To Person <to@todomain.com>
		Subject: SMTP e-mail test

		Error: """,errorMsg, """; 
		getUSGS_json e-mail message. 
		""", url,""" Not available."""

		try:
		   smtpObj = smtplib.SMTP('smtp.gmail.com')
		   smtpObj.sendmail(sender, receivers, message)

		   print "Successfully sent email"
		except Exception, e:
		   print "Error: unable to send email ",e
	else:
		print url, " not set in emailNotify()"
#end emailNotify

def returnJson(source):
	#Grab destination file json
	try:
	   with open(source) as jsonFile: # Open and verify file is there
	   	# load JSON object into memory
		j = json.load(jsonFile)

		return j
	except Exception, e:
		print e
		raise
# end returnJson

#getUSGS_json()
getGlobalCitiesWeather_jsonTest()