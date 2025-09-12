numero = int(input("Digite um número inteiro positivo: "))
print()
for i in range(numero, 0, -1):
    if i % 2 != 0:
        print(i, end=" ")
print()
