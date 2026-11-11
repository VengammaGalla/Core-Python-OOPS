class Snapchat:
    usernames = {}

    def __init__(self, name, username, age, gender, psd):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd
        self.followers = 0
        self.following = 0
        self.friends_list = []
        self.logged = False
        Snapchat.usernames[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your username: ")
            if username in Snapchat.usernames.keys():
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

    def add_friend(self, user):
        if self.logged:
            if user not in self.friends_list:
                self.friends_list.append(user)
                self.following += 1
                user.followers += 1
                print("Friend added successfully")
            else:
                print("User is already your friend")
        else:
            print("Not logged in")

    def remove_friend(self, user):
        if self.logged:
            if user in self.friends_list:
                self.friends_list.remove(user)
                self.following -= 1
                user.followers -= 1
                print("Friend removed successfully")
            else:
                print("User not Found")
        else:
            print("Not logged in")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Friends : {len(self.friends_list)}")
        print(f"Followers : {self.followers}")

    def friends_profile(self):
        if self.logged:
            for i, j in enumerate(self.friends_list):
                print(f"{i} : {j.name}")

            l = int(input("Enter your choice: "))
            self.friends_list[l].profile()
        else:
            print("Not logged in")

s1 = Snapchat.signup()
s2 = Snapchat.signup()
s3 = Snapchat.signup()
s4 = Snapchat.signup()
s1.login()
s1.add_friend(s2)
s1.add_friend(s3)
s1.add_friend(s4)
s1.profile()
s1.friends_profile()
s2.remove_friend(s1)
s3.add_friend(s2)
s3.friends_profile()