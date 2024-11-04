

class Book:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nAuthor: {self.author}"

books = [
    Book("Naruto", "Story of a young ninja who tries to save his best friend.", "Masashi Kishimoto"),
    Book("One Piece", "Story of a young man whose dream is to be the king of pirates.", "Eiichiro Oda"),
    Book("Attack on Titan", "A boy fights to protect humanity from giant monsters.", "Hajime Isayama"),
    Book("Bleach", "A high school student accidentally gains the powers of a Soul Reaper.", "Tite Kubo"),
    Book("Death Note", "A student discovers a notebook with deadly powers.", "Tsugumi Ohba"),
    Book("Fullmetal Alchemist", "Two brothers seek the Philosopher's Stone to restore their bodies.", "Hiromu Arakawa"),
    Book("Dragon Ball", "A martial artist seeks powerful orbs to summon a dragon.", "Akira Toriyama"),
    Book("My Hero Academia", "A powerless boy enters a school for heroes.", "Kohei Horikoshi"),
    Book("Fairy Tail", "A young wizard joins a guild and embarks on adventures.", "Hiro Mashima"),
    Book("Tokyo Ghoul", "A student turns into a half-ghoul and struggles with his identity.", "Sui Ishida"),
    Book("Hunter x Hunter", "A boy embarks on an adventure to find his father and become a Hunter.", "Yoshihiro Togashi"),
    Book("Demon Slayer", "A boy joins the Demon Slayer Corps to avenge his family and save his sister.", "Koyoharu Gotouge"),
    Book("Sword Art Online", "Players become trapped in a virtual reality game and must fight to survive.", "Reki Kawahara"),
    Book("Black Clover", "A young, magicless boy aspires to become the Wizard King.", "Yūki Tabata"),
    Book("Vagabond", "A fictionalized retelling of the life of legendary samurai Musashi Miyamoto.", "Takehiko Inoue"),
    Book("The Seven Deadly Sins", "A princess seeks the help of disbanded knights to save her kingdom.", "Nakaba Suzuki"),
    Book("Reborn!", "A young boy learns he's destined to lead an Italian mafia family.", "Akira Amano"),
    Book("JoJo's Bizarre Adventure", "Follows generations of the Joestar family, each with their own unique abilities.", "Hirohiko Araki"),
    Book("Yu Yu Hakusho", "A boy is brought back to life to work as a Spirit Detective.", "Yoshihiro Togashi"),
    Book("Berserk", "A dark, gritty tale of a lone swordsman's quest for revenge and survival.", "Kentaro Miura")
]


def add_book():
    while True:

        new_book = input("Do you want to add a new book? 'Yes' or 'No': ")

        if new_book.lower() != 'yes':
            print("Thank you!")
            break
        
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

def main_menu():
    while True:
        print("\n=== Library Menu ===")
        print("1. Add book")
        print("2. Search book")
        print("3. Search author")
        print("4. Show all books")
        print("5. Edit book")
        print("6. Delete book")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            author_book()
        elif choice == '4':
            print("\nAll Books:")
            for book in books:
                print(book)
        elif choice == '5':
            edit_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()