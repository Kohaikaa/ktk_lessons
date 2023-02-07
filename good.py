class Good():
    name:   str
    price:  int
    cost:   float
    weight: float

    def __init__(self, name, price, weight) -> None:
        self.name = name
        self.price = price
        self.weight = weight
        self.calc()

    def calc(self) -> None:
        self.cost = self.price * self.weight

    def __str__(self) -> str:
        return f"{self.name} costs {self.cost} for {self.weight} KG"
