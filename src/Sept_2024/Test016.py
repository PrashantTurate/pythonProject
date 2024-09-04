class PortalLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "turate.prashant@gmail.com" and self.password == "Pass123":
            print("Login successful")
        else:
            print("Login failed")

email = input("Enter your email address: ")
password = input("Enter your password: ")

obj = PortalLoginPage(email, password)
obj.login_confirm()
