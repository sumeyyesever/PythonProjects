import requests
from flight_data import FlightData
import os

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/"
KIWI_KEY = os.environ["KIWI_KEY"]


class FlightSearch:

    def send_iata(self, city_name):
        headers = {
            "apikey": KIWI_KEY
        }
        params = {
            "term": city_name
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}locations/query", params=params, headers=headers)
        data = response.json()
        data_list = data["locations"]
        return data_list[0]["code"]

    def search_price(self, origin_city_code, destination_city_code, from_time, to_time):
        search_endpoint = f"{KIWI_ENDPOINT}v2/search"

        headers = {
            "apikey": KIWI_KEY
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        try:
            response = requests.get(url=search_endpoint, headers=headers, params=params)
            data = response.json()["data"][0]
        except IndexError:
            params["max_stopovers"] = 2
            try:
                response = requests.get(url=search_endpoint, headers=headers, params=params)
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0]
                )
                flight_data.via_city = data["route"][0]["cityTo"]
                flight_data.stop_overs = 1
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
