import requests

API_KEY = "cdbe8d92a6ad557a042bd8c83f8786e1"  # Get from https://openweathermap.org/api
city = input("Enter city name: ")

# Construct the URL properly
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url).json()

if response["cod"] == 200:
    print(f"City: {response['name']}")
    print(f"Temperature: {response['main']['temp']}°C")
    print(f"Weather: {response['weather'][0]['description']}")
else:
    print("City not found!")
