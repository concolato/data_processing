#!/usr/bin/python
# -*- coding: utf-8 -*-

#To turn on VirtualEnv
# $ source bin/activate
# https://virtualenv.pypa.io/en/latest/userguide.html

import pprint, json, time
#import _mysql
#import sys

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

#Does not work ... yet
def fibinacci(start):
	myList=[]	
	#multiply by golden ration to get next number
	myList=[start + i * 1.61803398874989484820458683436563811772030917 for i in range(10)]

	return myList
#end fibinacci

#removing objects from json string
def jsonStrip():
	fileName = 'data/oasp.json'
	fileName2 = 'data/threads/Both.json'

	try:
		with open(fileName) as jsonGetData:
			j = json.load(jsonGetData)

			for dataAdd in j['features']:
				del dataAdd['properties']['aapi_pop']
				del dataAdd['properties']['both_age_18_24_raw']
				del dataAdd['properties']['both_lang_prof_raw']
				del dataAdd['properties']['both_age_25_54_raw']
				del dataAdd['properties']['both_age_55_over_raw']				
				del dataAdd['properties']['both_edu_less_than_high_raw']
				del dataAdd['properties']['both_edu_high_ged_raw']
				del dataAdd['properties']['both_edu_some_college_raw']
				del dataAdd['properties']['both_edu_college_higher_raw']
				del dataAdd['properties']['both_disability_raw']				
				del dataAdd['properties']['both_male_raw']
				del dataAdd['properties']['both_female_raw']
				del dataAdd['properties']['both_age_18_24']
				del dataAdd['properties']['both_lang_prof']
				del dataAdd['properties']['both_age_25_54']
				del dataAdd['properties']['both_age_55_over']				
				del dataAdd['properties']['both_edu_less_than_high']
				del dataAdd['properties']['both_edu_high_ged']
				del dataAdd['properties']['both_edu_some_college']
				del dataAdd['properties']['both_edu_college_higher']
				del dataAdd['properties']['both_disability']				
				del dataAdd['properties']['both_male']
				del dataAdd['properties']['both_female']
				del dataAdd['properties']['both_poverty']
				del dataAdd['properties']['both_unemployment']

				del dataAdd['properties']['asian_pop']
				del dataAdd['properties']['asian_age_18_24_raw']
				del dataAdd['properties']['asian_lang_prof_raw']
				del dataAdd['properties']['asian_age_25_54_raw']
				del dataAdd['properties']['asian_age_55_over_raw']				
				del dataAdd['properties']['asian_edu_less_than_high_raw']
				del dataAdd['properties']['asian_edu_high_ged_raw']
				del dataAdd['properties']['asian_edu_some_college_raw']
				del dataAdd['properties']['asian_edu_college_higher_raw']
				del dataAdd['properties']['asian_disability_raw']				
				del dataAdd['properties']['asian_male_raw']
				del dataAdd['properties']['asian_female_raw']
				del dataAdd['properties']['asian_age_18_24']
				del dataAdd['properties']['asian_lang_prof']
				del dataAdd['properties']['asian_age_25_54']
				del dataAdd['properties']['asian_age_55_over']				
				del dataAdd['properties']['asian_edu_less_than_high']
				del dataAdd['properties']['asian_edu_high_ged']
				del dataAdd['properties']['asian_edu_some_college']
				del dataAdd['properties']['asian_edu_college_higher']
				del dataAdd['properties']['asian_disability']				
				del dataAdd['properties']['asian_male']
				del dataAdd['properties']['asian_female']
				del dataAdd['properties']['asian_poverty']
				del dataAdd['properties']['asian_unemployment']

				del dataAdd['properties']['hawaiian_pop']
				del dataAdd['properties']['hawaiian_age_18_24_raw']
				del dataAdd['properties']['hawaiian_lang_prof_raw']
				del dataAdd['properties']['hawaiian_age_25_54_raw']
				del dataAdd['properties']['hawaiian_age_55_over_raw']				
				del dataAdd['properties']['hawaiian_edu_less_than_high_raw']
				del dataAdd['properties']['hawaiian_edu_high_ged_raw']
				del dataAdd['properties']['hawaiian_edu_some_college_raw']
				del dataAdd['properties']['hawaiian_edu_college_higher_raw']
				del dataAdd['properties']['hawaiian_disability_raw']				
				del dataAdd['properties']['hawaiian_male_raw']
				del dataAdd['properties']['hawaiian_female_raw']
				del dataAdd['properties']['hawaiian_age_18_24']
				del dataAdd['properties']['hawaiian_lang_prof']
				del dataAdd['properties']['hawaiian_age_25_54']
				del dataAdd['properties']['hawaiian_age_55_over']				
				del dataAdd['properties']['hawaiian_edu_less_than_high']
				del dataAdd['properties']['hawaiian_edu_high_ged']
				del dataAdd['properties']['hawaiian_edu_some_college']
				del dataAdd['properties']['hawaiian_edu_college_higher']
				del dataAdd['properties']['hawaiian_disability']				
				del dataAdd['properties']['hawaiian_male']
				del dataAdd['properties']['hawaiian_female']
				del dataAdd['properties']['hawaiian_unemployment']
				del dataAdd['properties']['hawaiian_poverty']
				
				del dataAdd['properties']['hispanic_age_18_24']
				del dataAdd['properties']['hispanic_lang_prof']
				del dataAdd['properties']['hispanic_age_25_54']
				del dataAdd['properties']['hispanic_age_55_over']				
				del dataAdd['properties']['hispanic_edu_less_than_high']
				del dataAdd['properties']['hispanic_edu_high_ged']
				del dataAdd['properties']['hispanic_edu_some_college']
				del dataAdd['properties']['hispanic_edu_college_higher']
				del dataAdd['properties']['hispanic_disability']				
				del dataAdd['properties']['hispanic_male']
				del dataAdd['properties']['hispanic_female']
				del dataAdd['properties']['hispanic_unemployment']
				del dataAdd['properties']['hispanic_poverty']
				
				del dataAdd['properties']['black_age_18_24']
				del dataAdd['properties']['black_lang_prof']
				del dataAdd['properties']['black_age_25_54']
				del dataAdd['properties']['black_age_55_over']				
				del dataAdd['properties']['black_edu_less_than_high']
				del dataAdd['properties']['black_edu_high_ged']
				del dataAdd['properties']['black_edu_some_college']
				del dataAdd['properties']['black_edu_college_higher']
				del dataAdd['properties']['black_disability']				
				del dataAdd['properties']['black_male']
				del dataAdd['properties']['black_female']
				del dataAdd['properties']['black_unemployment']
				del dataAdd['properties']['black_poverty']

				del dataAdd['properties']['asian_indian']
				del dataAdd['properties']['Bangladeshi']
				del dataAdd['properties']['Bhutanese']
				del dataAdd['properties']['Burmese']				
				del dataAdd['properties']['Cambodian']
				del dataAdd['properties']['Chinese']
				del dataAdd['properties']['Filipino']
				del dataAdd['properties']['Hmong']
				del dataAdd['properties']['Indonesian']				
				del dataAdd['properties']['Japanese']
				del dataAdd['properties']['Korean']
				del dataAdd['properties']['Laotian']
				del dataAdd['properties']['Malaysian']
				del dataAdd['properties']['Mongolian']
				del dataAdd['properties']['Nepalese']
				del dataAdd['properties']['Okinawan']
				del dataAdd['properties']['Pakistani']				
				del dataAdd['properties']['Sri_Lankan']
				del dataAdd['properties']['Taiwanese']
				del dataAdd['properties']['Thai']
				del dataAdd['properties']['Vietnamese']
				del dataAdd['properties']['Other_Asian']

				del dataAdd['properties']['comprehensive_count']
				del dataAdd['properties']['one_stop_count']				
				del dataAdd['properties']['affiliate_count']
				del dataAdd['properties']['enforcement_count']
				del dataAdd['properties']['osha_count']
				del dataAdd['properties']['ofccp_count']
				del dataAdd['properties']['job_center_count']
				del dataAdd['properties']['job_corp_count']
				del dataAdd['properties']['ebsa_count']
				del dataAdd['properties']['whd_count']

				#if(dataAdd['properties']['metro_area'] == "Abilene"):
					#print dataAdd['properties']

			print j
			filePutData(j, fileName2)

			try:
				with open(fileName2): #verify file is there
					checkFile = open(fileName2, "r")			
					contents = checkFile.read()

					valid = is_json(contents) #verify this is json

					#if not contents:
					if(valid == 0):
						print "error"
					else:
						print fileName2," processed."
						return 1
						#print contents
			except Exception, e:
				print e," ",fileName2
				raise
			else:
				pass
			finally:
				pass
			#end 
	except Exception, e:
		print e
		raise
	else:
		pass
	finally:
		pass
