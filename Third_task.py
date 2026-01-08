import re
def normalize_phone(phone_number):
    normalized_phone = re.sub(r'\D', '', phone_number)
    if normalized_phone.startswith('380'):
        normalized_phone = '+' + normalized_phone
        return normalized_phone
    elif normalized_phone.startswith('0'):
        normalized_phone = '+38' + normalized_phone
        return normalized_phone
    else:
        return '+' + normalized_phone
print(normalize_phone("+380441234567"))
