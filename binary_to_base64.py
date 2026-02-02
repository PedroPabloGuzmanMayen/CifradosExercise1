from utils import BASE64_ALPHABET, divide_binary_string, binary_string_to_decimal

def binary_to_base64(binary):
    final = ''
    padding = ''
    if len(binary) % 24 == 8:
        padding = '=='
    elif len(binary) % 24 == 16:
        padding = '='
    new_strings = divide_binary_string(binary, 6)
    for i in new_strings:
        final += BASE64_ALPHABET[binary_string_to_decimal(i)]
    
    return final + padding
