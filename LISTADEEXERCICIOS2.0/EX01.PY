candidatos = {
    10: {"Nome": "Candidato A"},
    20: {"Nome": "Candidato B"},
    30: {"Nome": "Candidato C"},
    98: {"Nome": "Voto Nulo"},
    99: {"Nome": "Voto em Branco"},
}

voto = int(input("Digite o número do seu candidato: "))

while voto not in candidatos:
    voto = int(input("Codigo invalido! Digite o número de seu candidato: "))

print(f"Votação realizada com sucesso! você votou {candidatos[voto]["Nome"]}")
