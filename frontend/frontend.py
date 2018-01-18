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

import webapp2
import os
import string
from google.appengine.ext.webapp import template

WEB_SITE = """<!doctype html> 
<html> 
  
  <body>  
    <h1 style="width: 100%; text-align: center;" >Josue's Stock Account</h1> 

    <h1 style="width: 100%; text-align: center;" > APPLE </h1>
    <h2 style="width: 100%; text-align: center;" > Quantity: {quatity} </h2>
    <h2 style="width: 100%; text-align: center;" > Last Price: {last_price} </h2>
    <h2 style="width: 100%; text-align: center;" > Current Value: {current_value} </h2> 

  </body>
</html>"""

# Get data from DB

# Look for tockens and replace
UPDATED_WEB_SITE = string.replace(WEB_SITE, "{quatity}", "WE ROCK")
UPDATED_WEB_SITE = string.replace(UPDATED_WEB_SITE, "{last_price}", "WE ROCK")
UPDATED_WEB_SITE = string.replace(UPDATED_WEB_SITE, "{current_value}", "WE ROCK")

"""
	<!-- Developer View -->
    <div class="intro-heading">Ticker</div>
    <div class="intro-lead-in">Date: TBD</div>
    <div class="intro-lead-in">Open Price: TBD</div>
    <div class="intro-lead-in">Day Price: TBD</div>
    <div class="intro-lead-in">Close Price: TBD</div>
    <div class="intro-lead-in">Today's Avg: TBD</div>
    <div class="intro-lead-in">Tomorrow's Avg*: TBD</div>
"""

UPDATE_STRING = "UPDATING...!!!"

class RestHandler(webapp2.RequestHandler):
    def get(self):

        # Web-site from local file    
        self.response.write( UPDATED_WEB_SITE )
        
        # Web-site from Bootstrap
        # print "Calling Main Page"
        # path = os.path.join(os.path.dirname(__file__), 'index.html') 
        # self.response.out.write(template.render(path, {}))

class UpdateHandler(RestHandler):

    print UPDATE_STRING
    
    #def post(self):
    #    print UPDATE_STRING

app = webapp2.WSGIApplication([
    ('/', RestHandler),
    ('/update', UpdateHandler),
], debug=True)