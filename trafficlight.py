from time import sleep


class TrafficLight:
    colors: dict

    def __init__(self) -> None:
        self.colors = {
            "green": 2.0,
            "yellow": 0.5,
            "red": 1.0
        }

    def switching(self) -> None:
        for i in self.colors:
            print(i)
            sleep(self.colors[i])
