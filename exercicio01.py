numeros = [0, 1, 2, 3, 4, 5]

while True:

    numero = int(input("Digite um número entre 0 e 5: "))

    if numero in numeros:
        print(f"O número {numero} é valido!")
        break
    else:
        print("ERRO!!! Número invalido!")
