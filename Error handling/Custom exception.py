class InvalidAgeError(Exception):
    pass

class Voter:
    def check_eligibility(self, age):
        if age < 18:
            raise InvalidAgeError("Not eligible to vote")
        print("Eligible to vote")

v = Voter()

try:
    v.check_eligibility(16)
except InvalidAgeError as e:
    print("Error:", e)