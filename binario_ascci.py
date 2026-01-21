import base64

def ascii_binary(message):
    final = []
    for i in message.split(' '):
        word = []
        for j in i:
            word.append(number_to_binary(int(ord(j))))
        final.append(word)
    return final


def number_to_binary(number):
    if number == 0:
        return '0'
    if number == 1:
        return '1'
    return number_to_binary(int(number/2)) + str(number % 2)





