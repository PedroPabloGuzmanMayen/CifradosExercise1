LOWER_ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
UPPER_ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

print(len(UPPER_ALPHABET))

def cipher_vigenere(message, key):
    
    final = ''
    key_index = 0
    for i in range(len(message)) :
        if message[i] not in UPPER_ALPHABET and message[i] not in LOWER_ALPHABET:
            final += message[i]
            continue

        abecedary = LOWER_ALPHABET if message[i] in LOWER_ALPHABET else UPPER_ALPHABET
        key_char = key[key_index % len(key)]
        key_char = key_char.lower() if abecedary == LOWER_ALPHABET else key_char.upper()
        idx = (abecedary.index(message[i]) + abecedary.index(key_char)) % 27
        final += abecedary[idx]
        key_index +=1
    
    return final

def decipher_vigenere(message, key):
    
    final = ''
    key_index = 0
    for i in range(len(message)) :
        if message[i] not in UPPER_ALPHABET and message[i] not in LOWER_ALPHABET:
            final += message[i]
            continue

        abecedary = LOWER_ALPHABET if message[i] in LOWER_ALPHABET else UPPER_ALPHABET
        key_char = key[key_index % len(key)]
        key_char = key_char.lower() if abecedary == LOWER_ALPHABET else key_char.upper()
        idx = (abecedary.index(message[i]) - abecedary.index(key_char) +27) % 27
        final += abecedary[idx]
        key_index +=1
    
    return final


print(f'Hola with lemon {decipher_vigenere('Jmvwduw id sn Kmozq', 'Cielo' )}')