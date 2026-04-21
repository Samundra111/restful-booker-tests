class ContactPage:
    def __init__(self,page):
        self.page=page
        self.Name_field=page.locator('#name')
        self.Email_field=page.locator('#email')
        self.Phone_field=page.locator('#phone')
        self.Subject_field=page.locator('#subject')
        self.Description_field=page.locator('#description')
        # This finds the button ONLY inside the contact form div
        self.submit_button = page.locator("#contact").locator("button:has-text('Submit')")
        self.success_message = page.get_by_role("heading", name="Thanks for getting in touch")
    def goto(self):
        self.page.goto("https://automationintesting.online/")
    def goto_contact(self):
        self.page.goto("https://automationintesting.online/#contact")
    
    def fill_form(self,Name_field,Email_field,Phone_field,Subject_field,Description_field):
        self.Name_field.fill(Name_field)
        self.Email_field.fill(Email_field)
        self.Phone_field.fill(Phone_field)
        self.Subject_field.fill(Subject_field)
        self.Description_field.fill(Description_field)
        self.submit_button.click()
    
    

    
        
    