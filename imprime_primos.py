def divisivel(x,y):
    div = False

    if x%y == 0:
        div  = True
    return div

def primo(numero):
    quantas_vezes_e_divisivel = 0
    i = 1
    primo = False

    while i <= numero and quantas_vezes_e_divisivel <= 2:
        if divisivel(numero, i):
            print(numero, i, 'divisivel')
            quantas_vezes_e_divisivel += 1
        i += 1

    if quantas_vezes_e_divisivel <= 2:
        primo = True

    return primo

def imprime_primos(n):
    for i in range(1, n+1):
        if primo(i):
            print(i)
#----------------------------------------------

x = int(input('Forneça um n°: '))

print('')

imprime_primos(x)
