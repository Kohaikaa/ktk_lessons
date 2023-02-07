class Car():
    color:          str
    brand:          str
    body:           str
    speed:          float
    transmission:   str

    def __init__(self, color: str, brand: str, body: str, speed: float, transmission: str) -> None:
        self.color = color
        self.brand = brand
        self.body = body
        self.speed = speed
        self.transmission = transmission

    def start(self) -> str:
        return "Это мой последний заезд..."

    def stop(self) -> str:
        return "Это был мой последний заезд..."

    def turn(self, side: str) -> str:
        return f"Car is turned to the {side}"

    def speed_up(self, value: float) -> str:
        old_speed = self.speed
        self.speed += value
        return f"Speed has been changed: {old_speed} -> {self.speed}"

    def speed_down(self, value: float) -> str:
        old_speed = self.speed
        self.speed -= value
        return f"Speed has been changed: {old_speed} -> {self.speed}"

    def beep(self) -> str:
        return "Союз нерушимый республик свободных....."
