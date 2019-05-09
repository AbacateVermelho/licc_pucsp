a = 0
lista = []
lista_nome = []

while a < 10:
    nome = input('Forneça um nome: ')
    lance = input('Forneça um lance: ')
    a += 1
    lista.append(lance)
    lista_nome.append(nome)
    print('')

ordem_lista = lista.index(max(lista))


print('Nome do ganhador: ', lista_nome[ordem_lista])
print('Valor do lance: ', max(lista))

