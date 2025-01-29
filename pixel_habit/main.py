import requests
from datetime import datetime

USERNAME = "charlesmdy1"
TOKEN = "hsdfsdfsdfsdfsd"
GRAPH_ID = "graph2"
date = datetime(year = 2024,month =12,day = 10).strftime("%Y%m%d")

pixel_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "hsdfsdfsdfsdfsd",
    "username": "charlesmdy1",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response1 = requests.post(url = pixela_endpoint,json=user_params)


graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name": "Cycling Graph",
    "unit":"Km",
    "type": "float",
    "color": "ajisai"
}
headers ={
    "X-USER-TOKEN": TOKEN
}

# response2 = requests.post(url = graph_endpoint,json = graph_config,headers = headers)
# print(response2.text)

pixel_creation_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# print(date.strftime("%Y%m%d"))


pixel_data ={
    "date": "20241210",
    "quantity": "2.5"
}

# response3 = requests.post(url = pixel_creation_endpoint,json =pixel_data,headers=headers)
# print(response3.text)


update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# pixel_update_data ={
#     "quantity": "5.5"
# }
#
# response4=requests.put(url=pixel_update_endpoint,json = pixel_update_data,headers=headers)
# print(response4.text)

delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
response4 = requests.put(url = delete_endpoint, headers = headers)
print(response4.text)

