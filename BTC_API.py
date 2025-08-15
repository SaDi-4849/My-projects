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



#api_key_for_sms = "547736467A5254506A362B2B784A4F716571537976553466716C6C514E5862457632476F473555636479633D"
#url = 'https://api.kavenegar.com/v1/%s/sms/send.json' %api_key_for_sms
def send_sms():
    api = KavenegarAPI('6730375568314B4D3549315061422B5A7A794F59366E413264413353523238597134574E5947624D7544493D')
    params = { 'sender' : '2000660110', 'receptor':'09333406383', 
    'message' :f'Title: {title}'
    '------------------------------------------'
    f'Image URL: {image_url}'
       }
    response = api.sms_send(params)
    print(response)

#while True:
    #try:
        #choice = input("SMS y or n : ")
        #if choice == 'y':
            #send_sms()
            #break
        #else:
            #break

    #except Exception as e :
        #print(f"Error: {e}")
