class SecureFile:

    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__logs = []

    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__logs.append("Unauthorized attempt")
            return "Access denied"


file = SecureFile("My secret data", "1234")

print(file.read("1234"))
print(file.read("9999"))

# Trying to access logs
# print(file.__logs)