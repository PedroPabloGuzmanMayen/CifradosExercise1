from caesar import cipher_caesar, decipher_caesar

def cipher_rot13(message):
    return cipher_caesar(message, 13)

def decihper_rot13(message):
    return decipher_caesar(message, 13)


print(cipher_rot13('Hola'))