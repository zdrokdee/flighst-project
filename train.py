import requests
from datetime import datetime, timedelta
from twilio.rest import Client
from pprint import pprint

TEQUILA_END_POINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = {"apikey": "D_Z4Ol68F-VEyUPf9lRwMfU9foZbeG58"}
end_point = f"{TEQUILA_END_POINT}/search"
presentday = datetime.now()
tomorrow = presentday + timedelta(1)
_days = presentday + timedelta(days=180)


search = {
    "fly_from": "WAW",
    "fly_to": "VCE",
    "date_from": f"{tomorrow.strftime('%d/%m/%Y')}",
    "date_to": f"{_days.strftime('%d/%m/%Y')}",
    "nights_in_dst_from": 3,
    "nights_in_dst_to": 5,
    "curr": "USD",
    "price_to": 100
}
response = requests.get(url=end_point, headers=TEQUILA_API_KEY, params=search)



result = response.json()["data"][0]
print(result)

