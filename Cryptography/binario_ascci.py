from utils import number_to_binary, cast_binary

def ascii_binary(message):
    """
    Convierte una cadena en ascii a binario, primero obtiene el valor numérico del caracter con la función
    ord, luego tranforma ese valor a binario y finalmente agrega los 0's necesarios para que la cadena
    binaria tenga 8 dígitos
    
    Args:
        message (str): el mensaje ascii para convertir a binario

    Returns:
        final: la cadena binaria
    """
    final = ''

    for i in message:
        binary = cast_binary(8, number_to_binary(int(ord(i))))
        final += binary

    return final

if __name__ == '__main__':
    while True:
        print('\n=== ASCII a Binario ===')
        print('1) Convertir ASCII a binario')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el texto en ASCII: ')

            binario = ascii_binary(mensaje)

            print('\nResultado en binario:')
            print(binario)

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
