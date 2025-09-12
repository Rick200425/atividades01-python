popA = 90000
popB = 250000
anos = 0
cres_a = 1.035
cres_b = 1.012

while popA <= popB:

    popA *= cres_a
    popB *= cres_b
    anos +=1


print(f'Serão necessarios {anos} anos para que a cidade A ({int(popA)}) ultrapasse a polução da cidade B ({int(popB)}) ')


