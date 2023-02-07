from cat import *
from good import *
from car import *


def task1():
    cat = Cat()
    cat.name = "Poker"
    cat.color = "Black"
    cat.age = 3
    print(f"{cat.meow()}\n{cat.purring()}\n{cat.piss_in_sneakers()}")


def task2():
    cat = Cat()
    cat.name = "Poker"
    cat.color = "Black"
    cat.age = 3
    print(f"{cat.meow()}\n{cat.purring()}\n{cat.piss_in_sneakers()}")

    apple = Good('apple', price=100, weight=1.5)
    pear = Good('pear', price=120, weight=0.8)
    print(apple)
    print(pear)


def task3():
    car = Car("Black", "BMW", "Lada Sidan Baklajan", 135.0, "I dunno")
    print(car.start())
    print(car.turn("left"))
    print(car.speed_up(150))
    print(car.speed_down(50))
    print(car.beep())
    print(car.stop())
    print('\n'*2)

    truck = Car("Green", "Samsung", "Ded", 75.0, "Kinda Sorda box")
    print(truck.start())
    print(truck.turn("straight"))
    print(truck.speed_up(12))
    print(truck.speed_down(12))
    print(truck.beep())
    print(truck.stop())


if __name__ == "__main__":
    pass
