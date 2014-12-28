#!/usr/bin/python
import urllib2, urllib
import smtplib

#Boolean
def getImage(url, fileName):
	print "Fetch image from URL for ", fileName
	
	try:
	    urllib.urlretrieve(url, fileName)

	except Exception, e:
		print e
		emailNotify(e, url)

		raise
	else:
		pass
	finally:
		pass
# end getImage

def emailNotify(errorMsg, url):
	if url:
		sender = 'archturiasystems@gmail.com'
		receivers = ['claude.mercury@gmail.com']

		message = """From: From Person <from@fromdomain.com>
		To: To Person <to@todomain.com>
		Subject: SMTP e-mail test

		Error: """,errorMsg, """; 
		getImage e-mail message. 
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

def main():
	fileName = 'data/noaaForcastCloudCover.gif'
	url = 'https://ready.arl.noaa.gov/data/forecast/grads/gfs/panel10/anim.gif'
	getImage(url,fileName)

	fileName2 = 'data/noaaForcastPrecipitation.gif'
	url2 = 'https://ready.arl.noaa.gov/data/forecast/grads/nam/panel9/anim.gif'
	getImage(url2,fileName2)

	fileName3 = 'data/noaaForcastPrecipitationThickness.gif'
	url3 = 'https://ready.arl.noaa.gov/data/forecast/grads/gfs/panel2/anim.gif'
	getImage(url3,fileName3)

	fileName4 = 'data/noaaForcastWindVortex.gif'
	url4 = 'https://ready.arl.noaa.gov/data/forecast/grads/gfs/panel1/anim.gif'
	getImage(url4,fileName4)

	fileName5 = 'data/noaaForcastCAPE.gif'
	url5 = 'https://ready.arl.noaa.gov/data/forecast/grads/gfslr/panel7/anim.gif'
	getImage(url5,fileName5)

	fileName6 = 'data/humidity.gif'
	url6 = 'http://weather.rap.ucar.edu/model/gfs012hr_925_tmp.gif'
	getImage(url6,fileName6)

	fileName7 = 'data/globalWeather.gif'
	url7 = 'http://www.eldoradocountyweather.com/current/skymet/skymet_kshgkhsworld.jpeg'
	getImage(url7,fileName7)

	fileName8 = 'data/globalHighTemps.gif'
	url8 = 'http://www.wunderground.com/data/images/world_highs24.gif'
	getImage(url8,fileName8)
#end main

main()
