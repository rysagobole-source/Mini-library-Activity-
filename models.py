from __future__ import annotations
from typing import List, Dict

class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = available

    @property
    def book_id(self) -> int:
        return self._book_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def available(self) -> bool:
        return self._available

    def borrow(self) -> None:
        from exceptions import BookNotAvailableError
        if not self._available:
            raise BookNotAvailableError(f"Book '{self._title}' is already borrowed.")
        self._available = False

    def return_book(self) -> None:  # Used for returning
        self._available = True

    def __str__(self) -> str:
        status = "Available" if self._available else "Borrowed"
        return f"[Book] ID: {self._book_id} | Title: {self._title} | Author: {self._author} | Status: {status}"


class Member:
    def __init__(self, member_id: int, name: str, email: str):
        self._member_id = member_id
        self._name = name
        self._email = email

    @property
    def member_id(self) -> int:
        return self._member_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    def __str__(self) -> str:
        return f"[Member] ID: {self._member_id} | Name: {self._name} | Email: {self._email}"


class Loan:
    def __init__(self, loan_id: int, book: Book, member: Member, is_active: bool = True):
        self._loan_id = loan_id
        self._book = book
        self._member = member
        self._is_active = is_active

    @property
    def loan_id(self) -> int:
        return self._loan_id

    @property
    def book(self) -> Book:
        return self._book

    @property
    def member(self) -> Member:
        return self._member

    @property
    def is_active(self) -> bool:
        return self._is_active

    def mark_returned(self) -> None:  # Used for returning
        self._is_active = False

    def __str__(self) -> str:
        status = "Active" if self._is_active else "Returned"
        return f"[Loan] ID: {self._loan_id} | Book: '{self._book.title}' | Member: {self._member.name} | Status: {status}"