#end jsonStrip

# String demographic
# Appends data from one JSON file to new data file
def jsonGeoBuild(demographic):
	source = 'data/oasp_dev.json' #using this version bc it has the dummy data

	if demographic == 'both':
		newFile = 'data/threads/Both.json'
		totalPop = 'aapi_pop'
	elif demographic == 'asian':
		newFile = 'data/threads/Asian.json'
		totalPop = 'asian_pop'
	elif demographic == 'hawaiian':
		newFile = 'data/threads/Pacific.json'
		totalPop = 'hawaiian_pop'
	elif demographic == 'hispanic':
		newFile = 'data/threads/Hispanic.json'
		totalPop = 'hispanic_pop'
	elif demographic == 'black':
		newFile = 'data/threads/Black.json'
		totalPop = 'black_pop'

	age_18_24_raw = demographic+'_age_18_24_raw' #concatinate to make dynamic
	age_18_24 = demographic+'_age_18_24'
	age_25_54_raw = demographic+'_age_25_54_raw'
	age_25_54 = demographic+'_age_25_54'
	age_55_over_raw = demographic+'_age_55_over_raw'
	age_55_over = demographic+'_age_55_over'
	disability_raw = demographic+'_disability_raw'
	disability = demographic+'_disability'
	edu_college_higher_raw = demographic+'_edu_college_higher_raw'
	edu_college_higher = demographic+'_edu_college_higher'
	edu_high_ged_raw = demographic+'_edu_high_ged_raw'
	edu_high_ged = demographic+'_edu_high_ged'
	edu_less_than_high_raw = demographic+'_edu_less_than_high_raw'
	edu_less_than_high = demographic+'_edu_less_than_high'
	edu_some_college_raw = demographic+'_edu_some_college_raw'
	edu_some_college = demographic+'_edu_some_college'
	female_raw = demographic+'_female_raw'
	female = demographic+'_female'
	male_raw = demographic+'_male_raw'
	male = demographic+'_male'
	lang_prof_raw = demographic+'_lang_prof_raw'
	lang_prof = demographic+'_lang_prof'
	poverty = demographic+'_poverty'
	unemployment = demographic+'_unemployment'

	jX = returnJson(source)
	jY = returnJson(newFile)

	for dataL1 in jY['features']: #traverse the stripped down file		
		for dataL2 in jX['features']: # then grab data values according to geography
			
			#This acts as a unique identifyer since some MSAs have the same name
			if dataL1['properties']['metro_area'] == dataL2['properties']['metro_area'] and dataL1['properties']['stusps'] == dataL2['properties']['stusps']:
				dataL1['properties'][totalPop] = dataL2['properties'][totalPop]
				dataL1['properties'][age_18_24_raw] = dataL2['properties'][age_18_24_raw]
				dataL1['properties'][age_18_24] = dataL2['properties'][age_18_24]
				dataL1['properties'][age_25_54_raw] = dataL2['properties'][age_25_54_raw]
				dataL1['properties'][age_25_54] = dataL2['properties'][age_25_54]
				dataL1['properties'][age_55_over_raw] = dataL2['properties'][age_55_over_raw]
				dataL1['properties'][age_55_over] = dataL2['properties'][age_55_over]
				dataL1['properties'][disability_raw] = dataL2['properties'][disability_raw]
				dataL1['properties'][disability] = dataL2['properties'][disability]
				dataL1['properties'][edu_college_higher_raw] = dataL2['properties'][edu_college_higher_raw]
				dataL1['properties'][edu_college_higher] = dataL2['properties'][edu_college_higher]

				dataL1['properties'][edu_high_ged_raw] = dataL2['properties'][edu_high_ged_raw]
				dataL1['properties'][edu_high_ged] = dataL2['properties'][edu_high_ged]
				dataL1['properties'][edu_less_than_high_raw] = dataL2['properties'][edu_less_than_high_raw]
				dataL1['properties'][edu_less_than_high] = dataL2['properties'][edu_less_than_high]
				dataL1['properties'][edu_some_college_raw] = dataL2['properties'][edu_some_college_raw]
				dataL1['properties'][edu_some_college] = dataL2['properties'][edu_some_college]
				dataL1['properties'][female_raw] = dataL2['properties'][female_raw]
				dataL1['properties'][female] = dataL2['properties'][female]
				dataL1['properties'][male_raw] = dataL2['properties'][male_raw]
				dataL1['properties'][male] = dataL2['properties'][male]

				dataL1['properties'][lang_prof_raw] = dataL2['properties'][lang_prof_raw]
				dataL1['properties'][lang_prof] = dataL2['properties'][lang_prof]
				dataL1['properties'][poverty] = dataL2['properties'][poverty]
				dataL1['properties'][unemployment] = dataL2['properties'][unemployment]

				#These are the same for every file
				dataL1['properties']['comprehensive_count'] = dataL2['properties']['comprehensive_count']
				dataL1['properties']['one_stop_count']	=	dataL2['properties']['one_stop_count']		
				dataL1['properties']['affiliate_count'] = dataL2['properties']['affiliate_count']
				dataL1['properties']['enforcement_count'] = dataL2['properties']['enforcement_count']
				dataL1['properties']['osha_count'] = dataL2['properties']['osha_count']
				dataL1['properties']['ofccp_count'] = dataL2['properties']['ofccp_count']
				dataL1['properties']['job_center_count'] = dataL2['properties']['job_center_count']
				dataL1['properties']['job_corp_count'] = dataL2['properties']['job_corp_count']
				dataL1['properties']['ebsa_count'] = dataL2['properties']['ebsa_count']
				dataL1['properties']['whd_count'] = dataL2['properties']['whd_count']

	print jY
	filePutData(jY, newFile)
	
