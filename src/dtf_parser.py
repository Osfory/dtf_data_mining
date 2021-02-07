from pathlib import Path
import json
import requests
import pandas as pd
import csv


class ConfigLoader:
    @staticmethod
    def load():
        script_path = Path(__file__).parents[1].absolute()
        with open(str(script_path) + "/config.json") as json_file:
            return json.load(json_file)


config = ConfigLoader.load()

# headers = {'User-Agent': config['user_agent'], "X-Device-Token": config['api']['token']}

# api_url = 'https://api.dtf.ru/v1.8/subsite/261696'
#
# response = requests.get(api_url, params = headers)
# print(response.status_code)
# print(response.json())
