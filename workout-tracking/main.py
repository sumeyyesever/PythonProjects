import requests
from datetime import datetime
import os

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_KEY = os.environ["SHEETY_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
nutri_params = {
     "query": input("tell me which exercises you did? ")
}
response = requests.post(url=exercise_endpoint, headers=nutri_headers, json=nutri_params)
data = response.json()


sheety_endpoint = f"https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts"
bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
exercises_length = len(data["exercises"])
today = datetime.now()

for i in range(0, exercises_length):
    exercise_name = data["exercises"][i]["name"].title()
    exercise_duration = data["exercises"][i]["duration_min"]
    exercise_calories = data["exercises"][i]["nf_calories"]

    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=bearer_headers)
    print(sheety_response.status_code)
    print(sheety_response.text)
