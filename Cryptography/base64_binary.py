from utils import BASE64_ALPHABET, number_to_binary, cast_binary

def base64_bin(message):
    """
    Convierte una cadena en base64 a binario
    
    Args:
        message (str): el mensaje en base64 a convertir en binario

    Returns:
        final: el mensaje en binario
    """
    final = ''
    for j in message:
        if j == '=':
            continue
        final += cast_binary(6, number_to_binary(BASE64_ALPHABET.index(j)))

    return final

if __name__ == '__main__':
    while True:
        print('\n=== Base64 a Binario ===')
        print('1) Convertir Base64 a binario')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el texto en Base64: ')

            binario = base64_bin(mensaje)

            print('\nResultado en binario:')
            print(binario)

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
