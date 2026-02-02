from utils import BASE64_ALPHABET, number_to_binary, cast_binary

def base64_bin(message):
    final = ''
    for j in message:
        if j == '=':
            continue
        final += cast_binary(6, number_to_binary(BASE64_ALPHABET.index(j)))

    return final


