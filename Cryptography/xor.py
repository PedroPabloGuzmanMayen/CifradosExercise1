def binary_xor(binary1, binary2):
    if len(binary1) != len(binary2):
        raise ValueError("Las cadenas deben tener la misma longitud")

    final = ''
    for b1, b2 in zip(binary1, binary2):
        final += '1' if b1 != b2 else '0'

    return final
