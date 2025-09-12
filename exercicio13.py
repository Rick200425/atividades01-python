positivos = 0
negativos = 0
zeros = 0

for i in range(8):
    num = int(input(f"Digite o {i+1}º número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zeros)