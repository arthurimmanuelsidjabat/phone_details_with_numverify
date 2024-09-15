## Phone number details using Phyton and Numverify API
import requests

def get_phone_number_info(number, api_key):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={number}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data
    else:
        return {"error": "Failed to retrieve data", "details": data}

api_key = 'YOUR_API_KEY' # Get it on https://numverify.com
phone_number = 'YOUR_PHONE_NUMBER'  # Example phone number

info = get_phone_number_info(phone_number, api_key)

print("Phone Number Details:")
for key, value in info.items():
    print(f"{key}: {value}")
