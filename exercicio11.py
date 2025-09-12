comeco = int(input('Digite o primeiro número: '))
fim = int(input('Digite o segundo número: '))

soma_impares = 0
for i in range(comeco, fim+1):
    if i % 2 != 0:
        soma_impares +=1


print('Soma dos números ímpares no intervalo', soma_impares)


       