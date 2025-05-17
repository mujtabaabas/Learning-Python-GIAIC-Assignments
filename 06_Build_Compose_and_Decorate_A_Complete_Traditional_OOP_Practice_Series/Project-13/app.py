class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")


class Car:
    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine  # Composition: Car HAS-A Engine

    def start_car(self):
        print(f"Starting the {self.brand} car...")
        self.engine.start()  # Accessing Engine’s method via Car


# ---- demo ----
if __name__ == "__main__":
    my_engine = Engine(150)
    my_car = Car("Honda", my_engine)

    my_car.start_car()
