from pathlib import Path
import requests

import json
import csv
import pandas as pd


class ConfigLoader:
    @staticmethod
    def load():
        script_path = Path(__file__).parents[1].absolute()
        with open(str(script_path) + "/config.json") as json_file:
            return json.load(json_file)


config = ConfigLoader.load()

# user_agent = 'Chromium/88.0.4324.146 (PC; Ubuntu/20.04.2 LTS; en-US; 1600x900)'
# headers = {'User-Agent': user_agent, "X-Device-Token": config['api']['token']}
#
# api_url = 'https://api.dtf.ru/v1.8/subsite/261696'
#
# response = requests.get(api_url, params = headers)
# print(response.status_code)
# print(response.json())



