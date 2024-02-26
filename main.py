from FlightSearch import FlightSearch
from da_man import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_CODE = "WAW"



tomorrow = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    city_data = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight_search:
        if city_data.price < destination["lowestPrice"]:
            message = (
                       f"Low price alert! Only {city_data.price} to fly "
                       f"from {city_data.origin_city}-{ORIGIN_CITY_CODE} to "
                       f"{destination['city']}-{destination['iataCode']},"
                       f" from {city_data.out_date} to {city_data.return_date}")
            notification.send_notification(message)

    else:
        print("dogo")
