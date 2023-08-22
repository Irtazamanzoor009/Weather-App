import requests
import json

city = input("Enter City Name: ")

url = f"https://api.weatherapi.com/v1/current.json?key=78d424f8cfd049b0be7185342231008&q={city}"

r = requests.get(url)
#print(r.text)

dic = json.loads(r.text)
print("Location: ",dic["location"]["name"])
print("Region: ",dic["location"]["region"])
print("Latitude: ", dic["location"]["lat"])
print("Longitude: ", dic["location"]["lon"])
print("Temperature Celcius: ",dic["current"]["temp_c"])
print("Temperature Farhenheit: ",dic["current"]["temp_f"])