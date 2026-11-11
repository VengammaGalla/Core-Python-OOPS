def send_email(message):
    print("Sending Email:", message)

def send_sms(message):
    print("Sending SMS:", message)

def send_push(message):
    print("Sending Push Notification:", message)

notification_type = input("Enter notification type: ")

if notification_type == "email":
    send_email("Hello")

elif notification_type == "sms":
    send_sms("Hello")

elif notification_type == "push":
    send_push("Hello")

else:
    print("Invalid notification")





#USING ABSTRACTION

from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailSender(Notifier):

    def send(self, message):
        print("Sending Email:", message)

class SMSSender(Notifier):

    def send(self, message):
        print("Sending SMS:", message)

class PushSender(Notifier):

    def send(self, message):
        print("Sending Push Notification:", message)

def notify(sender, message):
    sender.send(message)

email = EmailSender()
sms = SMSSender()
push = PushSender()

notify(email, "Hello")
notify(sms, "Hello")
notify(push, "Hello")