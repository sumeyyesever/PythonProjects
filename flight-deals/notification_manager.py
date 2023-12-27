import smtplib
import requests
import os

SHEETY_KEY = os.environ["SHEETY_KEY"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


class NotificationManager:

    def send_notification(self, price, origin_city, origin_airport, destination_city,
                          destination_airport, from_date, to_date, via_city):
        sheety_endpoint = f"https://api.sheety.co/{SHEETY_KEY}/flightDeals/users"
        my_email = "python.sumeyye@gmail.com"
        my_password = MY_PASSWORD
        response = requests.get(url=sheety_endpoint)
        users_data = response.json()["users"]
        for user in users_data:

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                if via_city != "":
                    connection.sendmail(from_addr=my_email, to_addrs=user["email"],
                                        msg=f"Subject: Low Flight Price Alert!\n\n Only {price} Euros to fly from "
                                            f"{origin_city}-{origin_airport} to {destination_city}-{destination_airport}, "
                                            f"from {from_date} to {to_date}\n Flight has 1 stop over via "
                                            f"{via_city}.")
                else:
                    connection.sendmail(from_addr=my_email, to_addrs=user["email"],
                                        msg=f"Subject: Low Flight Price Alert!\n\n Only {price} Euros to fly from "
                                            f"{origin_city}-{origin_airport} to {destination_city}-{destination_airport}, "
                                            f"from {from_date} to {to_date}")

