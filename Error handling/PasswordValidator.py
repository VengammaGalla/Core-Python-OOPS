class PasswordValidator:
    def validate(self, password):
        if len(password) < 8:
            raise ValueError("Password must contain at least 8 characters")
        print("Password is valid")

p = PasswordValidator()

try:
    p.validate("abc123")
except ValueError as e:
    print("Error:", e)