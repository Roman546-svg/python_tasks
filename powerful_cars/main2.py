brand_cars = [
    [{'name': 'Ferrari_F430', 'HP': 483},
     {'name': 'Ferrari_360', 'HP': 395},
     {'name': 'Ferrari_488', 'HP': 661}],
    [{'name': 'Lamborghini_Aventador', 'HP': 690},
     {'name': 'Lamborghini_Gallardo', 'HP': 560}]
]
minimal_hp = 661
def powerful_cars(brand_cars: list, minimal_hp: int) -> list:
    # write your code here
    return [
        [car for car in cars if car['HP'] >= minimal_hp] for cars in brand_cars
    ]
powerful_cars(brand_cars,minimal_hp)