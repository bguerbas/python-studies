import re
from re import Match


def email_ok(email: str) -> bool | Match[str] | None:
    # Define the regex pattern for a valid email
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not email:
        return False
    return re.match(email_regex, email)


def phone_ok(phone: str) -> bool:
    # Remove todos os caracteres que não são dígitos
    phone_regex = re.sub(r'\D', '', phone)
    len_phone = len(phone_regex)
    if len_phone == 10 or len_phone == 11:
        return True
    return False
