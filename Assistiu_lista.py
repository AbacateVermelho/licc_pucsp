verdade = True

lista_assistiu = 0
lista_nao_assistiu = 0
babacas = 0

lista = []
lista2 = []

while verdade == True:

    nome = input('Forneça seu nome: ')

    if nome == 'fim':
        verdade = False
        
    assistiu = input('Já assistiu Avengers? (s) para sim e (n) para não:  ')

    
    if assistiu == 's':
        lista_assistiu += 1
        lista.append(nome)

    elif assistiu == 'n':
        lista_nao_assistiu += 1
        lista2.append(nome)

    else:
        babacas =+ 1

    print('')

print('Pessoas que já assistiu: ', lista_assistiu)
print('Pessoas que não assistiu: ', lista_nao_assistiu)
print('')

tam = len(lista)
tam2 = len(lista2)

print('Nome das pessoas que já assistiu: ')
for i in range(0, tam):
    print(lista[i])

print('')

print('Nome das pessoas que não assistiu: ')
for i in range(0, tam2):
    print(lista2[i])
