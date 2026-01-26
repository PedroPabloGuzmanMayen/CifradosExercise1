from binario_ascci import number_to_binary, cast_binary

BASE64_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def base64_bin(message):
    final = []
    for i in message.split(' '):
        word = []
        for j in i:
            word.append(cast_binary(6, number_to_binary(BASE64_ALPHABET.index(j))))
        final.append(word)

    return final

print(f'Hola como estas in base 64 binary is: {base64_bin('Como')} ')
