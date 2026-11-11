class MobileRecharge:

    def recharge_plans(self):
        print("1. ₹199 - 1.5GB/day")
        print("2. ₹299 - 2GB/day")
        print("3. ₹399 - 2.5GB/day")

    def mobile_recharge(self):
        number = input("Enter mobile number: ")

        self.recharge_plans()

        plan = int(input("Choose recharge plan: "))

        if plan == 1:
            print("Recharge successful - ₹199")
        elif plan == 2:
            print("Recharge successful - ₹299")
        elif plan == 3:
            print("Recharge successful - ₹399")
        else:
            print("Invalid plan")


class BusTicketBooking:

    def display_buses(self):
        print("1. Hyderabad to Chennai - ₹500")
        print("2. Hyderabad to Bangalore - ₹600")
        print("3. Hyderabad to Vijayawada - ₹300")

    def book_ticket(self):
        self.display_buses()

        bus = int(input("Choose bus: "))

        if bus == 1:
            print("Bus ticket booked - ₹500")
        elif bus == 2:
            print("Bus ticket booked - ₹600")
        elif bus == 3:
            print("Bus ticket booked - ₹300")
        else:
            print("Invalid bus")


class ElectricityBills:

    def bill_details(self):
        print("Electricity Bill Payment")

    def pay_bill(self):
        self.bill_details()

        amount = int(input("Enter bill amount: "))

        print("Electricity bill paid - ₹", amount)


class Paytm(MobileRecharge, BusTicketBooking, ElectricityBills):

    def menu(self):
        print("\n----- PAYTM -----")
        print("1. Mobile Recharge")
        print("2. Bus Ticket Booking")
        print("3. Electricity Bill Payment")
        print("4. Exit")

    def services(self):

        while True:

            self.menu()

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.mobile_recharge()

            elif choice == 2:
                self.book_ticket()

            elif choice == 3:
                self.pay_bill()

            elif choice == 4:
                print("Thank you for using Paytm")
                break

            else:
                print("Invalid choice")


p = Paytm()
p.services()