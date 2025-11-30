
import requests # type: ignore
import json
API_KEY = "e6c6083509fc4d450cde0ca4414b3a9f"
def get_weather_with_errors(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        data = response.json()
        print(json.dumps(data, indent=4))
        return data
    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid city or API key.")
    except Exception as e:
        print("Unexpected Error:", str(e))
    return None
get_weather_with_errors("Hyderabad")
def get_weather_pretty(city):
    data = get_weather_with_errors(city)
    if data is None:
        return None
    city_name = data["name"]
    temp = data["main"]["temp"]
    hum = data["main"]["humidity"]
    desc = data["weather"][0]["description"].title()
    print(f"City: {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {hum}%")
    print(f"Weather: {desc}")
    return {"city": city_name, "temp": temp, "humidity": hum, "weather": desc}
res = get_weather_pretty("London")
assert "city" in res
assert "temp" in res
assert "weather" in res