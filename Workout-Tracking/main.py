import os
import requests
import datetime
import pprint
from requests.auth import HTTPBasicAuth


API_ID = os.environ.get("ID")
API_KEY = os.environ.get("KEY")
HOST = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET")
SHEET_PASSWORD = os.environ.get("SHEET_PASSWORD")

text = input("Tell me which exercises you did: ")


header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": text,
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 190,
    "age": 45
}


request = requests.post(url=f"{HOST}{ENDPOINT}", json=params, headers=header)




date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")
exercise = request.json()["exercises"][0]["name"].title()
duration = request.json()["exercises"][0]["duration_min"]
calories = request.json()["exercises"][0]["nf_calories"]


json_ = {
    "workout": {
        "date" : date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

header = {
    "Authorization": f"Basic {SHEET_PASSWORD}"
}

sheet = requests.post(url=SHEET_ENDPOINT, json=json_, headers=header)
print(sheet.text)
