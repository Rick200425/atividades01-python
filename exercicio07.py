menor = None
for i in range(7):
    num = int(input(f'Digite o {i+1}º número: '))
    if menor is None or num < menor:
        menor = num
print('O menor número digitado foi:', menor)        
