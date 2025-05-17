class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")


# ---- demo ----
if __name__ == "__main__":
    dog1 = Dog("Buddy", "Golden Retriever")
    dog1.bark()   # Output: Buddy says: Woof! Woof!
