from pydantic import BaseModel
import requests

class User(BaseModel):
    firstname:str
    lastname:str
    totalprice:int
    depositpaid:bool
    additionalneeds:str

class UserResponse(BaseModel):
     booking:User

def test_create_booking_validation(base_url, headers):
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
        "additionalneeds": "Breakfast"
    }
    
    response = requests.post(f"{base_url}/booking", json=payload, headers=headers)
    
    validated_data = UserResponse(**response.json())
    
    assert validated_data.booking.firstname == "Jim"
    print(f"Validated user: {validated_data.booking.firstname} {validated_data.booking.lastname}")