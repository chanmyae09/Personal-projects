#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import date, datetime, timedelta
from flight_data import get_cheapest_flight

Original_location_code = "LON"
data_manager = DataManager()


flight_search=FlightSearch()
sheet_data = data_manager.get_sheet_data()
print(sheet_data)


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"]= flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now()+timedelta(days =1)
six_months_from_today =datetime.now() + timedelta(days = (30*6))





for destination in sheet_data:
    print(f"Getting flights for {destination['city']}.... ")
    flights = flight_search.check_flights(Original_location_code,
                                          destination['iataCode'],
                                          tomorrow, six_months_from_today)
    flight_data = get_cheapest_flight(flights)
    print(f"{destination['city']}: Pound{flight_data.price}")
    if flight_data.pirce < sheet_data['lowestPrice']:
        print(f"The price is lower")


