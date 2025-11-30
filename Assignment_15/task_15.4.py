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
def fetch_weather(city):
    data = get_weather_with_errors(city)
    if data is None:
        print("Error: City not found. Please enter a valid city.")
        return None
    result = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"].title()
    }
    print(result)
    return result
assert fetch_weather("New York")["city"] == "New York"
assert fetch_weather("xyz123") is None
assert isinstance(fetch_weather("Delhi"), dict)
