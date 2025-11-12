from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view_all_available_books():
    print("\nAvailable Books:") # i added a newline header for better looks
    for book in library_books: #searches each entry of library books for a book
        if book["available"]: # checks if the book is available by looking at value of "available" t/f
            print(f'{book["id"]}: "{book["title"]}" by {book["author"]}') #f string prints the id value, title value, and author value
      


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching 

def author_genre_book_search():
    search = input("Please enter either the genre or author:").lower()
     # added .lower to make it case insensitive

    print("\n Results:")
    found = False 
        # created a boolean found to keep track of whether a matching book exists
    for book in library_books:
        if search in book["author"].lower() or search in book["genre"].lower():
            found = True
            print(f'{book["id"]}: "{book["title"]}" by {book["author"]}. Genre: ({book["genre"]})')
            # f string pulls book id, title, author, and genre and prints it to display to user
    if not found: 
        print("This book isn't in the database, sorry!")
        # if book isn't available aka boolean found is false, displays error message


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_book():
    book_id = input("\n Enter the book's ID to check out!")
    # asks user for the id of the book
    for book in library_books:
        if book["id"] == book_id: # checks if the ID entered matches the ID of the book
            if book["available"]: # checks if the book is listed as available
                book["available"] = False #marks the book unavailable if it's available and u checked it out
                due_date = datetime.now() + timedelta(days=14)
                # sets the due date to the current time and adds a change of 14 days to the date
                book["due_date"] = due_date.strftime("%Y-%m-%d")
                # makes time look better to user
                book["checkouts"] += 1
                # adds 1 to the checkout counter
                print(f'"You checked out "{book["title"]}". Due on {book["due_date"]}.')
                # regurgitates the title and due date of the book.
            else:
                print("That book has already been checked out, sorry!")
            return #exit function after processing
    print("Book ID not found, sorry!") #if there is no matching ID, displays error message


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_a_book():
    book_id = input ("\n Enter the book's ID to return it:")
    # gets ID 
    for book in library_books:
        if book["id"] == book_id:
            # checks if the book id entered is the same as any books in the class
            if not book["available"]: # if book is checked out and boolean available is false
                book["available"] = True # marks as available since you returned it
                book["due_date"] = None #clears the due date 
                print(f'You Returned "{book["title"]}". Thanks!')
            else:
                print(f'"{book["title"]}" was not checked out. Thanks!') 
                # if book is available then you can't return it
            return # stops once book is checked in
        print("Book Not Found, sorry!") # if no matching ID, book doesn't exist here

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def view_overdue_books():
    print("\n Overdue Books:")
    today = datetime.now().date() # command that gets todays date and sets it to a variable
    found = False # boolean that kept track of if a book exists to check if the book is not returned
    for book in library_books:
        if not book["available"] and book["due_date"]: # only checks for books that are checked out and have a due date
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date() 
            # turns string datetime into an actual date
            if due_date < today: # if due date is less than today's date, aka it was before
                found = True # the book is found
            print(f'{book["id"]}: "{book["title"]}" was due on {book["due_date"]}.. It\'s late!') # escapes the single apostrophe to keep python from thinking the string is wrong
    if not found: 
        print("No overdue books! Nice!") # only if the book you turned in is found

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()

# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
def menu():
    while True:
        print("\n Library's Menu:")
        print("1. View available Books")
        print("2. Search for a book (Author/Genre)")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. View all overdue books")
        print("6. Exit")

        choice = input("\n Enter your choice (1-6) Please :")
        if choice == "1":
            view_all_available_books()
        elif choice =="2":
            author_genre_book_search()
        elif choice == "3":
            checkout_book()
        elif choice == "4":
            return_a_book()
        elif choice == "5":
            view_overdue_books()
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Please enter a number from 1-6!")
        

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions           
    #view_all_available_books()     
    # author_genre_book_search()
    # checkout_book() 
    pass