import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from pprint import pprint


dm = DataManager()
sheet_data = dm.get_sheet_data()
print(sheet_data)

# for i in range(0, len(sheet_data)):
#     if sheet_data[i]["iataCode"] == "":
#         city_name = sheet_data[i]["city"]
#         fs = FlightSearch()
#         new_iata = fs.send_iata(city_name)
#         sheet_data[i]["iataCode"] = new_iata
#
#
# dm.sheet_data = sheet_data
# dm.update_sheet_data()

today = datetime.datetime.today() + datetime.timedelta(days=1)
end_day = today + datetime.timedelta(days=6 * 30)
fs = FlightSearch()


for city in sheet_data:

    data = fs.search_price("IST", city["iataCode"], today, end_day)
    try:
        flight_price = data.price
    except AttributeError:
        pass
    else:
        if data.price < city["lowestPrice"]:
            nm = NotificationManager()
            nm.send_notification(price=data.price, origin_city=data.origin_city,
                                 origin_airport=data.origin_airport, destination_city=data.destination_city,
                                 destination_airport=data.destination_airport, from_date=data.out_date,
                                 to_date=data.return_date, via_city=data.via_city)
