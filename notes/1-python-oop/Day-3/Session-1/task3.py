'''
### ⚡ Micro Task 3 (5 min)

Create this hierarchy:
- `Vehicle` (class variable: `count = 0`, `vehicle_type = "unknown"`)
- `Car(Vehicle)` (class variable: `count = 0`, `vehicle_type = "car"`, `max_passengers = 5`)
- `Truck(Vehicle)` (class variable: `count = 0`, `vehicle_type = "truck"`, `max_passengers = 3`)

Each `__init__` should increment its own class count using `self.__class__.count += 1`.

Create 3 cars and 2 trucks. Verify:
- `Car.count` is 3
- `Truck.count` is 2
- `Vehicle.count` is 0
- `Car.vehicle_type` is "car"
- A car object's `max_passengers` is 5
'''

class Vehicle:
    count = 0
    vehicle_type = "unknown"
    def __init__(self):
        self.__class__.count += 1

class Car(Vehicle):
    count = 0
    vehicle_type = 'car'
    max_passengers = 5
    def __init__(self):
        self.__class__.count += 1

class Truck(Vehicle):
    count = 0
    vehicle_type = "truck"
    max_passengers = 3
    def __init__(self):
        self.__class__.count += 1


if __name__ == "__main__":

    # Reset counts before testing (in case of multiple runs)
    Vehicle.count = 0
    Car.count = 0
    Truck.count = 0

    # Create 3 cars and 2 trucks
    car1 = Car()
    car2 = Car()
    car3 = Car()
    truck1 = Truck()
    truck2 = Truck()

    # Test 1: Car.count is 3
    try:
        assert Car.count == 3, f"Expected 3, got {Car.count}"
        print("Test 1 passed: Car.count is 3")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")

    # Test 2: Truck.count is 2
    try:
        assert Truck.count == 2, f"Expected 2, got {Truck.count}"
        print("Test 2 passed: Truck.count is 2")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")

    # Test 3: Vehicle.count is 0
    try:
        assert Vehicle.count == 0, f"Expected 0, got {Vehicle.count}"
        print("Test 3 passed: Vehicle.count is 0")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")

    # Test 4: Car.vehicle_type is "car"
    try:
        assert Car.vehicle_type == "car", f"Expected 'car', got '{Car.vehicle_type}'"
        print("Test 4 passed: Car.vehicle_type is 'car'")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")

    # Test 5: Car instance max_passengers is 5
    try:
        assert car1.max_passengers == 5, f"Expected 5, got {car1.max_passengers}"
        print("Test 5 passed: Car max_passengers is 5")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")

    # Test 6: Truck.max_passengers is 3 — WILL FAIL
    try:
        assert Truck.max_passengers == 3, f"Expected 3, got {Truck.max_passengers}"
        print("Test 6 passed: Truck max_passengers is 3")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")

    # Test 7: Truck instance max_passengers is 3 — WILL FAIL
    try:
        assert truck1.max_passengers == 3, f"Expected 3, got {truck1.max_passengers}"
        print("Test 7 passed: Truck instance max_passengers is 3")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")

    print("\nAll tests completed!")