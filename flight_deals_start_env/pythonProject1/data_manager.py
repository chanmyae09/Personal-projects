import requests

sheet_endpoint = "https://api.sheety.co/6dfe38856b6139bc887888dcd700618e/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.header = {
            "Authorization" : "Basic YXVuZ2M6VEBrZWFjaGlsbDA5"
        }
        self.destination_data2 = []

    def get_sheet_data(self):
        response = requests.get(url=sheet_endpoint,headers = self.header)
        data = response.json()
        self.destination_data=data["prices"]
        return self.destination_data


    def update_destination_codes(self):

        for city in self.destination_data:
            data_for_sheets={
                "price":
                    {
                        "iataCode":city["iataCode"]
                    }
            }
            response = requests.put(url = f"https://api.sheety.co/6dfe38856b6139bc887888dcd700618e/flightDeals/prices/{city["id"]}",
                                    json=data_for_sheets,headers=self.header)
            print(response.text)
