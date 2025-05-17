class Bank:
    # --- class variable ---
    bank_name = "Old Trust Bank"

    def __init__(self, account_holder: str):
        self.account_holder = account_holder

    # --- class method to change bank name ---
    @classmethod
    def change_bank_name(cls, name: str):
        cls.bank_name = name


# ---- demonstration ----
if __name__ == "__main__":
    # create two bank account holders
    user1 = Bank("Alice")
    user2 = Bank("Bob")

    # before changing the bank name
    print("Before change:")
    print(f"{user1.account_holder}'s bank: {user1.bank_name}")
    print(f"{user2.account_holder}'s bank: {user2.bank_name}")

    # change bank name using class method
    Bank.change_bank_name("Future Bank Ltd.")

    # after changing the bank name
    print("\nAfter change:")
    print(f"{user1.account_holder}'s bank: {user1.bank_name}")
    print(f"{user2.account_holder}'s bank: {user2.bank_name}")
