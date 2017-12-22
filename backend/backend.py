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
import datetime
import time
import json

# Global Variables
g_bSimulating = True

g_oScheduler = sched.scheduler(time.time, time.sleep)
g_iSampleRateSeconds = 3 #Seconds

# Times to sample stock market (PST)
g_oMarketOpens = datetime.datetime(year=1900, month=1, day=1, hour=6, minute=35, second=0, microsecond=0)
g_oMarketMidDay = datetime.datetime(year=1900, month=1, day=1, hour=9, minute=45, second=0, microsecond=0)
g_oMarketCloses = datetime.datetime(year=1900, month=1, day=1, hour=12, minute=55, second=0, microsecond=0)

# Simulation Variables
g_oSimStartDate = datetime.datetime(year=2017, month=12, day=18, hour=5, minute=00, second=0, microsecond=0)
g_oSimDateTimeDelta = datetime.timedelta(days=0, hours=0, minutes=0, seconds=5700, microseconds=0)
g_iDeltaMult = 0

# Data sample variables
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
	oCurDateTime = g_getCurDateTime() # -> TO DO

	# Check if it is time to get data (open market, mid-day, close market)
	if g_isItTime2Sample(oCurDateTime): # -> TO DO
		
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
		oCurDate = g_getSimDateTime()
	else:
		oCurDate = time.gmtime()

	print oCurDate
	return oCurDate

def g_isItTime2Sample(_oCurTime):

	# Global
	global g_oMarketOpens
	global g_oMarketMidDay
	global g_oMarketCloses
	global g_iDataPointsSampled
	global g_bSimulating

	if g_bSimulating == True:

		if _oCurTime.minute == g_oMarketOpens.minute or _oCurTime.minute == g_oMarketMidDay.minute or _oCurTime.minute == g_oMarketCloses.minute:
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

def g_getSimDateTime():

	# Global
	global g_oSimStartDate
	global g_oSimDateTimeDelta
	global g_iDeltaMult

	# Generate simulated date/time info
	oSimDate = g_oSimStartDate + g_iDeltaMult * g_oSimDateTimeDelta
	g_iDeltaMult = g_iDeltaMult + 1
	
	if g_iDeltaMult == 7:
		g_iDeltaMult = 0

	return oSimDate

#######################################################
### Start Scheduler ###
g_oScheduler.enter(g_iSampleRateSeconds, 1, g_pollingLoop, (g_oScheduler,))
g_oScheduler.run()