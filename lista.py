def lista_numeros():
    lista = [10, 12, 14, 16, 18, 20]

    lista.append(22) #APPEND ADICIONA ELEMENTO NA LISTA
    lista.append(24)

    tam = len(lista) #TAM É TAMANHO DA LISTA, LEN VAI CONTAR QUANTOS ELEMENTOS TEM

    print('Lista: ', lista)
    print('')

    for i in range(0, tam):
        print('{}° elemento da sequência: {}'.format(i+1, lista[i]))



def lista_nomes():
    lista_nomes = ['Ricardo', 'Isabela', 'Clayton']
    tam = len(lista_nomes)

    for i in range(0, tam):
        print(lista_nomes[i])

lista_numeros()
print('')
lista_nomes()
