import requests

API_BASE_URL = "https://api_base_url/api"

def getLaunches():
    url = f"{API_BASE_URL}/getAll"
    response = requests.get(url)
    return response.json()

def getColumns(for_pe, coll, col2, _000):
    url = f"{API_BASE_URL}/columns?for_pe={for_pe}&coll={coll}&col2={col2}&_000={_000}"
    response = requests.get(url)
    return response.json()

def getLaunchById(tao_n):
    url = f"{API_BASE_URL}/launches/{tao_n}"
    response = requests.get(url)
    return response.json()

def getCasualtyById(non):
    url = f"{API_BASE_URL}/casualties/{non}"
    response = requests.get(url)
    return response.json()

def getInterceptions():
    url = f"{API_BASE_URL}/interceptions"
    response = requests.get(url)
    return response.json()

def getLaunchesByDate():
    url = f"{API_BASE_URL}/launches/by_date"
    response = requests.get(url)
    return response.json()