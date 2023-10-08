import requests
from datetime import datetime, timedelta

api_key = '55d3ce7f471db6d3c8f884a9e8d6ff02'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error fetching weather data')
        return None
    
def printer(weather_data) :
    
    # Extract relevant weather information
    temperature = weather_data['main']['temp']  # in Kelvin
    cloud_cover = weather_data['clouds']['all']  # cloud cover percentage
    wind_speed = weather_data['wind']['speed']  # wind speed in meters per second
    description = weather_data['weather'][0]['description']  # weather description
    lightning_risk = "thunderstorm" in description.lower()  # Check for thunderstorm in description
    print("----------------------------------------------------------------")
    print("| Conditions   |\tNormal\t\t|\tLive Condition\t|")
    print("----------------------------------------------------------------")
    print (f"|Temperature   | ", end=" ")
    print (" 273.15 to 313.15\t|", end=" ")
    if (273.15 < temperature < 313.15):
        print(f'\033[92m \t{temperature}\t\033[0m', end=" ")
        print("\t|")
    else:
        print(f'\033[91m {temperature}\t\033[0m', end=" ")
        print("\t|")
    
    
    print (f"|Cloud Cover   | ", end=" ")
    print (" <10\t\t\t|", end=" ")
    if (cloud_cover<10):
        print(f'\033[92m\t{cloud_cover}\t\033[0m', end=" ")
        print("\t|")
    else:
        print(f'\033[91m\t{cloud_cover}\t\033[0m', end=" ")
        print("\t|")
        
        
    print (f"|Wind Speed    | ", end=" ")
    print (" <9\t\t\t|", end=" ")
    if (wind_speed < 9.0):
        print(f'\033[92m\t{wind_speed}\033[0m', end=" ")
        print("\t\t|")
    else:
        print(f'\033[91m\t{wind_speed}\033[0m', end=" ")
        print("\t\t|")
    
      
    print (f"|Sky           | ", end=" ")
    print (" Clear Sky\t\t|", end=" ")
    skies= "rain" not in description.lower() and "drizzle" not in description.lower()
    if (skies):
        if (len(description)<5) :
            print(f'\033[92m\t{description}\033[0m', end=" ")
            print("\t\t|")
        else :
            print(f'\033[92m\t{description}\033[0m', end=" ")
            print("\t|")
        
    else:
        if (len(description)>5) :
            print(f'\033[91m\t{description}\033[0m', end=" ")
            print("\t|")
        else :
            print(f'\033[91m\t{description}\033[0m', end=" ")
            print("\t|")
            
        
    print (f"|Lightning Risk| ", end=" ")
    print (" No Risk/False\t|", end=" ")
    storm= "thunderstorm" in description.lower()
    if (storm):
        print(f'\033[91m\t{lightning_risk}\033[0m', end=" ")
        print("\t\t|")
    else:
        print(f'\033[92m\t{lightning_risk}\033[0m', end=" ")
        print("\t\t|")
    
    print("----------------------------------------------------------------")
    return

def is_suitable_for_rocket_launch(weather_data):
    if weather_data is None:
        return False

    # Extract relevant weather information
    temperature = weather_data['main']['temp']  # in Kelvin
    cloud_cover = weather_data['clouds']['all']  # cloud cover percentage
    wind_speed = weather_data['wind']['speed']  # wind speed in meters per second
    description = weather_data['weather'][0]['description']  # weather description
    lightning_risk = "thunderstorm" in description.lower()  # Check for thunderstorm in description

    # Define launch criteria
    clear_skies = cloud_cover < 10  # Cloud cover less than 10% for clear skies
    low_wind_speed = wind_speed < 9.0  # Approximately 20 mph or less
    dry_weather = "rain" not in description.lower() and "drizzle" not in description.lower()
    moderate_temperature = 273.15 < temperature < 313.15  # Temperature in Kelvin (0°C to 40°C)
    low_lightning_risk = not lightning_risk
    good_visibility = clear_skies and not lightning_risk

    # Check if conditions are suitable for rocket launch
    return (
        clear_skies and
        low_wind_speed and
        dry_weather and
        moderate_temperature and
        low_lightning_risk and
        good_visibility
    )

def main():
    city = input('Enter city name: ')
    weather_data = get_weather_data(city)
    current_time = datetime.now()
    suitable_time = current_time + timedelta(hours=1)

    if weather_data:
        if is_suitable_for_rocket_launch(weather_data):
            print('\033[92mIdeal conditions for a student rocket launch!\033[0m')
                        
        else:
            print('\033[91mNot ideal conditions for a student rocket launch.\033[0m')
            print(f'\033[92mSuitable conditions expected around: {suitable_time.strftime("%Y-%m-%d,%H:%M:%S")}\033[0m')
    else:
        print('\033[91mUnable to determine weather conditions.\033[0m')
        
    printer(weather_data)
        

if __name__ == "__main__":
    main()
