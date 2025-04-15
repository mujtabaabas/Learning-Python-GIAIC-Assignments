# Sentence start string
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Get the three inputs from the user to make the Mad Lib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# This is required to run the main() function
if __name__ == '__main__':
    main()
