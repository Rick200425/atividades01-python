produto = 1
soma = 0
for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    produto *= num
    soma += num
media = soma / 6
print("Produto dos números:", produto)
print("Média aritmética:", media)
