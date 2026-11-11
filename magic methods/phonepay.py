class PhonePe:
    users = {}

    def __init__(self, name, username, age, gender, psd, balance):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd

        self.balance = balance
        self.transactions = []
        self.logged = False

        PhonePe.users[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")

        while True:
            username = input("Enter your username: ")

            if username in PhonePe.users.keys():
                print("Username already registered try another one")
                continue

            break

        psd = input("Enter Your Password: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender(Male/Female): ")
        balance = float(input("Enter your balance: "))

        return cls(name, username, age, gender, psd, balance)

    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your username: ")
            password = input("Enter your password: ")

            if user == self.username and password == self.password:
                self.logged = True
                print("Logged in Successfully")
            else:
                print("Invalid Credentials")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def check_balance(self):
        if self.logged:
            print("Your Balance : ₹", self.balance)
        else:
            print("Not logged in")

    def send_money(self, user, amount):
        if self.logged:
            if amount <= self.balance:
                self.balance -= amount
                user.balance += amount

                self.transactions.append(
                    f"Sent ₹{amount} to {user.name}"
                )

                user.transactions.append(
                    f"Received ₹{amount} from {self.name}"
                )

                print("Money sent successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Not logged in")

    def receive_money(self, amount):
        if self.logged:
            self.balance += amount
            self.transactions.append(
                f"Received ₹{amount}"
            )
            print("Money received successfully")
        else:
            print("Not logged in")

    def show_transactions(self):
        if self.logged:
            if len(self.transactions) == 0:
                print("No transactions")
            else:
                print("Transactions")

                for i, j in enumerate(self.transactions):
                    print(f"{i + 1} : {j}")
        else:
            print("Not logged in")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Balance : ₹{self.balance}")
        print(f"Transactions : {len(self.transactions)}")


# Creating users

p1 = PhonePe.signup()
p2 = PhonePe.signup()

# Login

p1.login()
p2.login()

# Check balance

p1.check_balance()
p2.check_balance()

# Send money

amount = float(input("Enter amount to send: "))
p1.send_money(p2, amount)

# Check balance

p1.check_balance()
p2.check_balance()

# Transactions

p1.show_transactions()
p2.show_transactions()

# Profile

p1.profile()
p2.profile()

# Logout

p1.logout()
p2.logout()