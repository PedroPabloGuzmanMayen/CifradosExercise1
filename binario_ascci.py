def ascii_binary(message):
    final = ""

    for i in message:
        binary = cast_binary(8, number_to_binary(int(ord(i))))
        final += binary

    return final


def number_to_binary(number):
    if number == 0:
        return '0'
    if number == 1:
        return '1'
    return number_to_binary(int(number/2)) + str(number % 2)


def cast_binary(base, bin_number):
    if len(bin_number) < base:
        return bin_number.zfill(base)
    return bin_number

print(f'Hola como estas es: {ascii_binary('Hola como estas')}')