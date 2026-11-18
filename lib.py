# ==========================================
#       LIBRARY MANAGEMENT SYSTEM
# ==========================================

books = [
    {"id": "B101", "name": "Python Programming", "author": "Guido", "status": "Available"},
    {"id": "B102", "name": "C Programming", "author": "Dennis Ritchie", "status": "Available"},
    {"id": "B103", "name": "Java Programming", "author": "James Gosling", "status": "Available"},
    {"id": "B104", "name": "Data Structures", "author": "Mark Weiss", "status": "Available"},
    {"id": "B105", "name": "Artificial Intelligence", "author": "Stuart Russell", "status": "Available"},
    {"id": "B106", "name": "Machine Learning", "author": "Tom Mitchell", "status": "Available"},
    {"id": "B107", "name": "Operating System", "author": "Galvin", "status": "Available"},
    {"id": "B108", "name": "Computer Networks", "author": "Tanenbaum", "status": "Available"},
    {"id": "B109", "name": "Database Management", "author": "Ramakrishnan", "status": "Available"},
    {"id": "B110", "name": "Web Development", "author": "Jon Duckett", "status": "Available"},
    {"id": "B111", "name": "HTML and CSS", "author": "Jon Duckett", "status": "Available"},
    {"id": "B112", "name": "Digital Electronics", "author": "Morris Mano", "status": "Available"},
    {"id": "B113", "name": "Software Engineering", "author": "Ian Sommerville", "status": "Available"},
    {"id": "B114", "name": "Computer Fundamentals", "author": "P.K. Sinha", "status": "Available"},
    {"id": "B115", "name": "Deep Learning", "author": "Ian Goodfellow", "status": "Available"},
    {"id": "B116", "name": "Cyber Security", "author": "William Stallings", "status": "Available"}
]


members = [
    {"id": "M101", "name": "Aman Kumar", "course": "B.Tech CSE"},
    {"id": "M102", "name": "Jotsroop Singh", "course": "B.Tech AI/ML"},
    {"id": "M103", "name": "Gurpreet Singh", "course": "BCA"},
    {"id": "M104", "name": "Harpreet Kaur", "course": "B.Tech CSE"},
    {"id": "M105", "name": "Simran Kaur", "course": "BCA"},
    {"id": "M106", "name": "Manpreet Singh", "course": "B.Tech AI/ML"},
    {"id": "M107", "name": "Rohit Kumar", "course": "BBA"},
    {"id": "M108", "name": "Sandeep Singh", "course": "B.Tech CSE"},
    {"id": "M109", "name": "Navdeep Kaur", "course": "BCA"},
    {"id": "M110", "name": "Arjun Singh", "course": "B.Tech AI/ML"},
    {"id": "M111", "name": "Rajveer Singh", "course": "BBA"},
    {"id": "M112", "name": "Priya Sharma", "course": "BCA"},
    {"id": "M113", "name": "Karan Kumar", "course": "B.Tech CSE"},
    {"id": "M114", "name": "Neha Sharma", "course": "BCA"},
    {"id": "M115", "name": "Deepak Singh", "course": "B.Tech AI/ML"},
    {"id": "M116", "name": "Anjali Kaur", "course": "BBA"}
]


def line():
    print("=" * 55)


def view_books():
    line()
    print("                 BOOK COLLECTION")
    line()

    for book in books:
        print("ID:", book["id"])
        print("Name:", book["name"])
        print("Author:", book["author"])
        print("Status:", book["status"])
        print("-" * 55)


def view_members():
    line()
    print("                 MEMBER DETAILS")
    line()

    for member in members:
        print("Member ID:", member["id"])
        print("Name:", member["name"])
        print("Course:", member["course"])
        print("-" * 55)


def add_book():
    line()
    print("                  ADD NEW BOOK")
    line()

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    books.append({
        "id": book_id,
        "name": name,
        "author": author,
        "status": "Available"
    })

    print("\nBook Added Successfully!")


def add_member():
    line()
    print("                 ADD NEW MEMBER")
    line()

    member_id = input("Enter Member ID: ")

    for member in members:
        if member["id"] == member_id:
            print("Member ID already exists!")
            return

    name = input("Enter Member Name: ")
    course = input("Enter Course: ")

    members.append({
        "id": member_id,
        "name": name,
        "course": course
    })

    print("\nMember Added Successfully!")


def search_book():
    line()
    print("                  SEARCH BOOK")
    line()

    book_id = input("Enter Book ID: ")
    found = False

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found!")
            print("Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            found = True

    if not found:
        print("Book Not Found!")


def issue_book():
    line()
    print("                   ISSUE BOOK")
    line()

    book_id = input("Enter Book ID: ")
    member_id = input("Enter Member ID: ")

    selected_book = None
    selected_member = None

    for book in books:
        if book["id"] == book_id:
            selected_book = book

    for member in members:
        if member["id"] == member_id:
            selected_member = member

    if selected_book is None:
        print("Book Not Found!")

    elif selected_member is None:
        print("Member Not Found!")

    elif selected_book["status"] == "Issued":
        print("Book Already Issued!")

    else:
        selected_book["status"] = "Issued"
        selected_book["issued_to"] = selected_member["name"]
        print("\nBook Issued Successfully!")
        print("Book:", selected_book["name"])
        print("Issued To:", selected_member["name"])


def return_book():
    line()
    print("                  RETURN BOOK")
    line()

    book_id = input("Enter Book ID: ")
    found = False

    for book in books:
        if book["id"] == book_id:
            found = True

            if book["status"] == "Issued":
                book["status"] = "Available"
                book.pop("issued_to", None)
                print("Book Returned Successfully!")

            else:
                print("Book Is Already Available!")

    if not found:
        print("Book Not Found!")


def delete_book():
    line()
    print("                  DELETE BOOK")
    line()

    book_id = input("Enter Book ID: ")
    found = False

    for book in books:
        if book["id"] == book_id:
            found = True

            if book["status"] == "Issued":
                print("Cannot delete an issued book!")
            else:
                books.remove(book)
                print("Book Deleted Successfully!")

            break

    if not found:
        print("Book Not Found!")


# MAIN PROGRAM

while True:

    print("\n")
    line()
    print("          WELCOME TO OUR LIBRARY")
    print("           LIBRARY MANAGEMENT")
    line()

    print("  1. View All Books")
    print("  2. View All Members")
    print("  3. Add New Book")
    print("  4. Add New Member")
    print("  5. Search Book")
    print("  6. Issue Book")
    print("  7. Return Book")
    print("  8. Delete Book")
    print("  9. Exit")

    line()

    choice = input("Enter Your Choice (1-9): ")

    if choice == "1":
        view_books()

    elif choice == "2":
        view_members()

    elif choice == "3":
        add_book()

    elif choice == "4":
        add_member()

    elif choice == "5":
        search_book()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        delete_book()

    elif choice == "9":
        print("\nThank You For Visiting Our Library!")
        print("Have A Nice Day!")
        break

    else:
        print("Invalid Choice! Please Try Again.")