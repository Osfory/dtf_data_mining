import json
import requests
import urllib.request
import pandas as pd
import time


class ConfigLoader:
    @staticmethod
    def load():
        script_path = "YOUR_PATH" # "YOUR_PATH"
        with open(str(script_path) + "/config.json") as json_file:
            return json.load(json_file)


config = ConfigLoader.load()
headers = {"User-Agent": config['user_agent']} #, "X-Device-Token": config['token']}
api_url = 'https://api.dtf.ru/v1.8/subsite/261696/timeline/new?count=50'

request = urllib.request.Request(api_url, None, headers)
response = urllib.request.urlopen(request)
data = response.read()
entry = json.loads(data)

df = pd.DataFrame()

for n in range(150):
    print(api_url + '&offset=' + str(50 * n))
    try:
        response = requests.get((api_url + '&offset=' + str(50 * n)), params=headers)
    except Exception as e:
        print(e)
        if 'Too many requests' in e:
            print('Слишком много запросов, дружок-пирожок. Отдохни немного. \nНомер страницы = {}'.format(n))
            time.sleep(30)
    else:
        df = pd.concat([df, pd.DataFrame(response.json()['result'])], axis=0)

print(df)
print(df.shape)
df.to_csv("YOUR_ANOTHER_PATH")