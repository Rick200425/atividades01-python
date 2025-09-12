comeco = int(input('Digite o primeiro número: '))
fim = int(input('Digite o segundo número: '))

pares = []
for i in range(comeco, fim+1):
    if i % 2 == 0:
        pares.append(i)


print('Números pares no intervalo', pares)
       