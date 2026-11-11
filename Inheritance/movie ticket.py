class Movie:
    def _init__(self,m):
        self.movie=m
    def ticket(self,m):
        if m=="lenin":
            return 200
        elif m=="pushpa":
            return 100
        elif m=="leo":
            return 150
        else:
            return 0
class Booking(Movie):
    def movies(self):
        print("available movies")
        print("lenin - 200")
        print("pushpa - 100")
        print("leo - 150")
    def selection(self):
        self.total=0
        self.movies()
        while True:
            movie = input("Enter movie name: ").lower()

            price = self.ticket(movie)

            if price == 0:
                print("Invalid movie")
            else:
                self.total = self.total + price
                print("Ticket booked:", price)

            choice = input("Do you want another ticket? yes/no: ").lower()

            if choice == "no":
                break

        self.billing()

    def billing(self):
        print("Ticket amount:", self.total)
        print("Booking charge: 30")
        print("Total amount:", self.total + 30)

class Customer(Booking):
    pass

c = Customer()
c.selection()