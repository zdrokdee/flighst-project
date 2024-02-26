import requests

SHEETY_ENDPOINT = "https://api.sheety.co/c8d7eac3873c70bcaaf445e26c4d6cb6/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            responce = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(responce.text)

