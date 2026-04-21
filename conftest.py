import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL=os.getenv("BASE_URL")
HEADERS={'Accept':'application/json',
         'Content-Type':'application/json'}

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def headers():
    return HEADERS

@pytest.fixture
def get_all_bookings():
    response=requests.get(f"{BASE_URL}/booking",headers=HEADERS)
    return response

@pytest.fixture
def get_single_booking():
    response=requests.get(f"{BASE_URL}/booking/4",headers=HEADERS)
    return response

@pytest.fixture
def auth_token():
    payload={'username':'admin','password':'password123'}
    response=requests.post(f"{BASE_URL}/auth",json=payload,headers=HEADERS)
    return response.json()['token']

@pytest.fixture
def auth_headers(auth_token):
    return{
         'Accept':'application/json',
         'Content-Type':'application/json',
         'Cookie':f'token={auth_token}'
         }

@pytest.fixture
def created_booking_id(base_url,headers):
    payload={
         "firstname": "Test",
        "lastname": "User",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    response=requests.post(f"{base_url}/booking",json=payload,headers=headers)
    return response.json()['bookingid']


    