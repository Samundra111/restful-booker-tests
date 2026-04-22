from pages.contact_page import ContactPage
from pages.admin_page import AdminPage
from pages.booking_page import BookingPage
from playwright.sync_api import Page,expect


def test_contact_form(page:Page):
    contact=ContactPage(page)
    contact.goto_contact()
    contact.fill_form("Samundra","sam@gmail.com","00908080808","contact","filled the contact form")
    expect(contact.success_message).to_be_visible()

def test_empty_contact_form(page:Page):
    contact=ContactPage(page)
    contact.goto_contact()
    contact.fill_form("","","","","")
    expect(contact.success_message).not_to_be_visible()

def test_login_admin(page:Page):
    admin=AdminPage(page)
    admin.goto_admin()
    admin.login("admin","password")
    expect(admin.logout_link).to_be_visible()
    expect(admin.messages_link).to_be_visible()
    expect(page).to_have_url("https://automationintesting.online/admin/rooms")

def test_login_admin_wrong_credentials(page: Page):
    admin = AdminPage(page)
    admin.goto_admin()
    admin.login("wrong", "wrong")
    # Should stay on login page
    expect(page).to_have_url(
        "https://automationintesting.online/admin"
    )

def test_admin_logout(page: Page):
    admin = AdminPage(page)
    admin.goto_admin()
    admin.login("admin", "password")
    admin.logout_link.click()
    # Should redirect back to login
    expect(page).to_have_url(
        "https://automationintesting.online/"
    )

def test_end_to_end_booking(page:Page):
    bookingpage=BookingPage(page)
    page.goto("https://automationintesting.online/")
    bookingpage.check_availability()
    bookingpage.book_first_room()
    bookingpage.reserve_now()
    bookingpage.complete_reservation("Sam","hora","sa@gmail.com","9847487457000")
    expect(bookingpage.confirmed_msg).to_be_visible()
    expect(bookingpage.return_home).to_be_visible()

