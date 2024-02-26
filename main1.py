from FlightSearch import FlightSearch
from da_man import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager


flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_CODE = "WAW"

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(destination["lowestPrice"])
    # if flight < destination["lowestPrice"]:
    #     notification.send_notification(
    #         message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
    #                 f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to "
    #                 f"{flight.return_date}.")

