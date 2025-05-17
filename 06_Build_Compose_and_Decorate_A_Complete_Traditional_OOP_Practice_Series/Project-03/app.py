class Car:
    # --- public variable ---
    def __init__(self, brand: str) -> None:
        self.brand = brand  # public variable

    # --- public method ---
    def start(self) -> None:
        print(f"The {self.brand} car has started.")


# ---- student-side: using the class ----
if __name__ == "__main__":
    # create an object of Car
    my_car = Car("Toyota")

    # access public variable
    print("Car Brand:", my_car.brand)

    # call public method
    my_car.start()
