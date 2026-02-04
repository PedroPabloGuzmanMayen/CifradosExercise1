LOWER_ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
UPPER_ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def cipher_caesar(message, shift):
    """
    Cifra un mensaje utiliando la técnica del cifrado césar
    
    Esta función toma un string y un entero y en base a eso desplaza cada letra del mensaje original para cifrarlo.
    
    Args:
        message (str): El mensaje a cifrar.
        shift (int): el desplazamiento a utlizar.
    
    Returns:
        mensaje final: el mensaje cifrado con el shift indicado. 
    """
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
    """
    Descifra un mensaje utiliando la técnica del cifrado césar
    
    Esta función toma un string y un entero y en base a eso desplaza cada letra del mensaje original para descifrarlo.
    
    Args:
        message (str): El mensaje a descifrar.
        shift (int): el desplazamiento a utlizar.
    
    Returns:
        mensaje final: el mensaje descifrado con el shift indicado. 
    """
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

if __name__ == '__main__':
    while True:
        print('\n=== Cifrado César (alfabeto español) ===')
        print('1) Cifrar mensaje')
        print('2) Descifrar mensaje')
        print('3) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el mensaje a cifrar: ')
            shift = int(input('Ingresa el desplazamiento (shift): '))

            cifrado = cipher_caesar(mensaje, shift)

            print('\nMensaje cifrado:')
            print(cifrado)

        elif opcion == '2':
            mensaje = input('\nIngresa el mensaje a descifrar: ')
            shift = int(input('Ingresa el desplazamiento (shift): '))

            descifrado = decipher_caesar(mensaje, shift)

            print('\nMensaje descifrado:')
            print(descifrado)

        elif opcion == '3':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
