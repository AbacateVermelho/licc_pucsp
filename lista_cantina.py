lista_nome = []
lista_pedido = []
lista_valor = []
valor = 0

print('|-------------------|')
print('| Tabela de valores |')
print('|-------------------|')
print('|Bolo...........4.50|')
print('|Cafe...........4.00|')
print('|Capuccino......6.00|')
print('|Dadinho........0.50|')
print('|Salgado........4.00|')
print('|Sorvete........6.00|')
print('|Suco...........5.00|')
print('|Refrigerante...4.00|')
print('|-------------------|')
print('')


for i in range(0, 3):
    nome = input('Forneça seu nome: ')
    lista_nome.append(nome)
    pedido = input('Nome do seu pedido: ')
    lista_pedido.append(pedido)
    print('')

tam_lista = len(lista_nome)

for i in range(0, tam_lista):
    if lista_pedido[i].lower() == 'salgado':
        lista_valor.append(4.00)

    elif lista_pedido[i].lower() == 'refrigerante':
        lista_valor.append(4.50)

    elif lista_pedido[i].lower() == 'suco':
        lista_valor.append(5.00)

    elif lista_pedido[i].lower() == 'sorvete':
        lista_valor.append(6.00)

    elif lista_pedido[i].lower() == 'cafe':
        lista_valor.append(4.00)

    elif lista_pedido[i].lower() == 'capuccino':
        lista_valor.append(6.00)

    if lista_pedido[i].lower() == 'bolo':
        lista_valor.append(4.50)

    elif lista_pedido[i].lower() == 'dadinho':
        lista_valor.append(0.50)

for i in range(0, tam_lista):
    valor = lista_valor[i] + valor

for i in range(0, tam_lista):
    print('{} - {} - {}'.format(lista_nome[i], lista_pedido[i], lista_valor[i]))

print('')
print('Valor total no caixa: R$ {}'.format(valor))    
