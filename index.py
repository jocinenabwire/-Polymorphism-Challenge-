# -Polymorphism-Challenge-
# Base class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}")
        print(f"Battery life: {self.battery_life} hours")

    def use_phone(self, hours):
        if hours <= self.battery_life:
            self.battery_life -= hours
            print(f"Used phone for {hours} hours. Remaining battery: {self.battery_life} hours.")
        else:
            print("Not enough battery!")

# Subclass
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, heart_rate_monitor=True):
        super().__init__(brand, model, battery_life)
        self.heart_rate_monitor = heart_rate_monitor

    def display_info(self):
        super().display_info()
        print(f"Heart Rate Monitor: {'Yes' if self.heart_rate_monitor else 'No'}")

# Create objects
phone = Smartphone("Apple", "iPhone 14", 20)
watch = Smartwatch("Samsung", "Galaxy Watch 5", 24)

# Use the objects
phone.display_info()
phone.use_phone(5)

print("\nSmartwatch Info:")
watch.display_info()


# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Call the move method on each object
vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move()
