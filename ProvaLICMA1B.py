def verificar_ano(data):
    ano = data[7]+data[8]
    anoi = int(ano)
    print('Ano: ',ano)

    
with open('series.csv', 'r') as file:
    for line in file:
        lista = line.split(',')
        if lista[5] == '10' and lista[6] == '10\n':
            print(line)

    for line in file:
        verificar_ano(lista[3])
        if ano < 9:
            soma = int(lista[2]) + soma
            print(soma)
            
            
            
        

    


            
