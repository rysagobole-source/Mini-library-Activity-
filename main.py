from services import LibraryService
from models import Book, Member
from validators import InputValidator
from exceptions import (InvalidBookIDError, EmptyFieldError, DuplicateBookIDError,
                        InvalidMemberIDError, DuplicateMemberIDError, InvalidEmailError,
                        BookNotFoundError, MemberNotFoundError, BookNotAvailableError, LoanError)

class LibraryApp:
    MENU = """
========== Library Menu ==========
  1. Add Book
  2. Register Member
  3. Borrow Book
  4. Return Book
  5. View Books
  6. View Members
  7. View Loans
  8. Exit
==================================
"""

    def __init__(self):
        self._service = LibraryService()
        self._validator = InputValidator()

    def run(self) -> None:
        print("Welcome to the Library System!")
        while True:
            print(self.MENU)
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self._add_book_flow()
            elif choice == '2':
                self._register_member_flow()
            elif choice == '3':
                self._borrow_book_flow()
            elif choice == '4':
                self._return_book_flow()      # ADDED RETURN BOOK
            elif choice == '5':
                self._view_books_flow()
            elif choice == '6':
                self._view_members_flow()
            elif choice == '7':
                self._view_loans_flow()
            elif choice == '8':
                print("Program closed.")
                break
            else:
                print("❌ Invalid choice. Please enter 1-8.\n")

    # ---------- Flow 1: Add Book ----------
    def _add_book_flow(self) -> None:
        print("\n--- Add a New Book ---")
        try:
            book_id = self._validator.validate_id(input("Input: Book ID -> "), "Book")
            title = self._validator.validate_non_empty("Book Title", input("Input: Book Title -> "))
            author = self._validator.validate_non_empty("Book Author", input("Input: Book Author -> "))
            new_book = Book(book_id, title, author, available=True)
            self._service.add_book(new_book)
            print(f"✅ Book added: {title}\n")
        except (InvalidBookIDError, EmptyFieldError, DuplicateBookIDError) as e:
            print(f"❌ Error: {e}\n")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

    # ---------- Flow 2: Register Member ----------
    def _register_member_flow(self) -> None:
        print("\n--- Register a New Member ---")
        try:
            member_id = self._validator.validate_id(input("Input: Member ID -> "), "Member")
            name = self._validator.validate_non_empty("Member Name", input("Input: Member Name -> "))
            email = self._validator.validate_email(input("Input: Member Email -> "))
            new_member = Member(member_id, name, email)
            self._service.register_member(new_member)
            print(f"✅ Member registered: {name}\n")
        except (InvalidMemberIDError, EmptyFieldError, DuplicateMemberIDError, InvalidEmailError) as e:
            print(f"❌ Error: {e}\n")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

    # ---------- Flow 3: Borrow Book ----------
    def _borrow_book_flow(self) -> None:
        print("\n--- Borrow a Book ---")
        try:
            book_id = self._validator.validate_id(input("Input: Book ID -> "), "Book")
            member_id = self._validator.validate_id(input("Input: Member ID -> "), "Member")
            loan = self._service.borrow_book(book_id, member_id)
            print(f"✅ {loan.member.name} borrowed {loan.book.title}\n")
        except (InvalidBookIDError, InvalidMemberIDError) as e:
            print(f"❌ Input Error: {e}\n")
        except (BookNotFoundError, MemberNotFoundError, BookNotAvailableError) as e:
            print(f"❌ Borrow Error: {e}\n")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

    # ---------- Flow 4: Return Book (NEW) ----------
    def _return_book_flow(self) -> None:
        print("\n--- Return a Book ---")
        try:
            book_id = self._validator.validate_id(input("Input: Book ID -> "), "Book")
            loan = self._service.return_book(book_id)
            print(f"✅ {loan.member.name} returned {loan.book.title}\n")
        except (InvalidBookIDError, BookNotFoundError, BookNotAvailableError, LoanError) as e:
            print(f"❌ Error: {e}\n")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

    # ---------- Flow 5: View Books ----------
    def _view_books_flow(self) -> None:
        print("\n--- View Books ---")
        try:
            books = self._service.view_books()
            if not books:
                print("No books found.\n")
                return

            print("Books:")
            for book in books:
                status = "Available" if book.available else "Borrowed"
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")
            print()
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

    # ---------- Flow 6: View Members ----------
    def _view_members_flow(self) -> None:
        print("\n--- View Members ---")
        try:
            members = self._service.view_members()
            if not members:
                print("No members found.\n")
                return

            print("Members:")
            for m in members:
                print(f"{m.member_id}-{m.name}({m.email})")
            print()
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")

    # ---------- Flow 7: View Loans ----------
    def _view_loans_flow(self) -> None:
        print("\n--- View Loans ---")
        try:
            loans = self._service.view_loans()
            if not loans:
                print("No loans found.\n")
                return

            print("Loans:")
            for loan in loans:
                status = "Active" if loan.is_active else "Returned"
                print(f"Loan ID: {loan.loan_id}, Book: {loan.book.title}, Member: {loan.member.name}, Status: {status}")
            print()
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}\n")


# ============================================================
# Entry Point
# ============================================================
if __name__ == "__main__":
    app = LibraryApp()
    app.run()