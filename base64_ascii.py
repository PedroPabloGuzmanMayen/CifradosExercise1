from base64_binary import base64_bin
from binary_ascii import binary_to_ascii

def base64_ascii(base64):

    return binary_to_ascii(base64_bin(base64))
    

print(base64_ascii('SGFiaWEgdW5hIHZleiB1biByZWlubyBlbmNhbnRhZG8='))