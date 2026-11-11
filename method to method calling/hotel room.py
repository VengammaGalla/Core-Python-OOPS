class HotelRoom:
    base_price=1000
    def __init__(self,room_number,nights_booked,guest_name):
        self.room_number=room_number
        self.nights_booked=nights_booked
        self.guest_name=guest_name
    def total_bill(self):
        bill=self.base_price*self.nights_booked
        print("Guest:", self.guest_name)
        print("Room No:", self.room_number)
        print("Total Bill:", bill)
    @classmethod
    def update(cls,np):
        cls.base_price=np
    @staticmethod
    def check(nights):
        if nights>0:
            return "valid"
        else:
            return "not valid"
r1 = HotelRoom(101, 3, "Ravi")
r2 = HotelRoom(102, 5, "Sneha")
r1.total_bill()
r2.total_bill()
HotelRoom.update(1500)
r1.total_bill()
r2.total_bill()
print("3 Nights:", HotelRoom.check(3))
print("-2 Nights:", HotelRoom.check(-2))
