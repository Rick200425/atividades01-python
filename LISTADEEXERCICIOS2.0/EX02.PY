total = 0
qtd = 1

while True:
     preço_produto = float(input(f"Digite o valor do {qtd}º produto: "))
     if preço_produto == 0:
          break
     elif preço_produto < 0:
          print("Valor invalido, digite valores maiores que 0: ")
     else:
          qtd += 1
          total += preço_produto
print(f" O valor total da sua compra é de: R$ {total:.2f}")


