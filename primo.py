#Descobrir se x é primo

def primo(x):
    contador=1
    while contador <= x:
        if x == 2:
            print('True')
            break

        elif x%2 == 1:
            contador=contador+1
            print('True')
            break

        elif x == 1:
            print('False')

        else:
            print('False')
            break
#---------------------------------------

print('Descubra se um número é primo.')

print('')

x = int(input('Digite um numero: '))


primo(x)
