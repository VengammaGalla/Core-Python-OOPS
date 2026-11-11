class Cab:
    def __init__(self,d,v):
        self.d=d
        self.v=v
    def calc(self,d,v):
        m=0
        if v=="bike":
            m=34+(d*4)
        elif v=="auto":
            m=50+(d*10)
        elif v=="car":
            m=60+(d*20)
        else:
            m=70+(d*30)
        return m

class Uber(Cab):
    def __init__(self,n,a):
        self.name=n
        self.age=a
        self.v_booked=None
        self.d=0

    def menu(self):
        print("bike 60rs+tax")
        print("auto 120rs+tax")
        print("car 200rs+tax")

    def booking(self):
        self.menu()
        print("1.bike 2.auto 3.car")
        user=input("choose the vehicle")
        self.v_booked="bike" if user==1 else "auto" if user==2 else "car"
        self.d=int(input("enter the distance travel in km:"))
        self.billing()

    def billing(self):
        bill=self.calc(self.d,self.v_booked)
        bill+=(bill*0.1)

        if bill>1000:
            bill-=(bill*0.15)
        print(f"your bill {bill} rs")

class Ola(Cab):
    def __init__(self,n,a):
        self.name=n
        self.age=a
        self.v_booked=None
        self.d=0

    def menu(self):
        print("bike 60rs+tax")
        print("auto 120rs+tax")
        print("car 200rs+tax")

    def booking(self):
        self.menu()
        print("1.bike 2.auto 3.car")
        user=input("choose the vehicle")
        self.v_booked="bike" if user==1 else "auto" if user==2 else "car"
        self.d=int(input("enter the distance travel in km:"))
        self.billing()

    def billing(self):
        bill=self.calc(self.d,self.v_booked)
        bill+=(bill*0.1)
        if bill>1000:
            bill-=(bill*0.15)
        print(f"your bill {bill} rs")

u=int(input("1 uber 2 ola enter your choice:"))
if u==1:
    u=Uber("x",21)
    u.booking()
if u==2:
    u=Ola("x",21)
    u.booking()
