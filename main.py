import json
import os

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book_id, title, author):
        for book in self.books:
            if book["id"] == book_id:
                print("\n⚠️ Book ID already exists!")
                return
        
        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "is_issued": False,
            "issued_to": None
        }
        self.books.append(new_book)
        self.save_books()
        print(f"\n✅ '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("\n📚 No books found in the library.")
            return
        
        print("\n--- 📚 Library Books List ---")
        for book in self.books:
            status = f"Issued to {book['issued_to']}" if book["is_issued"] else "Available"
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")

    def issue_book(self, book_id, student_name):
        for book in self.books:
            if book["id"] == book_id:
                if book["is_issued"]:
                    print(f"\n⚠️ Book is already issued to {book['issued_to']}!")
                    return
                book["is_issued"] = True
                book["issued_to"] = student_name
                self.save_books()
                print(f"\n✅ '{book['title']}' issued to {student_name} successfully!")
                return
        print("\n⚠️ Book ID not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if not book["is_issued"]:
                    print("\n⚠️ This book is not issued to anyone!")
                    return
                book["is_issued"] = False
                book["issued_to"] = None
                self.save_books()
                print(f"\n✅ '{book['title']}' returned successfully!")
                return
        print("\n⚠️ Book ID not found!")

    def search_book(self, keyword):
        keyword = keyword.lower()
        found_books = [
            b for b in self.books 
            if keyword in b["id"].lower() or keyword in b["title"].lower() or keyword in b["author"].lower()
        ]
        
        if not found_books:
            print("\n⚠️ No matching books found!")
            return

        print("\n--- 🔍 Search Results ---")
        for book in found_books:
            status = f"Issued to {book['issued_to']}" if book["is_issued"] else "Available"
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")

    def delete_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["is_issued"]:
                    print(f"\n⚠️ Cannot delete book! It is currently issued to {book['issued_to']}.")
                    return
                self.books.remove(book)
                self.save_books()
                print(f"\n✅ Book ID '{book_id}' deleted successfully!")
                return
        print("\n⚠️ Book ID not found!")

def main():
    lib = Library()
    
    while True:
        print("\n=== 📖 Student Library System ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Delete Book")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == "1":
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            if b_id and title and author:
                lib.add_book(b_id, title, author)
            else:
                print("\n⚠️ All fields are required!")
                
        elif choice == "2":
            lib.display_books()

        elif choice == "3":
            b_id = input("Enter Book ID to issue: ").strip()
            student = input("Enter Student Name: ").strip()
            if b_id and student:
                lib.issue_book(b_id, student)
            else:
                print("\n⚠️ Book ID and Student Name are required!")

        elif choice == "4":
            b_id = input("Enter Book ID to return: ").strip()
            if b_id:
                lib.return_book(b_id)
            else:
                print("\n⚠️ Book ID is required!")

        elif choice == "5":
            keyword = input("Enter ID, Title, or Author to search: ").strip()
            if keyword:
                lib.search_book(keyword)
            else:
                print("\n⚠️ Search keyword is required!")

        elif choice == "6":
            b_id = input("Enter Book ID to delete: ").strip()
            if b_id:
                lib.delete_book(b_id)
            else:
                print("\n⚠️ Book ID is required!")
            
        elif choice == "7":
            print("\n👋 Exiting... Thank you for using Library System!")
            break
        else:
            print("\n⚠️ Invalid choice! Please select 1 to 7.")

if __name__ == "__main__":
    main()