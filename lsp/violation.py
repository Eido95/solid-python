# LSP: The Liskov Substitution Principle

# (2017) A software artifact should be open for extension but
# closed for modification.

# (2002) If for each object o1 of type S there is anobject o2 of type T,
# such that for all programs P defined in terms of T,
# the behavior of P is unchanged when o1 is substituted for o2,
# then S is a subtype of T.

# (2000) Subclasses should be substitutable for their base classes.

# Simplified: Objects in a program should be replaceable with instances of
# their subtypes without altering the correctness of that program.

# Simplified: If a class Child is subtype of class Parent, then objects of
# type Parent should be easily substituted with objects of
# type Child without needing to change the program.


class Car:
    def __init__(self, type_):
        self.type = type_


class PetrolCar(Car):
    pass


car = Car("sport")
car.properties = {'color': 'red', 'capacity': 6}

petrol_car = PetrolCar("passenger")
petrol_car.properties = ('blue', 4)

cars = [car, petrol_car]


def find_red_cars(cars_):
    red_cars = 0
    for car_ in cars_:
        if car_.properties['color'] == 'red':
            red_cars += 1
            print('red cars:', red_cars)


find_red_cars(cars)
