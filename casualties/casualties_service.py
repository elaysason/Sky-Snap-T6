import requests

API_BASE_URL = "https://api_base_url/api"

def get_casualties(id):
    url = f"{API_BASE_URL}/casualties"
    response = requests.get(url)
    
    return response.json()

def get_casualty_by_id(id):
    url = f"{API_BASE_URL}/casualties/{id}"
    response = requests.get(url)

    return response.json()

def get_casualties_by_side():
    url = f"{API_BASE_URL}/casualties/per_side"
    response = requests.get(url)

    return response.json()
