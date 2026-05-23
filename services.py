from __future__ import annotations
from typing import List, Dict
from models import Book, Member, Loan
from exceptions import DuplicateBookIDError, DuplicateMemberIDError, BookNotFoundError, MemberNotFoundError, BookNotAvailableError, LoanError

class LibraryService:
    def __init__(self):
        self._books: Dict[int, Book] = {}
        self._members: Dict[int, Member] = {}
        self._loans: List[Loan] = []
        self._next_loan_id: int = 1

    def add_book(self, book: Book) -> None:
        if book.book_id in self._books:
            raise DuplicateBookIDError(f"Book with ID {book.book_id} already exists.")
        self._books[book.book_id] = book

    def view_books(self) -> List[Book]:
        return list(self._books.values())

    def register_member(self, member: Member) -> None:
        if member.member_id in self._members:
            raise DuplicateMemberIDError(f"Member with ID {member.member_id} already exists.")
        self._members[member.member_id] = member

    def view_members(self) -> List[Member]:
        return list(self._members.values())

    def borrow_book(self, book_id: int, member_id: int) -> Loan:
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book with ID {book_id} does not exist.")
        
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member with ID {member_id} does not exist.")
        
        if book.available is False:
            raise BookNotAvailableError(f"Book '{book.title}' is currently borrowed.")

        loan = Loan(self._next_loan_id, book, member, is_active=True)
        self._next_loan_id += 1
        self._loans.append(loan)
        book.borrow()
        
        return loan

    def return_book(self, book_id: int) -> Loan:
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book with ID {book_id} does not exist.")
        if book.available is True:
            raise BookNotAvailableError(f"Book '{book.title}' is not currently borrowed.")
        
        active_loan = None
        for loan in self._loans:
            if loan.book.book_id == book_id and loan.is_active:
                active_loan = loan
                break
                
        if active_loan is None:
            raise LoanError(f"No active loan found for Book ID {book_id}.")
            
        book.return_book()
        active_loan.mark_returned()
        return active_loan

    def view_loans(self) -> List[Loan]:
        return self._loans