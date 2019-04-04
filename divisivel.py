#Descobrir se x é divísivel por y

def divisivel(x,y):
    if x%y == 0:
        print('True')


    else:
        print('False')

#---------------------------------
print('Descubra se um número é divisível por outro.')

print('')

x = int(input('Forneça o 1° número: '))
y = int(input('Forneça o 2° número: '))

print('')

divisivel(x,y)
