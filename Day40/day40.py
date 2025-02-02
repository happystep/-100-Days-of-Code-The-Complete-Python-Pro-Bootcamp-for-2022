# Capstone: Flight Club

from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()


ORIGIN_CITY_IATA = 'PUTYOURS'

city_has_code = True
for city in sheet_data:
    if city["iataCode"] == "":
        city_has_code = False
    if not city_has_code:
        break

if not city_has_code:
    city_names = [city["city"] for city in sheet_data]
    city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes(city_codes)
    sheet_data = data_manager.get_destination_data()



destinations = {
    sheet_data["iataCode"]: {
        "id":sheet_data["id"],
        "city":sheet_data["city"],
        "price":sheet_data["lowestPrice"]
    } for sheet_data in sheet_data}



tomorrow = datetime.now() + timedelta(days=1)

six_month_from_today = datetime.now() + timedelta(days=6 * 30)


for city_code, diction in destinations.items():

    flight = flight_search.check_flights(ORIGIN_CITY_IATA,city_code,tomorrow,six_month_from_today)

    try:

        if flight.price < diction["price"]:

            routes = f"from {str(flight.routes[0][0])} to {str(flight.routes[0][1])},  from {str(flight.routes[1][0])} to {str(flight.routes[1][1])}"

            data_manager.replace_flight(row_id=diction["id"],
                                        airline_back=flight.airline_back,
                                        airline_go=flight.airline_go,
                                        bags_price=flight.bags_price,
                                        routes=routes,
                                        price=flight.price,
                                        destination_city=flight.destination_city,
                                        out_date=flight.out_date,
                                        return_date=flight.return_date)


            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]
            message = f"Low price alert! Only ₪ {flight.price}to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
            link = f"https://www.google.co.il/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            notification_manager.send_emails(emails, message, link)
            notification_manager.send_sms(message)


    except AttributeError:
        continue
