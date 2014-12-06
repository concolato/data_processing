#!/usr/bin/python
import pprint
import json
import time

def jsonReporter(): 
	print "Open File, Read and Do Sumation of Data"
	fileName = 'data/oasp.json'

	try:
	   with open(fileName) as jsonFile: # Open and verify file is there
		start1 = time.clock() *1000
	   	# load JSON object into memory
		j = json.load(jsonFile)
		#Initialize stat vars
		asian_pop = 0
		asian_age_18_24 = 0
		asian_lang_prof = 0
		asian_age_18_24 = 0
		asian_age_25_54 = 0
		asian_age_55_over = 0
		asian_unemployment = 0
		asian_edu_less_than_high = 0
		asian_edu_high_ged = 0
		asian_edu_some_college = 0
		asian_edu_college_higher = 0
		asian_disability = 0
		asian_poverty = 0
		asian_male = 0
		asian_female = 0
		count = 0

		print "Name of the file: \r", jsonFile.name, '\r'
		#print "Contents: ",contents

		for nodes in j['features']:
			if(nodes['properties']['metro_area'] == "Abilene"):				
				print #nodes['geometry']['coordinates']
			
		#pprint.pprint(j) #Like a var_dump in php

		for dataAdd in j['features']:
			asian_pop += dataAdd['properties']['asian_pop']
			asian_age_18_24 += dataAdd['properties']['asian_age_18_24_raw']
			asian_lang_prof += dataAdd['properties']['asian_lang_prof_raw']
			asian_age_25_54 += dataAdd['properties']['asian_age_25_54_raw']
			asian_age_55_over += dataAdd['properties']['asian_age_55_over_raw']
			asian_unemployment += dataAdd['properties']['asian_unemployment']
			asian_edu_less_than_high += dataAdd['properties']['asian_edu_less_than_high_raw']
			asian_edu_high_ged += dataAdd['properties']['asian_edu_high_ged_raw']
			asian_edu_some_college += dataAdd['properties']['asian_edu_some_college_raw']
			asian_edu_college_higher += dataAdd['properties']['asian_edu_college_higher_raw']
			asian_disability += dataAdd['properties']['asian_disability_raw']
			asian_poverty += dataAdd['properties']['asian_poverty']
			asian_male += dataAdd['properties']['asian_male_raw']
			asian_female += dataAdd['properties']['asian_female_raw']

			count += 1

		asian_unemployment_mean = dataMean(asian_unemployment, count)
		asian_poverty_mean = dataMean(asian_poverty, count)
		stop1 = time.clock() *1000 
		
		JSON_time = stop1 - start1

		print "Nation Wide Asian American Stat Report: ", JSON_time, 'millisec to process. \r'
		print "asian_population: ",asian_pop, '\r'
		print "asian_age_18_24: ",asian_age_18_24, '\r'
		print "asian_age_25_54: ",asian_age_25_54, '\r'
		print "asian_age_55_over: ",asian_age_55_over, '\r'
		print "asian_lang_prof: ",asian_lang_prof, '\r'
		print "asian_unemployment_mean: ",asian_unemployment_mean, '\r'
		print "asian_poverty_mean: ",asian_poverty_mean, '\r'
		print "asian_edu_some_college: ",asian_edu_some_college, '\r'
		print "asian_edu_high_ged: ",asian_edu_high_ged, '\r'
		print "asian_edu_college_higher: ",asian_edu_college_higher, '\r'
		print "asian_disability: ",asian_disability, '\r'
		print "asian_male: ",asian_male, '\r'
		print "asian_female: ",asian_female, '\r'

		jsonFile.close()
	except IOError:
	   print 'Oh dear. File:',fileName,' not found.'
# End jsonReporter

def dataMean(data, count):
	meanValue = 0
	#print data," / ", count

	meanValue = data / count
	return meanValue
#end dataMean

#remving objects from json string
def jsonStrip():
	fileName = 'data/oasp.json'
	fileName2 = 'data/msaRaw.json'

	try:
		with open(fileName) as jsonGetData:
			j = json.load(jsonGetData)

			for dataAdd in j['features']:
				del dataAdd['properties']['asian_pop']
				del dataAdd['properties']['hawaiian_pop']

				if(dataAdd['properties']['metro_area'] == "Abilene"):
					print dataAdd['properties']
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass
#end jsonStrip


#jsonReporter()
jsonStrip()