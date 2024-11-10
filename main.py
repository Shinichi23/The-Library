import books

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
            books.add_book()
        elif choice == '2':
            books.search_book()
        elif choice == '3':
            books.author_book()
        elif choice == '4':
            print("\nAll Books:")
            for book in books.books:
                print(book)
        elif choice == '5':
            books.edit_book()
        elif choice == '6':
            books.delete_book()
        elif choice == '7':
            books.save_book()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()