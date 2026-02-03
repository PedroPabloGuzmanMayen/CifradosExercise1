LOWER_ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
UPPER_ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def cipher_caesar(message, shift):

    shift = shift % 27
    final = ''
    for i in message:
        if i not in UPPER_ALPHABET and i not in LOWER_ALPHABET:
            final += i
            continue
        abecedary = LOWER_ALPHABET if i in LOWER_ALPHABET else UPPER_ALPHABET
        new = (abecedary.index(i) + shift) % 27
        final += abecedary[new]

    return final

def decipher_caesar(message, shift):

    shift = shift % 27
    final = ''
    for i in message:
        if i not in UPPER_ALPHABET and i not in LOWER_ALPHABET:
            final += i
            continue
        abecedary = LOWER_ALPHABET if i in LOWER_ALPHABET else UPPER_ALPHABET
        new = (abecedary.index(i) - shift) % 27
        final += abecedary[new]

    return final

