import requests
from datetime import datetime
from datetime import datetime
import pytz
import re
import json

from summarize import giveQuery, my_api_key, query_openai

def cleanString(str):
    cleaned_string = re.sub('\s+', ' ', str.replace("\n", " ")).strip()
    return cleaned_string
def logger(user_name):

    url = 'https://remembrall-cd7db0135b38.herokuapp.com/user/' + user_name
    r1 = requests.get(url)
    headers = {'Content-Type': 'application/json'}
    my_json = r1.json()
    response = json.loads(my_json['user_log_summarization'])
    # print(response)
    eastern = pytz.timezone('America/New_York')
    utc_now = datetime.now(pytz.utc)
    eastern_now = utc_now.astimezone(eastern)
    response.append(str(eastern_now))
    query = giveQuery()
    response.append(cleanString(query_openai(my_api_key, query)))
    # response = ["2024-02-04 04:29:36.796035-05:00", "Keyword: Beautiful morning Summary: Feeling liberated on a beautiful morning."]
    response = json.dumps(response)
    url = url + '/update'
    my_json['user_log_summarization'] = response
    requests.put(url, json = my_json, headers=headers)


logger("Firasat")

