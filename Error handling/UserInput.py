class UserInput:
    def get_integer(self, value):
        try:
            number = int(value)
            print("Integer:", number)
        except ValueError:
            print("Error: Invalid integer value")
        except TypeError:
            print("Error: Value cannot be converted to integer")

u = UserInput()

u.get_integer("123")
u.get_integer("hello")
u.get_integer(None)