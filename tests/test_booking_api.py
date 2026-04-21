import requests
import pytest

def test_all_booking_status_code(get_all_bookings):
    response_code=get_all_bookings.status_code
    assert response_code==200

def test_invalid_booking_id(base_url,headers):
    response=requests.get(f"{base_url}/booking/1000000",headers=headers)
    assert response.status_code==404

def test_first_user(base_url,headers):
    response=requests.get(f"{base_url}/booking/3",headers=headers)
    assert "firstname" in response.json()

def test_get_all_bookings_not_empty(get_all_bookings):
    data=get_all_bookings.json()
    assert len(data)>0

def test_get_all_bookings_have_bookingids(get_all_bookings):
    data=get_all_bookings.json()
    assert "bookingid" in data[0]

def test_single_booking_status_code(get_single_booking):
    assert get_single_booking.status_code==200


def test_single_booking_totalprice(get_single_booking):
    data=get_single_booking.json()
    assert "totalprice" in data
    assert isinstance(data['totalprice'],int)
def test_single_booking_dates(get_single_booking):
    data=get_single_booking.json()
    assert 'bookingdates' in data
    assert 'checkin' in data['bookingdates']
    assert isinstance(data['bookingdates']['checkin'],str)

def test_single_booking_deposit_paid(get_single_booking):
    data=get_single_booking.json()
    assert "depositpaid" in data
    assert isinstance(data['depositpaid'],bool)