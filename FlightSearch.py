import requests

from flight_data import FlightData

TEQUILA_END_POINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = {"apikey": "D_Z4Ol68F-VEyUPf9lRwMfU9foZbeG58"}


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_END_POINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=TEQUILA_API_KEY, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        global data
        end_point = f"{TEQUILA_END_POINT}/v2/search"
        search = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=end_point,
            headers=TEQUILA_API_KEY,
            params=search
        )

        try:
            data = response.json()['data'][0]

        except IndexError:
            print(f"No flight for {destination_city_code}")






        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data





