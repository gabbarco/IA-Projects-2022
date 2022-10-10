import Hebb as hebb
import Perceptron as perc

AND = {
    'entrada': [
        [ 1, 1, 1],
        [ 1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1]
    ]
}

print('Hebb AND com entrada bipolar')
hebb.hebb_rule(AND['entrada'])