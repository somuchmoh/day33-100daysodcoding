# How to get an API using requests library
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# If you want to raise an exception for an error that might occur use 👇
response.raise_for_status()
# and it will raise an error according to the status code

# Get a hold of the JSON data from the API endpoint
data = response.json()
print(data)

# Get a specific key from the JSON data
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)



# Find the sunrise and sunset time for a particular location
from datetime import datetime
parameters = {
    "lat": 12.972442,
    "lng": 77.580643,
    "formatted": 1,
}


new_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
new_response.raise_for_status()
new_data = new_response.json()
sunrise = new_data['results']['sunrise'].split("T")[0].split(":")[0]
sunset = new_data['results']['sunset'].split("T")[0].split(":")[0]
print(f"sunrise is at: {sunrise} and sunset is at: {sunset}")

time_now = datetime.now()
print(time_now.hour)
