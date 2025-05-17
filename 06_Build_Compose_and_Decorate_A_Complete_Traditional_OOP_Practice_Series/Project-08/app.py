class Person:
    def __init__(self, name: str):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Teacher(Person):
    def __init__(self, name: str, subject: str):
        # Call the constructor of the base class Person
        super().__init__(name)
        self.subject = subject

    def display(self):
        super().display()  # Call base class display
        print(f"Subject: {self.subject}")


# ---- demo ----
if __name__ == "__main__":
    t = Teacher("Mrs. Khan", "Mathematics")
    t.display()
