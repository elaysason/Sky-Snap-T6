from datetime import timedelta, datetime
from faker import Faker
import requests
import os

from .launches_types import LaunchData


import random

fake = Faker()

def generate_fake_launch_data(id=None) -> LaunchData:
    start_date = fake.date_time_this_decade(before_now=True, after_now=False)
    duration = timedelta(hours=random.randint(1, 24))
    end_date = start_date + duration
    start_location_x = random.uniform(-180, 180)
    start_location_y = random.uniform(-90, 90)
    end_location_x = random.uniform(-180, 180)
    end_location_y = random.uniform(-90, 90)
    distance = ((end_location_x - start_location_x) ** 2 + (end_location_y - start_location_y) ** 2) ** 0.5
    
    return LaunchData(
        launch_id=id if id is not None else random.randint(1, 1000),
        casualty_id=random.randint(1, 100),
        type_id=random.randint(1, 10),
        is_red_side=fake.boolean(),
        start_date=start_date,
        end_date=end_date,
        start_location_x=start_location_x,
        start_location_y=start_location_y,
        end_location_x=end_location_x,
        end_location_y=end_location_y,
        was_intercepted=fake.boolean(),
        rocket_type=random.randint(1, 3),
        time=duration,
        speed=distance / duration.total_seconds(),
        distance=distance
    )

DATA_ENDPOINT = os.getenv("DATA_ENDPOINT", "http://localhost:5050/api")

def get_launches():
    # send list of 10 fake launch data
    # return [generate_fake_launch_data() for _ in range(10)]
    url = f"{DATA_ENDPOINT}/getAll"
    response = requests.get(url, params={"table_name": "launch"})
    data = (response.json())['data']
    # Map the data from the server to LaunchData objects
    launches = [
        LaunchData(
            launch_id=item['launch_id'],
            casualty_id=item['casualty_id'],
            type_id=item['type_id'],
            is_red_side=item['is_red_side'],
            start_date=datetime.strptime(item['start_date'], '%a, %d %b %Y %H:%M:%S %Z'),
            end_date=datetime.strptime(item['end_date'], '%a, %d %b %Y %H:%M:%S %Z'),
            start_location_x=float(item['start_location_x']),
            start_location_y=float(item['start_location_y']),
            end_location_x=float(item['end_location_x']),
            end_location_y=float(item['end_location_y']),
            was_intercepted=item['was_intercepted'],
            speed=0,
            distance=0,
            time=timedelta(hours=0),
        ) for item in data
    ]

    return launches

def get_columns(for_pe, coll, col2, _000):
    url = f"{API_BASE_URL}/columns?for_pe={for_pe}&coll={coll}&col2={col2}&_000={_000}"
    response = requests.get(url)
    return response.json()

def get_launch_by_id(id):
    # send fake launch data with the given id
    return generate_fake_launch_data(id)
    url = f"{API_BASE_URL}/launches/{tao_n}"
    response = requests.get(url)
    return response.json()

def get_launches_by_rocket_type(rocket_type):
    launches = get_launches()
    return [launch for launch in launches if launch.rocket_type == rocket_type]

def get_launches_by_date_range(start_date, end_date):
    launches = get_launches()
    return [launch for launch in launches if start_date <= launch.start_date <= end_date]