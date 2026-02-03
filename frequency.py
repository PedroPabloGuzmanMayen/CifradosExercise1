import matplotlib.pyplot as plt

def frequency_analysis(message):

    freq = {}
    for i in message:
        if i.isalpha():
            freq[i] = freq.get(i, 0) + 1

    fig, ax = plt.subplots()
    ax.bar(freq.keys(), freq.values())
    ax.set_title('Frequency by letter')
    ax.set_xlabel('Letter')
    ax.set_ylabel('Frequency')
    plt.savefig("frequency.png")
    plt.close()

    print(f"{'Letra':<8}{'Frecuencia':<10}")
    print("-" * 18)
    for letter, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter:<8}{count:<10}")


frequency_analysis('Hello World')