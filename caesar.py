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


print(cipher_caesar('If he had anything confidential to say he wrote it in cipher that is by so changing the order of the letters of the alphabet that not a word could be made out', 7))
print(decipher_caesar('Om ñl ñhk htfañotn jvtmokltaohr av zhf ñl dyval oa ot jowñly añha oz if zv jñhtnotn añl vykly vm añl rlaalyz vm añl hrwñhila añha tva h dvyk jvbrk il shkl vba', 7))