class LibraryError(Exception):
    pass

class BookError(LibraryError):
    pass

class MemberError(LibraryError):
    pass

class LoanError(LibraryError): 
    pass

class EmptyFieldError(LibraryError):
    pass

class InvalidBookIDError(BookError):
    pass
class DuplicateBookIDError(BookError):
    pass
class BookNotFoundError(BookError):
    pass
class BookNotAvailableError(BookError):
    pass

class InvalidMemberIDError(MemberError):
    pass
class DuplicateMemberIDError(MemberError):
    pass
class MemberNotFoundError(MemberError):
    pass
class InvalidEmailError(MemberError):
    pass