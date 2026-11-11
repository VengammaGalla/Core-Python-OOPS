from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()