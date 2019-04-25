def frase_favorita(letra, frase):
    contador = 0
    i = 0
    tamanho = len(frase)

    while i < tamanho:
        if frase[i].lower() == letra.lower():
            contador += 1

        i += 1

    print('Sua letra favorita é a letra {} e ela aparece {} vezes na frase "{}"'.format(letra.upper(), contador, frase))

letra = input('Forneça sua letra favorita: ')
frase = input('Forneça uma frase: ')

frase_favorita(letra, frase)
