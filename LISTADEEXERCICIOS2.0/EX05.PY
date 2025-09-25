frase = input("Digite uma frase: ")

vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

n_vogais = 0
n_consoantes = 0

frase = frase.lower()

for letra in frase:
    if letra in vogais:
        n_vogais += 1
    elif letra in consoantes:
        n_consoantes += 1

print(f"A frase possui {n_vogais} Vogais!")   
print(f"A frase possui {n_consoantes} Consoantes!")
    