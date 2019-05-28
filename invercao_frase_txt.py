def inverter(frase):
    tam = len(frase)
    for i in range(tam -1, -1, -1):
        arquivo.write(frase[i])

frase = input('Forneça a frase que deseja inverter: ')

arquivo = open('invercao_de_frases.txt', 'w')
inverter(frase)
arquivo.close() 
