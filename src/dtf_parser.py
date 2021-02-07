import requests
import urllib.request
import json
import csv

import pandas as pd

import time
import functional

api_url = 'https://api.dtf.ru/v1.8/subsite/261696'

user_agent = 'Chromium/88.0.4324.146 (PC; Ubuntu/20.04.2 LTS; en-US; 1600x900)'
headers = {'User-Agent': user_agent}

response = requests.get(api_url, params = headers)
print(response.status_code)
print(response.json())
# print(res.headers['Content-Type'])
# data = response.json()


