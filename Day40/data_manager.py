import requests


SHEETY_ENDPOINT_SHEET = 'PUTYOURS'
SHEET_USERS_ENDPOINT = 'PUTYOURS'

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = ''

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT_SHEET)
        data = response.json()
        self.destination_data = data["price"]
        return self.destination_data

    def update_destination_codes(self,city_codes):
        for city_data in self.destination_data:
            city_name = city_data["city"]
            if city_data["city"] in city_codes:
                print(f"Brining the code of,{city_name}")
                new_data = {
                    "price": {
                        "iataCode": city_codes[city_name]
                    }
                }

                response = requests.put(
                    url=f"{SHEETY_ENDPOINT_SHEET}/{city_data['id']}",
                    json=new_data
                    )
                print(response.text)
                print("code has been updated")

    @staticmethod
    def replace_flight(row_id, airline_back,airline_go,bags_price,routes,price,destination_city,out_date,return_date):
        print(f"Brining the code of,{destination_city}")
        new_data = {
            "price": {
                "airLineBack":airline_back,
                "airLineGo":airline_go,
                "bagPrice":bags_price,
                "routes":routes,
                "lowestPrice":price,
                "departureDate":out_date,
                "returnDate":return_date


            }
        }
        response = requests.put(
            url=f"{SHEETY_ENDPOINT_SHEET}/{row_id}",
            json=new_data
        )
        print(response.text)
        print("Flight has been updated.")

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data