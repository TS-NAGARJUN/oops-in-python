class Outer:
    class Inner:
        def show(self):
            print("Inner class method called.")

obj = Outer.Inner()
obj.show()  # Output: Inner class method called.

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = self.Battery()

    def show(self):
        print(f"Laptop: {self.brand} {self.model}")
        self.battery.show()

    class Battery:
        def show(self):
            print("Battery: 6-cell, 5000mAh")

laptop = Laptop("Dell", "XPS 13")
laptop.show()

