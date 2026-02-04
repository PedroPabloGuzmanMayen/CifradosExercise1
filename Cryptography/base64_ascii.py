from base64_binary import base64_bin
from binary_ascii import binary_to_ascii

def base64_ascii(base64):
    """
    Convierte una cadena en base64 a caracteres ascii, primero convierte la cadena a binario y en base a eso 
    transforma a caracteres ascii
    
    Args:
        base64(int): el mensaje en base64 que queremos convertir en ascii

    Returns:
        final: la cadena original en ascii
    """
    return binary_to_ascii(base64_bin(base64))
    
if __name__ == '__main__':
    while True:
        print('\n=== Base64 a ASCII ===')
        print('1) Convertir Base64 a ASCII')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            base64_msg = input('\nIngresa el texto en Base64: ')

            try:
                resultado = base64_ascii(base64_msg)
                print('\nMensaje en ASCII:')
                print(resultado)
            except Exception as e:
                print('\n Error al convertir el Base64:')
                print(e)

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')

