class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit and return the value."""
        return (celsius * 9/5) + 32


# ---- demo ----
if __name__ == "__main__":
    c = 25
    f = TemperatureConverter.celsius_to_fahrenheit(c)
    print(f"{c}°C is equal to {f}°F")
