n = int(input("Digite um número inteiro positivo: "))

while n < 0:
    print("Número invalido!!! Digite um número maior ou igual a zero!")
    n = int(input("Digite um número inteiro positivo: "))

fatorial = 1

if n == 0:
        fatorial = 1
else:
    for i in range(1, n + 1):
            fatorial = fatorial * i


print(f"{n}! = {fatorial}")

            