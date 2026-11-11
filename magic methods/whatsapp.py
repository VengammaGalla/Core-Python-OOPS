class WhatsApp:
    usernames = {}

    def __init__(self, name, username, age, gender, psd):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd
        self.contacts = []
        self.groups = []
        self.logged = False

        WhatsApp.usernames[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")

        while True:
            username = input("Enter your username: ")

            if username in WhatsApp.usernames.keys():
                print("Username already registered try another one")
                continue

            break

        psd = input("Enter Your Password: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender(Male/Female): ")

        return cls(name, username, age, gender, psd)

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

    def add_contact(self, user):
        if self.logged:
            if user not in self.contacts:
                self.contacts.append(user)
                print("Contact added successfully")
            else:
                print("Contact already exists")
        else:
            print("Not logged in")

    def remove_contact(self, user):
        if self.logged:
            if user in self.contacts:
                self.contacts.remove(user)
                print("Contact removed successfully")
            else:
                print("Contact not Found")
        else:
            print("Not logged in")

    def create_group(self, user):
        if self.logged:
            if user not in self.groups:
                self.groups.append(user)
                print("User added to group")
            else:
                print("User already in group")
        else:
            print("Not logged in")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Contacts : {len(self.contacts)}")
        print(f"Groups : {len(self.groups)}")

    def contacts_profile(self):
        if self.logged:
            for i, j in enumerate(self.contacts):
                print(f"{i} : {j.name}")

            l = int(input("Enter your choice: "))
            self.contacts[l].profile()
        else:
            print("Not logged in")


# Creating users

w1 = WhatsApp.signup()
w2 = WhatsApp.signup()
w3 = WhatsApp.signup()
# w4 = WhatsApp.signup()

w1.login()

w1.add_contact(w2)
w1.add_contact(w3)
# w1.add_contact(w4)

w1.create_group(w2)
w1.create_group(w3)

w1.profile()
w1.contacts_profile()

w2.remove_contact(w1)
w3.add_contact(w2)
w3.contacts_profile()