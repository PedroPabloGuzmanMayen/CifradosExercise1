from utils import BASE64_ALPHABET, divide_binary_string, binary_string_to_decimal

def binary_to_base64(binary):
    """
    Toma una cadena binaria y la convierte a base64. Primero divide la cadena en grupos de 6,
    después convierte cada grupo a decimal y obtiene su valor en el alfabeto base 64. Finalmente
    agrega el padding correspondiente
    
    Args:
        binary(str): la cadena binaria que se quiere convertir a base64

    Returns:
        final: la cadena en base64
    """
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

if __name__ == '__main__':
    while True:
        print('\n=== Binario a Base64 ===')
        print('1) Convertir binario a Base64')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            binario = input('\nIngresa la cadena binaria: ')

            try:
                resultado = binary_to_base64(binario)
                print('\nResultado en Base64:')
                print(resultado)
            except Exception as e:
                print('\n Error al convertir el binario:')
                print(e)

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
