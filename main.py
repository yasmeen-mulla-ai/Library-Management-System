import os
from datetime import datetime


class Library:

    def __init__(self):
        self.books_file = "books.txt"
        self.students_file = "students.txt"
        self.issued_file = "issued_books.txt"

    # ================= ADD BOOK =================

    def add_book(self):

        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        with open(self.books_file, "a") as file:
            file.write(f"{book_id},{book_name},{author}\n")

        print("\n✅ Book Added Successfully")

    # ================= VIEW BOOKS =================

    def view_books(self):

        print("\n========== AVAILABLE BOOKS ==========\n")

        try:
            with open(self.books_file, "r") as file:

                books = file.readlines()

                if not books:
                    print("No Books Available")
                    return

                for book in books:

                    data = book.strip().split(",")

                    print(f"""
Book ID     : {data[0]}
Book Name   : {data[1]}
Author      : {data[2]}
-----------------------------------
""")

        except FileNotFoundError:
            print("Books File Not Found")

    # ================= ADD STUDENT =================

    def add_student(self):

        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")

        with open(self.students_file, "a") as file:
            file.write(f"{student_id},{student_name}\n")

        print("\n✅ Student Added Successfully")

    # ================= VIEW STUDENTS =================

    def view_students(self):

        print("\n========== STUDENT RECORDS ==========\n")

        try:
            with open(self.students_file, "r") as file:

                students = file.readlines()

                if not students:
                    print("No Students Found")
                    return

                for student in students:

                    data = student.strip().split(",")

                    print(f"""
Student ID     : {data[0]}
Student Name   : {data[1]}
-----------------------------------
""")

        except FileNotFoundError:
            print("Student File Not Found")

    # ================= ISSUE BOOK =================

    def issue_book(self):

        student_name = input("Enter Student Name: ")
        book_name = input("Enter Book Name: ")

        issue_date = datetime.now().strftime("%d-%m-%Y")

        with open(self.issued_file, "a") as file:
            file.write(f"{student_name},{book_name},{issue_date}\n")

        print("\n✅ Book Issued Successfully")

    # ================= VIEW ISSUED BOOKS =================

    def view_issued_books(self):

        print("\n========== ISSUED BOOKS ==========\n")

        try:
            with open(self.issued_file, "r") as file:

                records = file.readlines()

                if not records:
                    print("No Issued Books")
                    return

                for record in records:

                    data = record.strip().split(",")

                    print(f"""
Student Name   : {data[0]}
Book Name      : {data[1]}
Issue Date     : {data[2]}
-----------------------------------
""")

        except FileNotFoundError:
            print("Issued File Not Found")

    # ================= RETURN BOOK =================

    def return_book(self):

        student_name = input("Enter Student Name: ")
        book_name = input("Enter Book Name: ")

        try:

            with open(self.issued_file, "r") as file:
                records = file.readlines()

            with open(self.issued_file, "w") as file:

                found = False

                for record in records:

                    data = record.strip().split(",")

                    if data[0] == student_name and data[1] == book_name:
                        found = True
                        continue

                    file.write(record)

            if found:
                print("\n✅ Book Returned Successfully")
            else:
                print("\n❌ Record Not Found")

        except FileNotFoundError:
            print("Issued File Not Found")


# ================= MAIN PROGRAM =================

library = Library()

while True:

    print("""
=========== LIBRARY MANAGEMENT SYSTEM ===========

1. Add Book
2. View Books
3. Add Student
4. View Students
5. Issue Book
6. View Issued Books
7. Return Book
8. Exit

================================================
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.add_student()

    elif choice == "4":
        library.view_students()

    elif choice == "5":
        library.issue_book()

    elif choice == "6":
        library.view_issued_books()

    elif choice == "7":
        library.return_book()

    elif choice == "8":
        print("\nThank You")
        break

    else:
        print("\n❌ Invalid Choice")