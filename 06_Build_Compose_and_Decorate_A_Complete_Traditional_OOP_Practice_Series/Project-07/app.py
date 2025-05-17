class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public variable
        self._salary = salary     # protected variable (convention: single underscore)
        self.__ssn = ssn          # private variable (name mangling: double underscore)

    def display_info(self):
        print(f"Name    : {self.name}")
        print(f"Salary  : {self._salary}")
        print(f"SSN     : {self.__ssn}")


# ---- Testing access ----
if __name__ == "__main__":
    emp = Employee("John Doe", 50000, "123-45-6789")

    # Access public variable - works fine
    print("Public access:")
    print(emp.name)          # John Doe

    # Access protected variable - possible, but discouraged (convention)
    print("\nProtected access:")
    print(emp._salary)       # 50000

    # Access private variable - raises AttributeError if accessed directly
    print("\nPrivate access:")
    try:
        print(emp.__ssn)     # This will cause an error
    except AttributeError as e:
        print("Error:", e)

    # Access private variable via name mangling (not recommended, but possible)
    print("\nPrivate access via name mangling:")
    print(emp._Employee__ssn)  # 123-45-6789

    print("\nUsing class method to display all info:")
    emp.display_info()
