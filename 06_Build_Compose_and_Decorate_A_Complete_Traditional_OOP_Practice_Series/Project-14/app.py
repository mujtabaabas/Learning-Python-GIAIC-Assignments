class Employee:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee: {self.name}, Position: {self.position}")


class Department:
    def __init__(self, name: str, employee: Employee):
        self.name = name
        self.employee = employee  # Aggregation: Department references Employee

    def show_employee(self):
        print(f"Department: {self.name}")
        self.employee.display()


# ---- demo ----
if __name__ == "__main__":
    # Create Employee independently
    emp1 = Employee("Alice", "Developer")

    # Pass existing Employee to Department (aggregation)
    dept = Department("IT", emp1)

    dept.show_employee()

    # Employee still exists independently
    print("\nEmployee still accessible independently:")
    emp1.display()
