import requests
from datetime import datetime

USERNAME = "sumeyye"
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "English Graph",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minute you worked english today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)

# update the pixel

pixel_update_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"
pixel_update = {
    "quantity": "20"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=header)
# print(response.text)

# delete a pixel

pixel_delete_endpoint = f"{pixel_endpoint}/20231221"

# response = requests.delete(url=pixel_delete_endpoint, headers=header)
# print(response.text)
