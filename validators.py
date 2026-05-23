from exceptions import InvalidBookIDError, InvalidMemberIDError, EmptyFieldError, InvalidEmailError

class InputValidator:
    @staticmethod
    def validate_id(id_str: str, entity_name: str) -> int:
        try:
            entity_id = int(id_str.strip())
        except ValueError:
            if entity_name == "Book":
                raise InvalidBookIDError(f"{entity_name} ID must be an integer. Got: '{id_str}'")
            else:
                raise InvalidMemberIDError(f"{entity_name} ID must be an integer. Got: '{id_str}'")
        
        if entity_id <= 0:
            if entity_name == "Book":
                raise InvalidBookIDError(f"{entity_name} ID must be positive. Got: {entity_id}")
            else:
                raise InvalidMemberIDError(f"{entity_name} ID must be positive. Got: {entity_id}")
        return entity_id

    @staticmethod
    def validate_non_empty(field_name: str, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise EmptyFieldError(f"'{field_name}' cannot be empty.")
        return cleaned

    @staticmethod
    def validate_email(email_str: str) -> str:
        email = email_str.strip()
        if not email:
            raise EmptyFieldError("Member Email cannot be empty.")
        if '@' not in email or '.' not in email:
            raise InvalidEmailError(f"Invalid email format: '{email}'.")
        return email