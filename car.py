class Car():
    color:          str
    brand:          str
    body:           str
    speed:          float
    transmission:   str
    restrictions:   dict = {
        "truck": 60.0,
        "sedan": 80.0
    }

    def __init__(self, color: str, brand: str, body: str, speed: float, transmission: str) -> None:
        self.color = color.lower()
        self.brand = brand.lower()
        self.body = body.lower()
        self.transmission = transmission
        if not self.__check_speed(speed):
            self.speed = speed
        else:
            self.speed = self.restrictions[self.body]

    def start(self) -> str:
        return "Это мой последний заезд..."

    def stop(self) -> str:
        return "Это был мой последний заезд..."

    def turn(self, side: str) -> str:
        return f"Car is turned to the {side}"

    def speed_up(self, value: float) -> str:
        new_speed = self.speed + value
        if self.__check_speed(new_speed):
            return f"Speed hasn't been changed"

        old_speed = self.speed
        self.speed += value
        return f"Speed has been changed: {old_speed} -> {self.speed}"

    def speed_down(self, value: float) -> str:
        old_speed = self.speed
        self.speed -= value
        return f"Speed has been changed: {old_speed} -> {self.speed}"

    def beep(self) -> str:
        return "Союз нерушимый республик свободных....."

    def __check_speed(self, value: float):
        restr_speed = self.restrictions[self.body]
        if restr_speed < value:
            self.speed = restr_speed
            print(
                f"Скорость превышена! Разрешенная скорость {restr_speed} км/ч. " +
                f"Текущая скорость: {self.speed} км/ч")
            return True
        return False
