LOWER_ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
UPPER_ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

print(len(UPPER_ALPHABET))

def cipher_vigenere(message, key):
    """
    Cifra un mensaje utiliando el cifrado vigenere.

    Esta función recorre un mensaje y va sumando su valor en el alfabeto con el valor de la llave y en base a eso cifra el mensaje
    Args:
        message (str): El mensaje a cifrar.
        key (str): La llave para cifrar el mensaje

    Returns:
        mensaje final: el mensaje cifrado con vigenere 
    """
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
    """
    Descifra un mensaje utiliando el cifrado vigenere.

    Esta función recorre un mensaje y va restando su valor en el alfabeto con el valor de la llave y en base a eso descifra el mensaje
    Args:
        message (str): El mensaje a cifrar.
        key (str): La llave para descifrar el mensaje

    Returns:
        mensaje final: el mensaje descifrado con vigenere 
    """
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


if __name__ == '__main__':
    while True:
        print('\n=== Cifrado Vigenère (alfabeto español) ===')
        print('1) Cifrar mensaje')
        print('2) Descifrar mensaje')
        print('3) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el mensaje a cifrar: ')
            llave = input('Ingresa la llave: ')

            cifrado = cipher_vigenere(mensaje, llave)

            print('\nMensaje cifrado:')
            print(cifrado)

        elif opcion == '2':
            mensaje = input('\nIngresa el mensaje a descifrar: ')
            llave = input('Ingresa la llave: ')

            descifrado = decipher_vigenere(mensaje, llave)

            print('\nMensaje descifrado:')
            print(descifrado)

        elif opcion == '3':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
