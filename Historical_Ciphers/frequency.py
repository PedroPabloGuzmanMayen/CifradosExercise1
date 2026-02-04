import matplotlib.pyplot as plt
import os

def frequency_analysis(message):
    """
    Esta función toma un mensaje e indica cuáles letras son más frecuentes. Guarda una imagen PNG con un gráfico de barras 
    con la frecuencia de cada letra e imprime en pantalla la frecuencia
    
    Args:
        message (str): El mensaje a analizar.
    
    Returns:
        La gráfica png y la tabla impresa en consola. 
    """
    freq = {}
    for i in message:
        if i.isalpha():
            freq[i] = freq.get(i, 0) + 1

    fig, ax = plt.subplots()
    ax.bar(freq.keys(), freq.values())
    ax.set_title('Frequency by letter')
    ax.set_xlabel('Letter')
    ax.set_ylabel('Frequency')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMG_DIR = os.path.join(BASE_DIR, 'images')

    os.makedirs(IMG_DIR, exist_ok=True)

    plt.savefig(os.path.join(IMG_DIR, message + 'frequency.png'))
    plt.close()

    print(f'{'Letra':<8}{'Frecuencia':<10}')
    print('-' * 18)
    for letter, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f'{letter:<8}{count:<10}')

if __name__ == '__main__':
    while True:
        print('\n=== Análisis de Frecuencia ===')
        print('1) Analizar mensaje')
        print('2) Salir')

        opcion = input('Elige una opción: ')

        if opcion == '1':
            mensaje = input('\nIngresa el mensaje a analizar: ')

            print('\nFrecuencia de letras:\n')
            frequency_analysis(mensaje)

            print('\n Se ha guardado la gráfica en ./images/frequency.png')

        elif opcion == '2':
            print('\nSaliendo del programa...')
            break

        else:
            print('\n Opción inválida, intenta de nuevo.')
