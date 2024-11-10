# The-Library

Library Management System

A simple command-line application for managing a collection of manga books. This system allows users to add, search, edit, and delete manga entries while maintaining persistent storage using JSON.
Features

Add New Manga: Add manga entries with title, description, author, and availability status
Search Functions:

Search by manga title
Search by author name


Edit Manga: Modify existing manga entries' details
Delete Manga: Remove manga entries from the library
Data Persistence: All data is saved to JSON file for persistent storage

How to Use

Run the program:

python main.py

Choose from the following options in the main menu:

Add a new manga
Search for a manga by title
Search for manga by author
Edit manga details
Delete manga
Exit (automatically saves changes)



Data Structure
Each manga entry contains:

Title
Description
Author
Status (Available/Unavailable)

File Structure
Copy├── main.py       # Main program entry point
├── books.py          # Book class and related functions
├── books.json        # Data storage file
└── README.md         # Documentation
Requirements

Python 3.x
No additional packages required (uses only built-in libraries)

Example Usage
python# 
Adding a new manga
Do you want to add a new book? 'Yes' or 'No': Yes
Add a new book: One Piece
Add a description: Story of a young man whose dream is to be the king of pirates.
Add author: Eiichiro Oda

# Searching for a manga

Write the name of the book you're looking for: One Piece
Future Improvements

Contributing
Feel free to fork this project and submit pull requests with improvements. You can also open issues for bugs or feature requests.

License
This project is open source and available under the MIT License.