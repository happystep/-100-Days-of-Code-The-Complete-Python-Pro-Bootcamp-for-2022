import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="superluis5@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email"
                        )

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
if year == 2022:
    print("Wear a face mask")

date_of_birth = dt.datetime(year=1996, month=4, day=21)
print(date_of_birth)
