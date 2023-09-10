from info import API_KEY, BASE_URL
import requests


city = input("Enter a city name: ").lower().capitalize()
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    
    #Getting the variable data
    weather = data["weather"][0]["description"]
    temperature = round(data['main']['temp'])
    expected = round(data['main']['feels_like'])
    min = round(data['main']['temp_min'])
    max = round(data['main']['temp_max'])
    
    print(f'Weather: {weather}')
    print(f"The temperature in {city} is {temperature} Celsius, feels like {expected} Celsius")
    print(f"Expected max,min temperature for today is {max} Celsius, {min} Celsius respectively")
else:
    print(f"Error Code: {response.status_code}")