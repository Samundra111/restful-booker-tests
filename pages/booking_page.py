class BookingPage:
    def __init__(self,page):
        self.page=page
        self.check_availability_btn=page.get_by_role('button',name='Check Availability')
        self.book_now_btn=page.get_by_role('link',name='Book now').nth(1)
        self.reserve_btn=page.locator('#doReservation')
        self.first_name_input=page.get_by_placeholder('Firstname')
        self.last_name_input=page.get_by_placeholder('Lastname')
        self.email_input=page.get_by_placeholder('Email')
        self.phone_input=page.get_by_placeholder('Phone')
        self.reserve_now_button=page.get_by_role('button',name="Reserve Now")
        self.confirmed_msg=page.get_by_role('heading',name="Booking Confirmed")
        self.return_home=page.get_by_role('link',name="Return home")

    def check_availability(self):
        self.check_availability_btn.scroll_into_view_if_needed()
        self.check_availability_btn.click()
    def book_first_room(self):
        self.book_now_btn.click()
    def reserve_now(self):
        self.reserve_btn.click()
    def complete_reservation(self,fname,lname,email,phone):
        self.first_name_input.fill(fname)
        self.last_name_input.fill(lname)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.reserve_now_button.click()