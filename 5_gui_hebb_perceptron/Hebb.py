def hebb_rule(entradas):
    print(f'{"Entrada":^8} {"Target":^16}{"Mudança de pesos":^15}{"Pesos":^22}')
    w1, w2, b = 0, 0, 0
    print(' ' * 45, f'({w1:2}, {w2:2}, {b:2})')
    for x1, x2, y in entradas:
        w1 = w1 + x1 * y
        w2 = w2 + x2 * y
        b = b + y
        print(f'({x1:2}, {x2:2})        {y:2}        ({x1*y:2}, {x2*y:2}, {y:2})        ({w1:2}, {w2:2}, {b:2})')
    hebb_testes(w1,w2,b,entradas)

def hebb_testes(w1,w2,b,entradas):
    print("\nSaídas:")
    contador=0
    for x1,x2,y in entradas:
        E = b + ((x1 * w1) + (x2 * w2))
        if (E > 0):
            saida = 1
        elif (E == 0):
            saida = 0
        elif (E < 0):
            saida = -1
        print(saida)
        if (saida == y):
            contador = contador + 1
    taxaacert = (contador / 4) * 100
    print("\nTaxa de acerto: ", taxaacert, "%")
    return 0
