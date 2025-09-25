total = 0
contador = 0

while True:
    valor = float(input("Digite o valor da despesa (0 para sair): "))

    if valor == 0:
        break

    total += valor
    contador += 1

if contador > 0:
    media = total / contador
else:
    media = 0

print("===== RESUMO =====")
print(f"Total gasto: R$ {total:.2f}")
print(f"Número de despesas: {contador}")
print(f"Valor médio por despesa: R$ {media:.2f}")
