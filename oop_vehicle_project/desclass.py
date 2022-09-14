class Vehicle:
    def __init__(self, color, speed, num_of_gears):
        self.color = color
        self.speed = speed
        self.num_of_gears = num_of_gears
class Car(Vehicle):
    def __init__(self, color, speed, num_of_gears, car_bod):
        super().__init__(color, speed, num_of_gears,)
        self.car_bod = car_bod
class Bike(Vehicle):
    def __init__(self, color, speed, num_of_gears, scope_of_apllication):
        super().__init__(color, speed, num_of_gears,)
        self.scope_of_application = scope_of_apllication
class Bus(Vehicle):
    def __init__(self, color, speed, num_of_gears, num_of_seats):
        super().__init__(color, speed, num_of_gears,)
        self.num_of_seats = num_of_seats
class Truck(Vehicle):
    def __init__(self, color, speed, num_of_gears, height, weight):
        super().__init__(color, speed, num_of_gears,)
        self.height = height
        self.weight = weight
