from pyowm import OWM

owm = OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key
city = input("What city you are interested in:")

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
#lat=22.57 W, lon=43.12S (Rio de Janeiro, BR)

observation_list = mgr.weather_around_coords(-22.57, -43.12)
w= observation.weather
  	

temperature = w.temperature('celsius')['temp']
print(f"Min temperature {w.temperature('celsius')['temp_min']}")
print(f"Max temperature {w.temperature('celsius')['temp_max']}")
print(f"Temperature {w.temperature('celsius')['temp']}")
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print(f"For the coordinates 22.57, 43.12 temperature is{w.temperature('celsius')['temp']}" )