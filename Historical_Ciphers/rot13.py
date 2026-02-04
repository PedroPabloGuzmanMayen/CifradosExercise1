from caesar import cipher_caesar, decipher_caesar

def cipher_rot13(message):
    """
    Cifra un mensaje utiliando la técnica ROT13, para ello utiliza la función de cifrado césar del archivo caesar.py utilizando un shift de 13
    
    Args:
        message (str): El mensaje a cifrar.

    Returns:
        mensaje final: el mensaje cifrado en rot13 
    """
    return cipher_caesar(message, 13)

def decihper_rot13(message):
    """
    Descifra un mensaje utiliando la técnica ROT13, para ello utiliza la función de cifrado césar del archivo caesar.py utilizando un shift de 13
    
    Args:
        message (str): El mensaje a descifrar.

    Returns:
        mensaje final: el mensaje descifrado en rot13 
    """
    return decipher_caesar(message, 13)

if __name__ == '__main__':
    while True:
        print('\n=== Cifrado ROT13 ===')
        print('1) Cifrar mensaje')
        print('2) Descifrar mensaje')
        print('3) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el mensaje a cifrar: ')
            resultado = cipher_rot13(mensaje)

            print('\nMensaje cifrado (ROT13):')
            print(resultado)

        elif opcion == '2':
            mensaje = input('\nIngresa el mensaje a descifrar: ')
            resultado = decihper_rot13(mensaje)

            print('\nMensaje descifrado (ROT13):')
            print(resultado)

        elif opcion == '3':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
