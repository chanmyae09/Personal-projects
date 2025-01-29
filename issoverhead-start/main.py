import requests
from datetime import datetime
import smtplib
my_email = "pythont292@gmail.com"
password = "T@keachill09"

MY_LAT = 46.065552 # Your latitude
MY_LONG = -118.333641# Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if 0 < abs(iss_latitude - MY_LAT) < 5 and 0 < abs(iss_longitude - MY_LONG) < 5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour>= sunset or time_now.hour <= sunrise:
        return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject: LOOk up \n \n  The ISS is above you in the sky.1"
    )











