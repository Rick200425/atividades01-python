pao = 0.75
broa = 1.75
refrigerante = 12.00

qtd_pao = int(input("Quantos pães você deseja: "))
qtd_broa = int(input("Quantas broas você deseja: "))
qtd_refrigerante = int(input("Quantos refrigerantes você deseja: "))

total_pao = pao * qtd_pao
toal_broa = broa * qtd_broa
total_refrigerante = refrigerante * qtd_refrigerante

total = total_pao + toal_broa + total_refrigerante

print(f"O total é R${total}")