class Service:
    def risky_method(self):
        raise ValueError("Something went wrong")

    def run(self):
        try:
            self.risky_method()
        except ValueError as e:
            print("Handled error:", e)

s = Service()
s.run()