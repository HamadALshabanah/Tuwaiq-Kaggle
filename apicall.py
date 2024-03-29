import requests
import json

url = 'https://distanceto.p.rapidapi.com/distance/route'
headers = {
    'content-type': 'application/json',
    'X-RapidAPI-Key': 'fad0993ce2mshc22086d84151b6cp1d3f9ajsn8bfeaf9b9fcb',
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


