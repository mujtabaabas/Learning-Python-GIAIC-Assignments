# The speed of light in meters per second (m/s)
C = 299792458

def main():
    # Prompt the user to enter mass in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate the energy using E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the breakdown and the result
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# Required to run the main function
if __name__ == '__main__':
    main()
