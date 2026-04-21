class AdminPage:
    def __init__(self,page):
       self.page=page
       self.username=page.get_by_placeholder("Enter username")
       self.password=page.get_by_placeholder("Password")
       self.login_btn=page.locator('#doLogin')
       self.logout_link =page.get_by_role("button", name="Logout")
       self.room_list = page.locator(".room-list")
       self.messages_link = page.get_by_role("link", name="Messages")
    def goto_admin(self):
        self.page.goto("https://automationintesting.online/admin")
    
    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
    

