def ascii_binary(message):
    final = []
    for i in message.split(' '):
        word = []
        for j in i:
            word.append(bin(int(ord(j)))[2:])
        final.append(word)
    return final

print(f"Hola is {ascii_binary("Hola como estas")} ")


