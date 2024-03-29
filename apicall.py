import requests
import json

url = 'https://distanceto.p.rapidapi.com/distance/route'
headers = {
    'content-type': 'application/json',
    'X-RapidAPI-Key': 'd208f5389cmsh6a4b1158e36ff89p1a1d74jsnd1533208c1a9',
    'X-RapidAPI-Host': 'distanceto.p.rapidapi.com'
}
data = {
    "route": [
        {
            "country": "SA",
            "name": "Riyadh"
        },
        {
            "country": "SA",
            "name": "Jeddah"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

try:
    response.raise_for_status()
    # Get the full response data
    response_data = response.json()
    # Extract just the 'route' portion
    route = response_data.get('route', {})
    print(json.dumps(route, indent=2))
except requests.exceptions.HTTPError as err:
    print(err)


