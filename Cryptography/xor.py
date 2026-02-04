def binary_xor(binary1, binary2):
    """
    Aplica XOR para 2 cadenas binarias, si no tienen el mismo tamaño entonces tira un error
    
    Args:
        binary1(str): La cadena binaria a la que se le aplciara XOR.
        binary2(str): La cadena binaria que se usará para aplicar XOR.

    Returns:
        mensaje final: la cadena resultante luego de aplicar XOR
    """
    if len(binary1) != len(binary2):
        raise ValueError("Las cadenas deben tener la misma longitud")

    final = ''
    for b1, b2 in zip(binary1, binary2):
        final += '1' if b1 != b2 else '0'

    return final


if __name__ == '__main__':
    while True:
        print('\n=== XOR Binario ===')
        print('1) Aplicar XOR')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            bin1 = input('\nIngresa la primera cadena binaria: ')
            bin2 = input('Ingresa la segunda cadena binaria: ')

            try:
                resultado = binary_xor(bin1, bin2)
                print('\nResultado del XOR:')
                print(resultado)
            except ValueError as e:
                print('\n Error:')
                print(e)

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
