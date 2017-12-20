# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import webapp2
import sched # Scheduler
import time
import json

# Global Variables

g_bSimulating = False

g_oScheduler = sched.scheduler(time.time, time.sleep)
g_iSampleRateSeconds = 3
g_oSimMarketOpens = time.strptime("Wed, 13 Dec 2017 21:00:00", "%a, %d %b %Y %H:%M:%S")
g_oSimMarketMidDay = time.strptime("Wed, 13 Dec 2017 21:20:00", "%a, %d %b %Y %H:%M:%S")
g_oSimMarketCloses = time.strptime("Wed, 13 Dec 2017 21:40:00", "%a, %d %b %Y %H:%M:%S")
g_iMin = 0
g_oSimDate = time.strptime("Wed, 13 Dec 2017 21:" + str(g_iMin) + ":00", "%a, %d %b %Y %H:%M:%S")

DATA_POINTS_NEEDED = 3
g_iDataPointsSampled = 0

g_dicTestDbRecord = {"Ticker":"NVDA",
					"Date":"18-12-2017",
					"Samples":[
								{"Time":"","Price":190.0},
								{"Time":"","Price":190.0},
								{"Time":"","Price":190.0}
								],
					"DayAvg":190.0,
					"Prediction+1":{
									"ModelType":"Extrapolation",
									"PredDayAvg":190.0,
									"Error":0.0
									}
					}
#######################################################

### Running Polling Loop ###
def g_pollingLoop(_oScheduler): 
	
	# Get current date
	oCurDate = g_getCurDateTime()

	# Check if it is time to get data (open market, mid-day, close market)
	if g_isItTime2Sample(oCurDate): # -> TO DO
		
		# Sample Data
		g_sampleDataPoint() # -> TO DO

		# IF Enough Data Samples
		if g_gotEnoughSamples(): # -> TO DO

			# Operate on data collected
			g_operateOnSamples() # -> TO DO

			# IF we have a model ready
			if g_readyToPredict(): # -> TO DO

				# Apply model and predict
				g_predictDataPoint() # -> TO DO

			# ELSE continue
		# ELSE continue	
	# ELSE continue


	# Call PollingLoop again and for ever    
	g_oScheduler.enter(g_iSampleRateSeconds, 1, g_pollingLoop, (_oScheduler,))


def g_getCurDateTime():

	# Global
	global g_bSimulating

	if g_bSimulating == True:
		oCurDate = g_getSimDate()
	else:
		oCurDate = time.gmtime()

	print time.strftime("%Y-%m-%d %H:%M:%S", oCurDate)
	return oCurDate

def g_isItTime2Sample(_oCurTime):

	# Global
	global g_oSimMarketOpens
	global g_oSimMarketMidDay
	global g_oSimMarketCloses
	global g_iDataPointsSampled
	global g_bSimulating

	if g_bSimulating == True:

		if _oCurTime.tm_min == g_oSimMarketOpens.tm_min or _oCurTime.tm_min == g_oSimMarketMidDay.tm_min or _oCurTime.tm_min == g_oSimMarketCloses.tm_min:
			g_iDataPointsSampled = g_iDataPointsSampled + 1 # Keep track of the number of data points sampled
			return True
		else:
			return False
		
	else:
		print "Not simulating in: g_isItTime2Sample()"
		return False

def g_sampleDataPoint():

	print "Sample Data Point"

def g_gotEnoughSamples():

	# Global
	global g_iDataPointsSampled
	global DATA_POINTS_NEEDED

	if g_iDataPointsSampled == DATA_POINTS_NEEDED:
		g_iDataPointsSampled = 0 # Reset number of samples
		return True
	else:
		return False

def g_operateOnSamples():

	# Global
	global g_sTestDbRecord

	#print "Operate on data collected"
	jTestDbRecord = json.dumps(g_dicTestDbRecord)
	oTestDbRecord = json.loads(jTestDbRecord)
	#print "Ticker: " + oTestDbRecord["Ticker"] + " $" + str(oTestDbRecord["DayAvg"])

def g_readyToPredict():

	return True

def g_predictDataPoint():

	print "Predict the future...!!!"

def g_getSimDate():

	# Global
	global g_iMin

	# Generate simulated date/time info
	oSimDate = time.strptime("Wed, 13 Dec 2017 21:" + str(g_iMin) + ":00", "%a, %d %b %Y %H:%M:%S")
	g_iMin = g_iMin + 10
	if g_iMin == 60:
		g_iMin = 0

	return oSimDate

#######################################################
### Start Scheduler ###
g_oScheduler.enter(g_iSampleRateSeconds, 1, g_pollingLoop, (g_oScheduler,))
g_oScheduler.run()