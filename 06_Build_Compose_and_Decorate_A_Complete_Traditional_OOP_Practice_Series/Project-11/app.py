class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title: str):
        self.title = title
        # Increment total_books whenever a new Book object is created
        Book.increment_book_count()

    # Class method to increment the book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books


# ---- demo ----
if __name__ == "__main__":
    b1 = Book("1984")
    b2 = Book("To Kill a Mockingbird")
    b3 = Book("The Great Gatsby")

    print("Total books:", Book.get_total_books())  # Output: Total books: 3
