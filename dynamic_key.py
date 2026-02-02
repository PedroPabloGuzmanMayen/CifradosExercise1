import random
import string
from xor import binary_xor
from binario_ascci import ascii_binary
from binary_ascii import binary_to_ascii

def generate_key(size):
    char_string = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(char_string) for _ in range(size))
    return key

def dynamic_cipher(message):

    key = generate_key(len(message))
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key)
    bin_xor = binary_xor(bin_message, bin_key)

    return binary_to_ascii(bin_xor)

def static_cipher(message, key_size):

    key = generate_key(key_size)
    bin_message = ascii_binary(message)
    bin_key = ascii_binary(key)
    if len(bin_message) != len(bin_key):
        bin_key = (bin_key *((len(bin_message) // len(bin_key) ) +1))[:len(bin_message)]
    bin_xor = binary_xor(bin_message, bin_key)
    return binary_to_ascii(bin_xor)


print(f'Cifrado estáfico: {static_cipher('Arbol', 3)}')