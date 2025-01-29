import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6dfe38856b6139bc887888dcd700618e/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = "aungc"
        self._password = "T@keachill09"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.header = {
            "Authorization": "Basic YXVuZ2M6VEBrZWFjaGlsbDA5"
        }
        self.destination_data = {}
        self.customer_email = []

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",headers=self.header,
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url = "https://api.sheety.co/6dfe38856b6139bc887888dcd700618e/flightDeals/users",headers = self.header)
        data = response.json()['users']
        for i in data:
            self.customer_email.append(i["whatIsYourEmail?"])

        return self.customer_email


