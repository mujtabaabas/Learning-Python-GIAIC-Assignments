import streamlit as st
import json

class LibraryManager:
    def __init__(self):
        self.library = []

    def add_book(self, title, author, year, genre, read_status):
        book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read_status
        }
        self.library.append(book)

    def remove_book(self, title):
        for book in self.library:
            if book['title'].lower() == title.lower():
                self.library.remove(book)
                return True
        return False

    def search_books(self, search_type, query):
        if search_type == "Title":
            return [book for book in self.library if query.lower() in book['title'].lower()]
        elif search_type == "Author":
            return [book for book in self.library if query.lower() in book['author'].lower()]
        return []

    def display_books(self):
        return self.library

    def display_statistics(self):
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book['read'])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        return total_books, percentage_read

    def save_library(self):
        with open('library.txt', 'w') as file:
            json.dump(self.library, file)

    def load_library(self):
        try:
            with open('library.txt', 'r') as file:
                self.library = json.load(file)
        except FileNotFoundError:
            pass


def main():
    st.title("Personal Library Manager")
    manager = LibraryManager()
    manager.load_library()

    menu = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics", "Exit"]
    choice = st.sidebar.selectbox("Choose an action", menu)

    if choice == "Add a Book":
        st.subheader("Add a Book")
        title = st.text_input("Enter the book title")
        author = st.text_input("Enter the author")
        year = st.number_input("Enter the publication year", min_value=1000, max_value=9999)
        genre = st.text_input("Enter the genre")
        read_status = st.selectbox("Have you read this book?", ("Yes", "No"))
        read_status = read_status == "Yes"
        if st.button("Add Book"):
            if title and author and genre:  # Check if essential fields are provided
                manager.add_book(title, author, year, genre, read_status)
                st.success("Book added successfully!")
                manager.save_library()
            else:
                st.error("Please fill in all required fields.")

    elif choice == "Remove a Book":
        st.subheader("Remove a Book")
        title = st.text_input("Enter the title of the book to remove")
        if st.button("Remove Book"):
            if title:
                if manager.remove_book(title):
                    st.success("Book removed successfully!")
                else:
                    st.error("Book not found!")
                manager.save_library()
            else:
                st.error("Please provide a book title.")

    elif choice == "Search for a Book":
        st.subheader("Search for a Book")
        search_type = st.radio("Search by", ("Title", "Author"))
        query = st.text_input(f"Enter the {search_type.lower()} to search")
        if query:
            results = manager.search_books(search_type, query)
            if results:
                st.write("Matching Books:")
                for book in results:
                    read_status = "Read" if book['read'] else "Unread"
                    st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
            else:
                st.write("No matching books found.")

    elif choice == "Display All Books":
        st.subheader("Display All Books")
        books = manager.display_books()
        if books:
            for book in books:
                read_status = "Read" if book['read'] else "Unread"
                st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        else:
            st.write("No books in the library.")

    elif choice == "Display Statistics":
        st.subheader("Library Statistics")
        total_books, percentage_read = manager.display_statistics()
        st.write(f"Total books: {total_books}")
        st.write(f"Percentage read: {percentage_read:.2f}%")

    elif choice == "Exit":
        manager.save_library()
        st.write("Library saved. Goodbye!")

if __name__ == "__main__":
    main()
