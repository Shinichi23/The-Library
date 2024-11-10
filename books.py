import os
import json

def load_books():
    try:
        if os.path.exists("books.json"):
            with open("books.json") as file:
                books_data = json.load(file)
                return [Book(
                    book["title"],
                    book["description"],
                    book["author"],
                    book["status"]
                ) for book in books_data]
    except json.JSONDecodeError:
        # If the file is corrupted or empty, delete it and return empty list
        if os.path.exists("books.json"):
            os.remove("books.json")
    return []

class Book:
    def __init__(self, title, description, author, status):
        self.title = title
        self.description = description
        self.author = author
        self.status = status
    
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nAuthor: {self.author}\nStatus: {self.status}"

def add_book():
    while True:

        new_book = input("Do you want to add a new book? 'Yes' or 'No': ")

        if new_book.lower() != 'yes':
            print("Thank you!")
            break
        
        book_title = input("Add a new book: ")
        book_description = input("Add a description: ")
        book_author = input("Add author: ")
        book_status = "Available"

        books.append(Book(book_title, book_description, book_author, book_status))
        print("Book added successfully!")

def search_book():
    search_book = input("Write the name of the book you're looking for: ")
    found = False

    for book in books:
        if search_book.lower() in book.title.lower():
            print("\nBook found:")
            print(book)
            found = True
    if not found:
        print("Sorry, book not found!")

def author_book():
    author_name = input("Write the name of the author you're looking for: ")
    found = False

    for book in books:
        if author_name.lower() in book.author.lower():
            print("\nBook found:")
            print(book)
            found = True
    if not found:
        print("Sorry, author not found!")

def delete_book():
    search_book = input("Write the name or the author name of the book you want to delete: ")

    for index, book in enumerate(books):
        if search_book.lower() in book.title.lower() or search_book.lower() in book.author.lower():
            print("\nFound book to delete:")
            print(book)
            confirm = input("Are you sure you want to delete this book? (yes/no): ")
            if confirm.lower() == 'yes':
                del books[index]
                print("Book deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    
    print("Book not found!")

def edit_book():
    search_book = input("Write the name of the book you want to edit: ")

    for book in books:
        if search_book.lower() in book.title.lower():
            print("\nCurrent book details:")
            print(book)
            print("\nEnter new details (or press Enter to keep current value):")

            new_title = input("New book title: ")
            new_description = input("New book description: ")
            new_author = input("New book author: ")

            book.title = new_title if new_title else book.title
            book.description = new_description if new_description else book.description
            book.author = new_author if new_author else book.author
            
            print("\nBook updated successfully!")
            break
    else:
        print("Book not found")

def save_book():
    books_list = [{
        "title": book.title,
        "description": book.description,
        "author": book.author,
        "status": book.status
    } for book in books]
    
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)

books = load_books()
