import requests, os

# Tool: Get weather information
def detect_location_from_ip() -> str:
    """Returns city name based on IP address."""
    try:
        ipinfo_token = os.getenv("IPINFO_TOKEN", None)
        url = "https://ipinfo.io/json"
        if ipinfo_token:
            url += f"?token={ipinfo_token}"

        response = requests.get(url, timeout=3)
        data = response.json()
        return data.get("city", "")
    except Exception as e:
        return ""

def get_weather(city: str = "") -> str:
    """Returns current weather info for a given or detected city."""
    if not city:
        city = detect_location_from_ip()
        if not city:
            return "I couldn't determine your location. Please provide a city name."

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather service is not configured properly, please check your API key."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return f"⚠️ Weather API Error: {data.get('message', 'Unknown error')}"

        if "weather" not in data or "main" not in data:
            return "⚠️ Unexpected response format. Please try again later."

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return (
            f"The weather in {city.title()} is {weather}, "
            f"{temp}°C (feels like {feels_like}°C), "
            f"with {humidity}% humidity."
        )

    except Exception as e:
        return f"Error retrieving weather: {str(e)}"