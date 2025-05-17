class MathUtils:
    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b


# ---- quick demo ----
if __name__ == "__main__":
    result = MathUtils.add(7, 5)
    print("Sum:", result)   # → Sum: 12
