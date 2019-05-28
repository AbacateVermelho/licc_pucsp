def inverter(frase):
    tam = len(frase)
    for i in range(tam -1, -1, -1):
        print(frase[i])

frase = input('Forneça a frase que deseja inverter: ')

inverter(frase)
