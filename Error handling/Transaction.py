class Transaction:
    def process(self):
        try:
            print("Processing transaction")
            raise ValueError("Transaction failed")
        except ValueError as e:
            print("Error:", e)
        finally:
            print("Cleanup completed")

t = Transaction()
t.process()