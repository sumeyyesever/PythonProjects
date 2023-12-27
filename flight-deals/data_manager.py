import requests
import os

SHEETY_KEY = os.environ["SHEETY_KEY"]
sheety_endpoint = f"https://api.sheety.co/{SHEETY_KEY}/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.sheet_data = []

    def get_sheet_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def update_sheet_data(self):
        for i in range(0, len(self.sheet_data)):
            update_params = {
                "price": {
                    "iataCode": self.sheet_data[i]["iataCode"]
                }
            }
            update_endpoint = f"{sheety_endpoint}/{self.sheet_data[i]["id"]}"
            response = requests.put(url=update_endpoint, json=update_params)
            print(response.text)
