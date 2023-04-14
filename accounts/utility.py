import re
from rest_framework.exceptions import ValidationError

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regex = re.compile(r"^9\d{12}$")


def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        email_or_phone = 'email'
    elif re.fullmatch(phone_regex, email_or_phone):
        email_or_phone = 'phone'
    else:
        data = {
            'success': False,
            'message': "Email yoki telefon raqamingiz notog'ri"
        }
        raise ValidationError(data)
    return email_or_phone