#end jsonGeoBuild

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

def jsonFilterByType():
	fileName = 'data/oshaReginalAndWhdDistrictOffices.json'
	
	newFileJobCorps = 'data/threads/JobCorps.json'
	newFileComp = 'data/threads/Comp.json'
	newFileAffiliate = 'data/threads/Affiliate.json'
	newFileOsha = 'data/threads/Osha.json'
	newFileWHD = 'data/threads/WHD.json'
	newFileOfccp = 'data/threads/Ofccp.json'
	newFileEBSA = 'data/threads/EBSA.json'

	newJsonObj_JobCorps = []
	newJsonObj_Comp = []
	newJsonObj_Affiliate = []
	newJsonObj_Osha = []
	newJsonObj_WHD = []
	newJsonObj_Ofccp = []
	newJsonObj_EBSA = []

	try:
	   with open(fileName) as jsonFile: # Open and verify file is there
	   	# load JSON object into memory
		j = json.load(jsonFile)

		for dataL1 in j:			
			if dataL1['TYPE'] == "Job Corps Center":
				#print dataL1['Street_Address']
				newJsonObj_JobCorps.append(dataL1)

			elif dataL1['TYPE'] == "Affiliate Job Center":
				newJsonObj_Affiliate.append(dataL1)

			elif dataL1['TYPE'] == "Comprehensive Job Center":
				newJsonObj_Comp.append(dataL1)

			elif dataL1['TYPE'] == "OSHA Area Office":
				newJsonObj_Osha.append(dataL1)

			elif dataL1['TYPE'] == "OFCCP Area Office" or dataL1['TYPE'] == "OFCCP Regional Office" or dataL1['TYPE'] == 'OFCCP Regional/District Office':
				newJsonObj_Ofccp.append(dataL1)

			elif dataL1['TYPE'] == "WHD District Office":
				newJsonObj_WHD.append(dataL1)

			elif dataL1['TYPE'] == "EBSA Regional Office" or dataL1['TYPE'] == 'EBSA Regional/District Office':
				newJsonObj_EBSA.append(dataL1)
		
		#print newJsonObj_JobCorps

		filePutData(newJsonObj_Affiliate, newFileAffiliate)
		filePutData(newJsonObj_JobCorps, newFileJobCorps)
		filePutData(newJsonObj_Comp, newFileComp)
		filePutData(newJsonObj_Osha, newFileOsha)
		filePutData(newJsonObj_Ofccp, newFileOfccp)
		filePutData(newJsonObj_WHD, newFileWHD)
		filePutData(newJsonObj_EBSA, newFileEBSA)

	except Exception, e:
		print e
		raise
#end jsonSortByType

def filePutData(data, filename):
	if data:
		new_data = str(json.dumps(data))
		filePut = open(filename, 'w+')
		#add data
		if is_json(new_data) == 1:
			filePut.write(new_data)
			filePut.close()

		print "Data for ", filename, " processed."
		return 1
	else:
		print "There is no data for ", filename
		return 0

#end filePutData

def is_json(myjson):
	try:
		json_object = json.loads(myjson)
		return 1
	except ValueError, e:
		print 'No valid JSON.'
		return 0

	return 1
#end is_json

#An experiment in moving data from one file to another that worked
def testDataTransform():
	source = 'data/threads/testFile2.json' 
	newFile = 'data/threads/testFile1.json'

	jX = returnJson(source)
	jY = returnJson(newFile)

	for dataL1 in jX:
		#print dataL1['city']
		for dataL2 in jY:
			if dataL1['city'] == dataL2['city']:
				dataL2['population'] = dataL1['population']

	for test in jY:
		print test
# end testDataTransform

#jsonReporter()
#jsonStrip()
#jsonFilterByType()
jsonGeoBuild('both')
#testDataTransform()