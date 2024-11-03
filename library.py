

class Book:
    def __init__(self, title, description, author):
        self.title = title
        self.descritpion = description
        self.auhtor = author
    
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.descritpion}\nAuthor: {self.auhtor}"


book = Book("Naruto", "Story of a young ninja who tries to save his best friend.", "Masashi Kishimoto")
book2 = Book("One Piece", "Story of a young man who's dream is being the king of pirates", "Eichiro Oda")

'''print(book.title)
print(book.descritpion)
print(book.auhtor)'''

books = [
        Book("Naruto", "Story of a young ninja who tries to save his best friend.", "Masashi Kishimoto"), 
        Book("One Piece", "Story of a young man who's dream is being the king of pirates", "Eichiro Oda")
         ]

'''print(book)
print(book2)
'''

def add_book():
    while True:

        new_book = input("Do you want to add a new book? 'Yes' or 'No': ")

        if new_book.lower() != 'yes':
            print("Thank you!")
            break
        else:
            book_title = input("Add a new book: ")
            book_description = input("Add a description: ")
            book_author = input("Add author: ")

        books.append(Book(book_title, book_description, book_author))
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
    

def main_menu():
    while True:
        print("\n=== Library Menu ===")
        print("1. Add book")
        print("2. Search book")
        print("3. Show all books")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            print("\nAll Books:")
            for book in books:
                print(book)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()