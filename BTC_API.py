import requests
import webbrowser
from datetime import datetime, date, timedelta
import json
from kavenegar import *

url = 'https://api.nasa.gov/planetary/apod'
api_key = "JZXjKYRMZjYbUs4nbmcTa2g73eUcuqO17UDsgfvB"

target_date = ""
target_time = "" 

while True:
    input_date = input("Enter the date (YYYY-MM-DD) for the APOD image, or press Enter to get today's image: ").strip()
    if not input_date:
        today = date.today()
        target_date = today.strftime("%Y-%m-%d")
        print(f"Getting today's image ({target_date})...")
        break
    else:
        try:
            
            datetime.strptime(input_date, '%Y-%m-%d')
            target_date = input_date 
            print(f"Getting image for {target_date}...")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e:
            print(f"An unexpected error occurred during date input: {e}")
params = {
    "api_key": api_key,
    "date": target_date 
}
response = requests.get(url, params=params)
response.raise_for_status() 

data = response.json()

title = data.get('title')
date_of_image = data.get("date")
explanation = data.get("explanation")
image_url = data.get("url")

try:
    response = requests.get(url, params=params)
    response.raise_for_status() 

    print("--- NASA APOD ---")
    print("Title: ", title)
    print('Date: ', date_of_image)
    print("Explanation: ", explanation)

    if image_url:
        print("Image URL: ", image_url)

        while True:
            user_input = input("Do you want to open the image? (yes/no): ").strip().lower()
            if user_input == 'yes':
                print("Opening the image in your browser...")
                webbrowser.open(image_url)
                break
            elif user_input == 'no':
                print("Okay, not opening the image.")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    else:
        print("No image URL found for this entry.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


