import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []    
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input('Enter The Title Of The Book:')
    author = input('Name The Author Of The Book:')
    year = input('Enter The Publication Year:')
    genre = input('Enter The Genre Of The Book:')
    read = input('Have You Read The The Book? (yes/no):').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)  # append is used to add new book
    save_library(library)
    print(f'Book {title}Added Successfully.')   #function 

def remove_book(library):     #Function
    title = input('Select The Book To Remove From Library')
    initial_length =len(library)     #Variable
    liibrary = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book {title} removed successfully.')
    else:
        print(f'Book {title} not found in the library.')    

def search_library(library):    #Function for search library
    search_by = input("Search by title or author").lower()
    search_term = input(f'Enter the {search_by}').lower()

    results = [book for book in library if search_term in book[search_by].lower()]
    if results:
        for book in results:
           status = "Read" if book['read'] else "Unread"
           print(f'{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}')
        else:
            print(f"No books found matching '{search_term}' in the {search_by} field.") 
def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")  

    else:
        print("The library is empty.")                  

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}") 
    print(f"Percentage rea : {percentage_read:.2f}%")   

def main():
    library = load_library()
    while True:
        print("Welcome to the library manager")
        print("Menu")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search")
        print("4. Display all books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter Your Choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library) 
        elif choice == '3':
            search_library(library) 
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Finished!")
            break
        else :
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()            
