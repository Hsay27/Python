# import csv
# from os import write
#
# data = [["name","age","country"],
#         ["yash","20","india"],
#         ["sanidhya","20","india"],
#         ["lakshay","20","india"]
# ]
#
# with open('data.csv','w',newline="") as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row)
#
# with open('data.csv','r') as file:
#     reader = csv.reader(file)
#     for row in data:
#         print(row)

import requests
def main(city,api_key):
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    final_url = f"{url}q={city}&appid={api_key}&units=metric"
    print(final_url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        data  = response.json()
        
        tempeature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        # feels_like= data["main"]["feels_like"]
        
        print(f"wether in {city} is {data['weather'][0]['description']}")
        print(f"temperature is {tempeature} degree celsius")
        print(f"humidity is {humidity}")
        
    except requests.exceptions.RequestException as e:
        print(f"error fetching weather data:{e}")

api_key = "c886a6625554e8c0656caa021caa2de5"
city=input("enter city name: ")
main(city,api_key)