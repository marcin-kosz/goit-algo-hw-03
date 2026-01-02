import re

def normalize_phone(phone_number):
    normalized_phone = re.sub(r'\D', '', phone_number)
    if not normalized_phone.startswith('+'):
        if normalized_phone.startswith('380'):
            normalized_phone = '+' + normalized_phone
        else:
            normalized_phone = '+38' + normalized_phone
    return normalized_phone
