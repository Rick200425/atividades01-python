def contar_vogais(texto):
    contador = 0

    vogais = ('aeiouáéíóúàèìòùâêîôûãõäëïöü')
    for v in texto:
        if v in vogais:
            contador +=1

    return contador

texto = str(input('Escreva uma palavra ou uma frase: ')).lower()
numero_vogais = contar_vogais(texto)

print(f'A streing "{texto}" possui {numero_vogais} vogais.')