#!/usr/bin/python3
import requests
import wget

date_choice = input("What date would you like to pick? Enter in YYYY-MM-DD format:\n ")

quality_choice = input("Enter 1 for High Definition, 2 for Standard Definition:\n ")

# concatenates API URL

api_url = f"https://api.nasa.gov/planetary/apod?date={date_choice}&api_key=MY_API KEY"

r = requests.get(api_url)

json_result = r.json()

pic_date = json_result.get("date")

pic_title = json_result.get("title")

pic_description = json_result.get("explanation")

sd_url = json_result.get("url")

hd_url = json_result.get("hdurl")

# output to user
print(f"The title of the picture is {pic_title}, from {pic_date}, and it says: {pic_description}")

# getting the picture using wget
if quality_choice.strip() == "1":
    wget.download(hd_url)
    print("Check your folder, a high definition pic has been downloaded")
else:
    wget.download(sd_url)
    print("A standard definition pic has been downloaded")


