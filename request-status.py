#!/usr/bin/python

import requests
import time

while True:
    #r = requests.get('http://insights-status-insights-qa.1b13.insights.openshiftapps.com/status')
    r = requests.get('http://www.google.com')
    print(r.status_code)
    time.sleep(60)
