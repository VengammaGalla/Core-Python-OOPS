class Bus:

    def sleeper(self):
        return 800

    def semi_sleeper(self):
        return 600

    def ac(self):
        return 1000
class RedBus(Bus):

    def routes(self):
        print("----- REDBUS ROUTES -----")
        print("1. Hyderabad to Chennai")
        print("2. Hyderabad to Bangalore")
        print("3. Hyderabad to Vijayawada")

    def booking(self):
        self.routes()

        bus_type = int(input("Enter bus type (1-Sleeper 2-Semi-Sleeper 3-AC): "))

        if bus_type == 1:
            self.total = self.sleeper()
        elif bus_type == 2:
            self.total = self.semi_sleeper()
        elif bus_type == 3:
            self.total = self.ac()
        else:
            print("Invalid bus type")
            return

        self.billing()

    def billing(self):
        gst = self.total * 10 / 100
        reservation = 30

        final_bill = self.total + gst + reservation

        print("Bus fare:", self.total)
        print("GST:", gst)
        print("Reservation charge:", reservation)
        print("Final Bill:", final_bill)


class AbhiBus(Bus):

    def routes(self):
        print("----- ABHIBUS ROUTES -----")
        print("1. Hyderabad to Chennai")
        print("2. Hyderabad to Bangalore")
        print("3. Hyderabad to Vijayawada")

    def booking(self):
        self.routes()

        bus_type = int(input("Enter bus type (1-Sleeper 2-Semi-Sleeper 3-AC): "))

        if bus_type == 1:
            self.total = self.sleeper()
        elif bus_type == 2:
            self.total = self.semi_sleeper()
        elif bus_type == 3:
            self.total = self.ac()
        else:
            print("Invalid bus type")
            return

        self.billing()

    def billing(self):
        gst = self.total * 10 / 100
        reservation = 20

        final_bill = self.total + gst + reservation

        print("Bus fare:", self.total)
        print("GST:", gst)
        print("Reservation charge:", reservation)
        print("Final Bill:", final_bill)


# Driver Code

print("1. RedBus")
print("2. AbhiBus")

choice = int(input("Choose platform: "))

if choice == 1:
    r = RedBus()
    r.booking()

elif choice == 2:
    a = AbhiBus()
    a.booking()

else:
    print("Invalid choice")