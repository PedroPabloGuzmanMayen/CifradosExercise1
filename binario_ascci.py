def ascii_binary(message):
    final = ""

    for i in message:
        binary = number_to_binary(int(ord(i)))
        if len(binary) < 8:
            binary = binary.zfill(8)
        final += binary

    return final


def number_to_binary(number):
    if number == 0:
        return '0'
    if number == 1:
        return '1'
    return number_to_binary(int(number/2)) + str(number % 2)


print(f'Hola es encoded like: {ascii_binary('Hola')} ')


