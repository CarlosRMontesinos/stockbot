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

g_iSampleRateSeconds = 3

### Adding a scheduler ###
import sched, time
g_oScheduler = sched.scheduler(time.time, time.sleep)
#######################################################


### Running Polling Loop ###
def g_pollingLoop(_oScheduler): 
    
    # Check if it is the time of day to sample stock price (open market, mid-day, close market)
	print "Run PollingLoop"
    	#IF (open market, mid-day, close market)
    	if True:
    		# Sample Data
    		print "Sample Data Point"
    		# IF Enough Data Samples
    		if True:
    			print "Check for Model"
    			# IF Model
    			if True:
    				print "Predict"
    			# ELSE continue
    		# ELSE continue	
		# ELSE continue
	# Call PollingLoop again and for ever    
	g_oScheduler.enter(g_iSampleRateSeconds, 1, g_pollingLoop, (_oScheduler,))


#######################################################
### Start Scheduler ###
g_oScheduler.enter(g_iSampleRateSeconds, 1, g_pollingLoop, (g_oScheduler,))
g_oScheduler.run()