from base64_binary import BASE64_ALPHABET


def binary_string_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        if binary[::-1][i] == '1':
            decimal += (2**i)
    return decimal


def divide_binary_string(binary, division):
    divided = []
    for i in range(0, len(binary), division):
        divided.append(binary[i:i+division].ljust(division, '0'))
    return divided


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

