import smtplib
import datetime as dt
import random

MY_EMAIL="YOUR EMAIL HERE"
PASSWORD="YOUR PASSWORD HERE"
TO_EMAIL = "RECEIVER EMAIL HERE"

with open("quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)
now = dt.datetime.now()
if now.weekday()==0:
    print(now.time())
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="TO_EMAIL",
                            msg=f"subject:Monday Motivation\n\n{quote}")




