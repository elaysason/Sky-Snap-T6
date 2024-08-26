import requests

API_BASE_URL = "https://api_base_url/api"

def getColumns(for_pe, coll, col2, _000):
    url = f"{API_BASE_URL}/columns?for_pe={for_pe}&coll={coll}&col2={col2}&_000={_000}"
    response = requests.get(url)
    return response.json()

def getCasualties(id):
    url = f"{API_BASE_URL}/casualties"
    response = requests.get(url)
    
    return response.json()

def getCasualtyById(id):
    url = f"{API_BASE_URL}/casualties/{id}"
    response = requests.get(url)

    return response.json()

def getCasualtiesBySide():
    url = f"{API_BASE_URL}/casualties/per_side"
    response = requests.get(url)

    return response.json()
