import requests
token_endpoint ="https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFER_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
from datetime import datetime
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = "esj0g747i9Nx2PbSDGQuDQWY0CuIIfAw"
        self._api_secret = "FaQh6QxObFr0UWuf"
        self._token = self._get_new_token()


    def _get_new_token(self):
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url = token_endpoint,data =body,headers = header)
        return response.json()["access_token"]

    def get_destination_code(self,city_name):
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
    def check_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode":origin_city_code,
            "destinationLocationCode":destination_city_code,
            "departureDate":from_time.strftime("%Y-%m-%d"),
            "returnDate":to_time.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop":"true",
            "currencyCode" : "GBP",
            "max": "10"}
        response = requests.get(url = FLIGHT_OFFER_ENDPOINT, headers = headers,params = query)
        return response.json()


