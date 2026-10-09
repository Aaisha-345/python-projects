import requests

def get_weather(city_name: str, api_key: str):
    """
    Fetches weather data for a given city using OpenWeatherMap API.
    Handles network errors, invalid cities, and missing keys gracefully.
    """
    # Use metric units for Celsius (change to 'imperial' for Fahrenheit)
    url = f"https://openweathermap.org{city_name}&appid={api_key}&units=metric"
    
    try:
        # 1. Making the HTTP API request
        response = requests.get(url, timeout=10)
        
        # Check for HTTP status errors (e.g., 404, 401)
        response.raise_for_status()
        
        # 2. Parsing structured JSON data
        weather_data = response.json()
        
        # --- KEY INSTRUCTION: Uncomment the line below to inspect raw JSON ---
        # print(weather_data) 
        
        # 3. Extracting required fields only (L1 MVP & L3 Challenge)
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].title()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        country = weather_data["sys"]["country"]
        
        # Displaying data cleanly
        print(f"\n Weather in {city_name.title()}, {country}:")
        print(f"  Temperature: {temp}°C")
        print(f"  Condition: {description}")
        print(f"  Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    # 4. Graceful error handling (L2 Improve)
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f" Error: Could not find the city '{city_name}'. Please check the spelling.")
        elif response.status_code == 401:
            print(" Error: Invalid API Key. Please verify your credentials.")
        else:
            print(f" HTTP Error occurred: {http_err}")
            
    except requests.exceptions.ConnectionError:
        print(" Network Error: Unable to connect to the internet. Please check your connection.")
        
    except requests.exceptions.Timeout:
        print(" Timeout Error: The request timed out. Try again later.")
        
    except KeyError:
        print(" Parsing Error: Expected weather data was missing from the response.")
        
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    # --- KEY INSTRUCTION: Keep API keys private! ---
    # Replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key
    API_KEY = "YOUR_API_KEY_HERE" 
    
    print("--- Simple Weather App ---")
    user_city = input("Enter a city name: ").strip()
    
    if user_city:
        get_weather(user_city, API_KEY)
    else:
        print(" Error: City name cannot be empty.")