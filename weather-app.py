import requests

def get_weather(city):
    api_key = 'your_api_key'  # Zde vložte svůj API klíč z OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"The weather in {city} is {weather}. The temperature is {temperature}°C.")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter the city: ")
    get_weather(city)
