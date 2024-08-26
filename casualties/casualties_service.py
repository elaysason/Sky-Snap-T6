import os
import requests
from casualties.casualties_types import CasualtyData


DATA_ENDPOINT = os.getenv("DATA_ENDPOINT", "http://localhost:5000/api")

def casualties():
    url = f"{DATA_ENDPOINT}/getAll"
    response = requests.get(url, params={"table_name": "casualty"})
    data = (response.json())['data']

    # Map the data from the server to LaunchData objects
    casualties = [
        CasualtyData(
            casualty_id=int(item["casualty_id"]),
            mortal_injured=int(item["mortal_injured"]),
            hard_injured=int(item["hard_injured"]),
            medium_injured=int(item["medium_injured"]),
            easy_injured=int(item["easy_injured"]),
            death_count=int(item["death_count"]),
        ) for item in data
    ]

    return casualties

def casualty_by_id(id):
    url = f"{DATA_ENDPOINT}/getCasualtyById"
    response = requests.get(url, params={"id": id})
    
    if 'data' not in response.json():
        return None
    data = (response.json())['data']

    # Map the data from the server to LaunchData objects
    casualty = CasualtyData(
            casualty_id=int(data["casualty_id"]),
            mortal_injured=int(data["mortal_injured"]),
            hard_injured=int(data["hard_injured"]),
            medium_injured=int(data["medium_injured"]),
            easy_injured=int(data["easy_injured"]),
            death_count=int(data["death_count"]),
        )

    return casualty

def casualties_by_side():
    url = f"{DATA_ENDPOINT}/casualties/per_side"
    response = requests.get(url)

    return response.json()
