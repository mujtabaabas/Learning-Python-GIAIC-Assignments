def main():
    print("📈 Welcome to the Number Doubler Program!\n")

    while True:
        try:
            # Get a valid number from the user
            curr_value = int(input("Enter a number to start doubling: "))
            original_value = curr_value
            count = 0
            results = []

            # Doubling process
            while curr_value < 100:
                curr_value *= 2
                results.append(curr_value)
                count += 1

            # Print results
            print("\n🔁 Doubling sequence:")
            print(" → ".join(map(str, results)))

            # Feedback
            print(f"\n✅ Started with {original_value}, it reached {curr_value} after {count} doublings.")

        except ValueError:
            print("❌ Please enter a valid number!\n")
            continue

        # Ask user if they want to run again
        repeat = input("\n🔁 Do you want to try another number? (yes/no): ").strip().lower()
        if repeat not in ["yes", "y"]:
            print("\n👋 Thanks for using the Number Doubler! Goodbye!")
            break


if __name__ == '__main__':
    main()
