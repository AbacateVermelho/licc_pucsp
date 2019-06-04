texto = "Ricardo Carvalho"
texto.split(' ')

texto.replace('a', '4') #TROCAR O PRIMEIRO ELEMENTO PELO OUTRO DEPOIS DA VIRCULA.
texto.replace('ar', 'aaaarr')
texto.isnumeric() #VERIFICAR SE É NÚMERICO.

numero = '10'
numero.isnumeric() #VERIFICAR SE É NÚMERICO.

'ricardo'.capitalize() #COLOCAR LETRA MAIUSCULA NA PRIMEIRA LETRA.

'RICARDO'.lower() #COLOCAR TODAS LETRAS MINUSCULAS.


frutas = "Banana, Uva, Caqui, Batman"
print(frutas)

lista = frutas.split(',') #DIVIDE A STRING PELO CARACTER QUE O USUARIO QUISER, TRANSFERINDO EM UMA LISTA.
print(lista)


lista.pop() #.pop() remove o último elemento da lista.
print(lista)

frutas = ', '.join(lista) #TIRA DA LISTA E TRANSFORMA EM UMA STRING.
print(frutas)
