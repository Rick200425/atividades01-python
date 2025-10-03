def analisar_lista(lista):
    result = []
    result.append(sum(lista))
    result.append(max(lista))

    minha_tupla = tuple(result)

    return minha_tupla

print(analisar_lista([10, 15, 20, 25]))