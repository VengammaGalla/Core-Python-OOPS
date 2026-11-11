from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perform_duty(self):
        pass


class MedicalStaff(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def perform_duty(self):
        print("Medical staff helps patients")


class Doctor(MedicalStaff):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.specialization = specialization

    def perform_duty(self):
        print("Doctor examines patients")


class Surgeon(Doctor):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary, specialization)
        self.__patient_notes = "Confidential"

    def perform_duty(self):
        print("Surgeon performs operations")


people = [
    MedicalStaff("Ravi", 30000),
    Doctor("Sita", 60000, "Cardiology"),
    Surgeon("Rani", 90000, "Surgery")
]

for person in people:
    person.perform_duty()