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
from google.appengine.ext import db


# Data base
g_sTicker = "NVDA"

# https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.ext.db
# Data Base Record Definition
# "Ticker":"NVDA",
# "Date":"18-12-2017",
# "DayAvg":190.0,
# "PredDayAvg":190.0,

# oDataPoint = StockData(sTicker="NVDA1")
# oDataPoint.fDayAvg = 180.0
# oDataPoint.fPreDayAvg = 185.0
# oDataPoint.put()

class StockData(db.Model):
	sTicker = db.StringProperty()
	oDateTime = db.DateTimeProperty(auto_now_add=True)
	fPriceOpen = db.FloatProperty()
	fPriceMidDay = db.FloatProperty()
	fPriceClose = db.FloatProperty()
	fDayAvg = db.FloatProperty()
	fPreDayAvg = db.FloatProperty()

##### Print ALL DB for debug #####
##### This code generates a "# StockData is not callable" bellow when we want to create a StockData object
# AllStockData = StockData.all()
# for StockData in AllStockData:
# 	print StockData.sTicker
# 	print StockData.oDateTime
# 	print StockData.fPriceOpen
# 	print StockData.fPriceMidDay
# 	print StockData.fPriceClose
# 	print StockData.fDayAvg
# 	print StockData.fPreDayAvg

g_oStockData = None
g_oPrevStockDataDateTime = datetime.datetime(year=1900, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

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
g_fSimPrice = 100.0
g_fSimPriceMult = 0.0

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
	oCurDateTime = g_getCurDateTime()

	# Creat today's StockData record
	g_createStockDataRec()

	# Check if it is time to get data (open market, mid-day, close market)
	if g_isItTime2Sample(oCurDateTime):
		
		# Sample Data Point
		fDataPoint = g_sampleDataPoint() # -> TO DO: Get real data from service
		print "-------------"
		print fDataPoint
		print "-------------"

		# Push to DB
		g_pushToDb(fDataPoint) # -> TO DO

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
		oCurDate = datetime.datetime.now()

	# Print Time
	print oCurDate

	return oCurDate

def g_createStockDataRec():

	# Global
	global g_oStockData
	global g_oPrevStockDataDateTime
#	global StockData

	# Check if we haven't created a DB record to today
	if g_oStockData == None or g_oStockData.oDateTime.date() != g_oPrevStockDataDateTime.date():
		
		# Create today's DB record
		g_oStockData = StockData(sTicker = g_sTicker)
		g_oStockData.put()

	# Update temp StockData DateTime
	g_oPrevStockDataDateTime = g_oStockData.oDateTime

def g_isItTime2Sample(_oCurTime):

	# Global
	global g_oMarketOpens
	global g_oMarketMidDay
	global g_oMarketCloses
	global g_iDataPointsSampled
	global g_bSimulating

	if _oCurTime.minute == g_oMarketOpens.minute or _oCurTime.minute == g_oMarketMidDay.minute or _oCurTime.minute == g_oMarketCloses.minute:
		return True
	else:
		return False

def g_sampleDataPoint():

	fDataPoint = 0.0

	# Get data point from 
	if g_bSimulating == True:
		fDataPoint = g_getSimDataPoint()
	else:
		print "USE API TO GET STOCK PRICE"

	return fDataPoint

def g_pushToDb(_fDataPoint):

	# Globals
	global g_iDataPointsSampled
	global g_bSimulating
	global g_oStockData

	if g_iDataPointsSampled == 0:
		# Push stock price at open time
		g_oStockData.fPriceOpen = _fDataPoint
	elif g_iDataPointsSampled == 1:
		# Push stock price at mida day
		g_oStockData.fPriceMidDay = _fDataPoint
	elif g_iDataPointsSampled == 2:
		# Push stock price at closing time
		g_oStockData.fPriceClose = _fDataPoint
	else:
		print "In g_pushToDb() -> we should never be here...!!!"

	# Push date to DB
	g_oStockData.put()
	# Keep track of the number of data points sampled
	g_iDataPointsSampled = g_iDataPointsSampled + 1
	 # Reset number of samples

def g_getSimDataPoint():
	
	global g_fSimPriceMult
	global g_fSimPrice

	fSimPrice = g_fSimPrice + g_fSimPriceMult * 50.0 # Adding $50
	g_fSimPriceMult = g_fSimPriceMult + 1.0

	if g_fSimPriceMult == 3.0:
		g_fSimPriceMult = 0.0

	return fSimPrice

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
	global g_oStockData

	# Calculate the average
	g_oStockData.fDayAvg = (g_oStockData.fPriceOpen + g_oStockData.fPriceMidDay + g_oStockData.fPriceClose )/3
	g_oStockData.put()

def g_readyToPredict():

	return True

def g_predictDataPoint():

	print "Predict the future...!!!"

	if g_bSimulating == True:
		g_oStockData.fPreDayAvg = 170.0
		g_oStockData.put()
	else:
		print "Get predicted value using ML"

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