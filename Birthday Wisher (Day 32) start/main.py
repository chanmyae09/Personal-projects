import smtplib
import datetime as dt
import random
from shlex import quote

#
# my_email = "pythont292@gmail.com"
# password= "weteyrklfefckyqk"
#
# with  smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email , password =password )
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pythont292@yahoo.com",
#         msg = "Hello")

#
# now = dt.datetime.now()
# year=now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year =2002 ,month = 9 , day=9 )
# print(date_of_birth)

now = dt.datetime.now()
day_of_week = now.weekday()
my_email = "pythont292@gmail.com"
password= "weteyrklfefckyqk"

if day_of_week == 1:
    with open(file = "quotes.txt") as file:
        lines = file.readlines()
        quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs = "aungc@whitman.edu",
            msg = quote
        )


