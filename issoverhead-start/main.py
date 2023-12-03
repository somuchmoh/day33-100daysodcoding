import requests
from datetime import datetime
import pytz

MY_LAT = 9.507351 # Your latitude
MY_LONG = 164.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
print(sunrise)
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.now(tz=pytz.utc)
print(time_now.hour)


if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5:
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        print("look up")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



