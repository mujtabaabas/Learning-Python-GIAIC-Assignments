class Student:
    def __init__(self, name: str, marks: float) -> None:
        # the self keyword refers to the current instance
        self.name = name
        self.marks = marks

    def display(self) -> None:
        """Print the student's details."""
        print(f"Student Name : {self.name}")
        print(f"Marks        : {self.marks}")

# --- quick demo ---
if __name__ == "__main__":
    s1 = Student("Ayesha", 87.5)
    s1.display()
