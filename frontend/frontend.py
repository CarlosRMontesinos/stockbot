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
import htmlSite

# Get data from DB

# Look for tockens and replace
WEB_SITE = htmlSite.BOOTSTRAP_WEB_SITE
UPDATED_WEB_SITE = string.replace(WEB_SITE, "Date:", "Date: ???")


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

# -------------- Serve Web-Site -----------------

class RestHandler(webapp2.RequestHandler):
    def get(self):

        # Web-site from local file    
        #self.response.write( UPDATED_WEB_SITE ) # Plain HTML
        self.response.write( htmlSite.BOOTSTRAP_WEB_SITE ) # Bootstrap
        
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