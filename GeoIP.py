import requests
import json

ip = r'1.1.1.1'
url = r'https://extreme-ip-lookup.com/json'

request = requests.get(f"{url}/{ip}")


if request.status_code == 200:
    
    jsonAnswer = request.json()
    
    print(jsonAnswer)












else:
    exit()