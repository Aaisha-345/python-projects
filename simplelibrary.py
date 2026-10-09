# Initialize the library with a few books (Represented as dictionaries)
library = [
    {"title": "Python 101", "author": "Guido", "available": True},
    {"title": "Data Science Basics", "author": "Alice", "available": True},
    {"title": "Learn Coding", "author": "Bob", "available": False}  # Starting as unavailable for testing
]

def show_available_books():
    """Displays all books that are currently available to borrow."""
    print("\n--- Available Books ---")
    found = False
    for book in library:
        if book["available"]:
            print(f" '{book['title']}' by {book['author']}")
            found = True
    if not found:
        print(" No books are currently available.")

def borrow_book(title):
    """Borrows a book by changing its availability status to False."""
    print(f"\nAttempting to borrow: '{title}'")
    for book in library:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print(f" Success! You have borrowed '{book['title']}'.")
                return
            else:
                print(f" Error: '{book['title']}' is already borrowed.")
                return
    print(f" Error: '{title}' was not found in the library.")

def return_book(title):
    """Returns a borrowed book by setting its availability to True."""
    print(f"\nAttempting to return: '{title}'")
    for book in library:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print(f" Success! '{book['title']}' has been returned.")
                return
            else:
                print(f" Info: '{book['title']}' was already available in the library.")
                return
    print(f" Error: '{title}' does not belong to this library.")

def search_books(keyword):
    """Challenge: Search for books by title or author keyword."""
    print(f"\n--- Search Results for '{keyword}' ---")
    found = False
    for book in library:
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f" '{book['title']}' by {book['author']} [{status}]")
            found = True
    if not found:
        print("No books matched your search.")

# =====================================================================
# DEMO & TEST CASES (Definition of Done)
# =====================================================================

print("--- Initial State ---")
show_available_books()

# Test Case 1: Standard Borrowing & Availability Update
print("\n>>> TEST CASE 1: Standard Borrowing <<<")
borrow_book("Python 101")
show_available_books()

# Test Case 2: Test borrowing the same book twice (Key Rule)
print("\n>>> TEST CASE 2: Borrowing the Same Book Twice <<<")
borrow_book("Python 101")

# Test Case 3: Returning a book & Challenge Search Feature
print("\n>>> TEST CASE 3: Return & Search Challenge <<<")
return_book("Python 101")
search_books("Guido")