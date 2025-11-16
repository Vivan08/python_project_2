# Name - Vivan Sethi
# Date - 2025-11-15
# Program - BCA(AI&DS)
# semester - 1st
# section - A
# Description - library management system


books={}
borrowing_records = {}
borrowed_books = []

def search_book_id () :
    search_id = input("Enter Book ID to search: ")
    if search_id in books:
        print("Book id:", search_id, end=" ")
        print("Name:", books[search_id]['name'], end=" ")
        print("Author:", books[search_id]['author'], end=" ")
        print("Copies:", books[search_id]['copies'])

def search_book_name () :
    search_name = input("Enter Book Name to search: ")
    found = False
    for book_id, details in books.items():
        if details['name'].lower() == search_name.lower():
            print("Book id:", book_id, end=" ")
            print("Name:", details['name'], end=" ")
            print("Author:", details['author'], end=" ")
            print("Copies:", details['copies'])
            found = True
    if not found:
        print("Book not found.")


while True :
    print("welcome to library management system !")
    print("1. Add Book")
    print("2. View Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    
    # initialize a dictionary to store book details
    option = int(input("Enter your choice: "))
    # perform operations based on user choice
    if option == 1:
        # enter book details
        entry = int(input("How many books do you want to add? "))
        for i in range(entry):
            id = input("Enter Book ID: ")
            name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")
            copies = int(input("Enter Number of Copies: "))
            books[id] = {'name': name, 'author': author, 'copies': copies}
            print("Book added successfully.")
   
   
    if option == 2 :
    # view all books
        for book in books:
            print("Book id:", book, end=" ")
            print("Name:", books[book]['name'], end=" ")
            print("Author:", books[book]['author'], end=" ")
            print("Copies:", books[book]['copies'])
   
   
    if option == 3 :
        print("Search Book by: ")
        print("1. Book ID")
        print("2. Book Name")
        type_choice = int(input("Enter your choice: "))
        #search book by Book ID
        if type_choice == 1 :
            search_book_id()
        # search by book title
        search_book_name()
    
    
    if option == 4 :
        # borrow book
        borrow_id = input("Enter Book ID to borrow: ")
        name = input("Enter Name of the student: ")
        # check if book is available
        if borrow_id in books and books[borrow_id]['copies'] > 0:
            books[borrow_id]['copies'] -= 1
            # add to borrowing records
            borrowing_records[name] = borrow_id
            print("Book borrowed successfully.")
        # if book not available
        else:
            print("Book not available for borrowing.")
    
    
    if option == 5 :
        # return book
        return_id = input("Enter Book ID to return: ")
        name = input("Enter Name of the student: ")
        # check if the book was borrowed
        if name in borrowing_records and borrowing_records[name] == return_id:
            books[return_id]['copies'] += 1
            del borrowing_records[name]
            print("Book returned successfully.")
            for i in borrowing_records:
                print("name :",i, end=" ")
                print("Book ID :",borrowing_records[i])
        else:
            print("No record of this book being borrowed by you.")
    
    
    if option == 6:
        print("Exiting the system. Goodbye!")
        break