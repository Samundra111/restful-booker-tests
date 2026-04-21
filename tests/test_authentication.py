import requests

import pytest



    

def test_wrong_credentials(base_url,headers):
    payload={'username':'hello','password':'wrongpassword'}
    response=requests.post(f"{base_url}/auth",json=payload,headers=headers)
    assert response.status_code==200
    data=response.json()
    assert data['reason']=='Bad credentials'
    
def test_missing_credentials(base_url,headers):
    payload={}
    response=requests.post(f"{base_url}/auth",json=payload,headers=headers)
    assert response.status_code==200

def test_create_booking(base_url,headers):
    payload={
        'firstname':'samundra',
        'lastname':'Budhathoki',
        'totalprice':'1200',
        'depositpaid':'false',
        'bookingdates':{
            'checkin':'2026-01-01',
            'checkout':'2026-01-05'
        },
        'additionalneeds':'Breakfast'
    }
    response=requests.post(f"{base_url}/booking",json=payload,headers=headers)
    assert response.status_code==200
    data=response.json()
    assert data['booking']['firstname']=="samundra"
    assert data['booking']['totalprice']==1200
    assert isinstance(data['booking']['depositpaid'],bool)

### testing the put method
def test_update_booking(base_url,auth_headers,created_booking_id):
    update_payload={
        "firstname": "Samundra", 
        "lastname": "User",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    response=requests.put(f"{base_url}/booking/{created_booking_id}"
                          ,json=update_payload,headers=auth_headers)
    assert response.status_code==200
    assert response.json()['firstname']=="Samundra"

## testing the Delete

def test_delete_booking(base_url,auth_headers,created_booking_id):
    response=requests.delete(f"{base_url}/booking/{created_booking_id}",headers=auth_headers)
    assert response.status_code==201
    
    get_response=requests.get(f"{base_url}/booking/{created_booking_id}",headers=auth_headers)
    assert get_response.status_code==404