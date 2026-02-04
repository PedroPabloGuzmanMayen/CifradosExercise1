import random
import string
from xor import binary_xor
from binario_ascci import ascii_binary
from binary_ascii import binary_to_ascii

def generate_key(size):
    """
    Genera una llave para cifrar mensajes, utliza random para generar una cadena ascii al azar
    
    Args:
        size (int): El tamaño de la llave que vamos a generar

    Returns:
        key: la llave generada
    """
    char_string = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(char_string) for _ in range(size))
    return key

def dynamic_cipher(message):
    """
    Genera una llave con la función anterior del mismo tamaño que el mensaje, convierte el mensaje y la llave a binary, aplica xor y el
    resultado lo convierte a ascii
    
    Args:
        message(str): el mensaje a cifrar

    Returns:
        final: el mensaje en ascii luego de aplicar xor
    """
    key = generate_key(len(message))
    print(f'LLave:{key} ')
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key)
    bin_xor = binary_xor(bin_message, bin_key)

    return binary_to_ascii(bin_xor)

def static_cipher(message, key_size):
    """
    Genera una llave con la función de generate_key con un tamaño específico, convierte el mensaje y la llave a binary, aplica xor y el
    resultado lo convierte a ascii
    
    Args:
        message(str): el mensaje a cifrar

    Returns:
        final: el mensaje en ascii luego de aplicar xor
    """

    key = generate_key(key_size)
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key)
    if len(bin_message) != len(bin_key):
        bin_key = (bin_key *((len(bin_message) // len(bin_key) ) +1))[:len(bin_message)]
    bin_xor = binary_xor(bin_message, bin_key)
    return binary_to_ascii(bin_xor)

if __name__ == '__main__':
    while True:
        print('\n=== Cifrado XOR ===')
        print('1) Cifrado dinámico (clave del tamaño del mensaje)')
        print('2) Cifrado estático (clave repetida)')
        print('3) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el mensaje a cifrar: ')

            cifrado = dynamic_cipher(mensaje)

            print('\nMensaje cifrado (XOR dinámico):')
            print(cifrado)
            print('\n Guarda la clave si quieres poder descifrar después.')

        elif opcion == '2':
            mensaje = input('\nIngresa el mensaje a cifrar: ')
            key_size = int(input('Ingresa el tamaño de la clave: '))

            cifrado = static_cipher(mensaje, key_size)

            print('\n Mensaje cifrado (XOR estático):')
            print(cifrado)
            print('\n Guarda la clave si quieres poder descifrar después.')

        elif opcion == '3':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
