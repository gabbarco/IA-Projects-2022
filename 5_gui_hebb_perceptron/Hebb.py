from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox, QComboBox

def hebb_rule(entradas):
    w1, w2, b = 0, 0, 0
    for x1, x2, y in entradas:
        x1=int(x1)
        x2=int(x2)
        y=int(y)
        w1 = w1 + x1 * y
        w2 = w2 + x2 * y
        b = b + y
    return w1,w2,b

def hebb_testes(w1,w2,b,entradas):
    sai=[]
    for x1,x2 in entradas:
        x1=int(x1)
        x2=int(x2)
        E = b + ((x1 * w1) + (x2 * w2))
        if (E > 0):
            saida = 1
        elif (E <= 0):
            saida = -1
        sai.append(saida)
    saida1=sai[0]
    saida2=sai[1]
    saida3=sai[2]
    saida4=sai[3]
    return saida1,saida2,saida3,saida4