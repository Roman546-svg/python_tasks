import desclass
car = desclass.Car('red', 160, 5, 'SVN')
bus = desclass.Bus('blue', 80, 4, 30)
bike = desclass.Bike('gray', 99, 3, 'mountain')
truck = desclass.Truck('black', 100, 5, 15, 1000)
print(car.__dict__)
print(bus.__dict__)
print(bike.__dict__)
print(truck.__dict__)

