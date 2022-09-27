def hebb_rule(entradas):
     print(f'{"Entrada":^8} {"Target":^16}{"Mudança de pesos":^15}{"Pesos":^22}')
     w1, w2, b = 0, 0, 0
     print(' ' * 45, f'({w1:2}, {w2:2}, {b:2})')
     for x1, x2, y in entradas:
         w1 = w1 + x1 * y
         w2 = w2 + x2 * y
         b = b + y
         print(f'({x1:2}, {x2:2})        {y:2}        ({x1*y:2}, {x2*y:2}, {y:2})        ({w1:2}, {w2:2}, {b:2})')


AND = {
    'entrada': [
        [ 1, 1, 1],
        [ 1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1]
    ]
}

print('Hebb AND com entrada bipolar')
hebb_rule(AND['entrada'])