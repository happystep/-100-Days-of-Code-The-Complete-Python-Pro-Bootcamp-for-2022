import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = 'PUTYOURS'


class FlightSearch:
    def __init__(self):
        self.city_codes = {}

    def get_destination_codes(self,city_names):
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        for city in city_names:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            data = response.json()
            city_code = data["locations"][0]['code']
            self.city_codes[city] = city_code
        return self.city_codes

    @staticmethod
    def check_flights(origin_city_code, destination_city_code, from_time, to_time):
        print(f"Check flights triggered for {destination_city_code}")
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": 2,
            "selected_cabins": "M",
            "adult_hold_bag": "1,1",
            "max_stopovers": 0,
            "curr": 'PUTYOURS'
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        try:
            data = response.json()["data"][0]

            flight_data = FlightData(
                bags_price=data["bags_price"]["1"],
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                airline_go=data["route"][0]["airline"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                airline_back=data["route"][1]["airline"],
                routes=data["routes"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: ₪{flight_data.price}")
            return flight_data
        except IndexError:
            print("No flights were found.")
