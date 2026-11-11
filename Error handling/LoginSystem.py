class LoginSystem:
    def login(self, password):
        if password != "python123":
            raise ValueError("Incorrect password")
        print("Login successful")

login_system = LoginSystem()

try:
    login_system.login("")
except ValueError as e:
    print("Login error:", e)