class Logger:
    def __init__(self):
        print("Logger created: Constructor called.")

    def __del__(self):
        print("Logger destroyed: Destructor called.")


# ---- demo ----
if __name__ == "__main__":
    log = Logger()  # Constructor will be called here
    print("Logger is active...")

    # When `log` goes out of scope or is deleted, the destructor will be called
    del log          # optional: force destruction

    print("End of program.")
