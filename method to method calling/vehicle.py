class Vehicle:
    service_rate=5
    def __init__(self,model,kilometers_run,service_history):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=service_history
    def service_charge(self):
        charge=self.service_rate*self.kilometers_run
        print("Model:", self.model)
        print("Service Charge:", charge)
    @classmethod
    def update(cls,nr):
        cls.service_rate=nr
    @staticmethod
    def eligible(model_year):
        current_year = 2026
        if current_year - model_year <= 15:
            return "Eligible for Service"
        else:
            return "Not Eligible for Service"
v1 = Vehicle("x", 12000, "2 Services")
v2 = Vehicle("y", 20000, "3 Services")

print("Before Updating Service Rate")
v1.service_charge()
v2.service_charge()
Vehicle.update(3)
print(v1.model, "-", Vehicle.eligible(2018))
print(v2.model, "-", Vehicle.eligible(2008))

