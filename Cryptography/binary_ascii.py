from utils import divide_binary_string, binary_string_to_decimal

def binary_to_ascii(binary):
    """
    Convierte una cadena binaria a caracteres ascii, primero divide la cadena en grupos de 8,
    después recorre cada grupo de 8 números, los convierte a decimal y en base a eso obtiene
    el caracter correspondiente
    
    Args:
        binary(str): la cadena binaria que se quiere convertir a ascii

    Returns:
        final: la cadena en ascii
    """
    if len(binary) % 8 != 0:
        characters = divide_binary_string(binary[:-(len(binary) % 8)],8)
    else:
        characters = divide_binary_string(binary,8)
    final = ''
    for i in characters:
        final += chr(binary_string_to_decimal(i))

    return final


if __name__ == '__main__':
    while True:
        print('\n=== Binario a ASCII ===')
        print('1) Convertir binario a ASCII')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            binario = input('\nIngresa la cadena binaria: ')

            try:
                resultado = binary_to_ascii(binario)
                print('\nResultado en ASCII:')
                print(resultado)
            except Exception as e:
                print('\nError al convertir el binario:')
                print(e)

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')

