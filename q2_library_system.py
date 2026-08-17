def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print("Book added successfully!")


def borrow_book(catalog, borrowed_books, book_id):

    if book_id in catalog:

        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print("Book borrowed successfully!")

        else:
            print("Book is already borrowed.")

    else:
        print("Book does not exist.")


def return_book(borrowed_books, book_id):

    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned successfully!")

    else:
        print("Book was not borrowed.")


def register_member(members, member_id):

    if member_id not in members:
        members.add(member_id)
        print("Member registered successfully!")

    else:
        print("Member already exists.")


def show_available(catalog, borrowed_books):

    print("\nAvailable Books:")

    for book_id in catalog:

        if book_id not in borrowed_books:
            title, author, year = catalog[book_id]

            print("ID:", book_id)
            print("Title:", title)
            print("Author:", author)
            print("Year:", year)
            print()


def main():

    # Dictionary
    catalog = {}

    # List
    borrowed_books = []

    # Set
    members = set()

    # Adding 4 books
    add_book(catalog, 101, "Python Basics", "John", 2022)
    add_book(catalog, 102, "Java Programming", "James", 2021)
    add_book(catalog, 103, "Data Structures", "Robert", 2023)
    add_book(catalog, 104, "Machine Learning", "David", 2024)

    # Registering members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)

    # Trying to register same member again
    register_member(members, 2)

    # Borrowing 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 102)

    # Returning book 101
    return_book(borrowed_books, 101)

    # Display available books
    show_available(catalog, borrowed_books)


main()