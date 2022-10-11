import Hebb as hebb
import Perceptron as perc
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox, QComboBox

def on_botaotesteHebb_clicked():
    peso1=window.findChild(QLabel, 'peso1')
    w1=int(peso1.text())
    peso2=window.findChild(QLabel, 'peso2')
    w2=int(peso2.text())
    pesob=window.findChild(QLabel, 'pesob')
    b=int(pesob.text())
    hebb13= window.findChild(QComboBox, 'hebb13')
    h13=hebb13.currentText()
    hebb14= window.findChild(QComboBox, 'hebb14')
    h14=hebb14.currentText()
    hebb15= window.findChild(QComboBox, 'hebb15')
    h15=hebb15.currentText()
    hebb16= window.findChild(QComboBox, 'hebb16')
    h16=hebb16.currentText()
    hebb17= window.findChild(QComboBox, 'hebb17')
    h17=hebb17.currentText()
    hebb18= window.findChild(QComboBox, 'hebb18')
    h18=hebb18.currentText()
    hebb19= window.findChild(QComboBox, 'hebb19')
    h19=hebb19.currentText()
    hebb20= window.findChild(QComboBox, 'hebb20')
    h20=hebb20.currentText()
    AND = {
    'teste': [
        [ h13, h14],
        [ h15, h16],
        [ h17, h18],
        [ h19, h20]
    ]}
    hebb.hebb_testes(w1,w2,b,AND['teste'])
    saida1,saida2,saida3,saida4=hebb.hebb_testes(w1,w2,b,AND['teste'])
    saida1=str(saida1)
    saida2=str(saida2)
    saida3=str(saida3)
    saida4=str(saida4)
    lab1=window.findChild(QLabel, 'saida1')
    lab1.setText(saida1)
    lab2=window.findChild(QLabel, 'saida2')
    lab2.setText(saida2)
    lab3=window.findChild(QLabel, 'saida3')
    lab3.setText(saida3)
    lab4=window.findChild(QLabel, 'saida4')
    lab4.setText(saida4)


def on_botaotreinoHebb_clicked():
    hebb1= window.findChild(QComboBox, 'hebb1')
    h1=hebb1.currentText()
    hebb2= window.findChild(QComboBox, 'hebb2')
    h2=hebb2.currentText()
    hebb3= window.findChild(QComboBox, 'hebb3')
    h3=hebb3.currentText()
    hebb4= window.findChild(QComboBox, 'hebb4')
    h4=hebb4.currentText()
    hebb5= window.findChild(QComboBox, 'hebb5')
    h5=hebb5.currentText()
    hebb6= window.findChild(QComboBox, 'hebb6')
    h6=hebb6.currentText()
    hebb7= window.findChild(QComboBox, 'hebb7')
    h7=hebb7.currentText()
    hebb8= window.findChild(QComboBox, 'hebb8')
    h8=hebb8.currentText()
    hebb9= window.findChild(QComboBox, 'hebb9')
    h9=hebb9.currentText()
    hebb10= window.findChild(QComboBox, 'hebb10')
    h10=hebb10.currentText()
    hebb11= window.findChild(QComboBox, 'hebb11')
    h11=hebb11.currentText()
    hebb12= window.findChild(QComboBox, 'hebb12')
    h12=hebb12.currentText()
    AND = {
    'entrada': [
        [ h1, h2, h9],
        [ h3, h4, h10],
        [ h5, h6, h11],
        [ h7, h8, h12]
    ]}
    hebb.hebb_rule(AND['entrada'])
    w1,w2,b=hebb.hebb_rule(AND['entrada'])
    pes1=str(w1)
    pes2=str(w2)
    pesb=str(b)
    peso1=window.findChild(QLabel, 'peso1')
    peso1.setText(pes1)
    peso2=window.findChild(QLabel, 'peso2')
    peso2.setText(pes2)
    pesob=window.findChild(QLabel, 'pesob')
    pesob.setText(pesb)
    calcular_teste= window.findChild(QPushButton, 'botaotesteHebb')
    calcular_teste.clicked.connect(on_botaotesteHebb_clicked)

def on_botaotestePercep_clicked():
    peso1=window.findChild(QLabel, 'peso1percep')
    w0=int(peso1.text())
    peso2=window.findChild(QLabel, 'peso2percep')
    w1=int(peso2.text())
    pesob=window.findChild(QLabel, 'pesobpercep')
    wb=int(pesob.text())
    bi=window.findChild(QLabel, 'bias')
    bias=int(bi.text())
    percep13= window.findChild(QComboBox, 'percep13')
    p13=percep13.currentText()
    percep14= window.findChild(QComboBox, 'percep14')
    p14=percep14.currentText()
    percep15= window.findChild(QComboBox, 'percep15')
    p15=percep15.currentText()
    percep16= window.findChild(QComboBox, 'percep16')
    p16=percep16.currentText()
    percep17= window.findChild(QComboBox, 'percep17')
    p17=percep17.currentText()
    percep18= window.findChild(QComboBox, 'percep18')
    p18=percep18.currentText()
    percep19= window.findChild(QComboBox, 'percep19')
    p19=percep19.currentText()
    percep20= window.findChild(QComboBox, 'percep20')
    p20=percep20.currentText()
    AND = {
    'entradaTestes': [
        [ p13, p14],
        [ p15, p16],
        [ p17, p18],
        [ p19, p20]
    ]
    }
    saida1,saida2,saida3,saida4= perc.TestesAND(w0,w1,wb,bias,AND['entradaTestes'])
    saida1=str(saida1)
    saida2=str(saida2)
    saida3=str(saida3)
    saida4=str(saida4)
    lab1=window.findChild(QLabel, 'saida1percep')
    lab1.setText(saida1)
    lab2=window.findChild(QLabel, 'saida2percep')
    lab2.setText(saida2)
    lab3=window.findChild(QLabel, 'saida3percep')
    lab3.setText(saida3)
    lab4=window.findChild(QLabel, 'saida4percep')
    lab4.setText(saida4)


def on_botaotreinoPercep_clicked():
    percep1= window.findChild(QComboBox, 'percep1')
    p1=int(percep1.currentText())
    percep2= window.findChild(QComboBox, 'percep2')
    p2=int(percep2.currentText())
    percep3= window.findChild(QComboBox, 'percep3')
    p3=int(percep3.currentText())
    percep4= window.findChild(QComboBox, 'percep4')
    p4=int(percep4.currentText())
    percep5= window.findChild(QComboBox, 'percep5')
    p5=int(percep5.currentText())
    percep6= window.findChild(QComboBox, 'percep6')
    p6=int(percep6.currentText())
    percep7= window.findChild(QComboBox, 'percep7')
    p7=int(percep7.currentText())
    percep8= window.findChild(QComboBox, 'percep8')
    p8=int(percep8.currentText())
    percep9= window.findChild(QComboBox, 'percep9')
    p9=int(percep9.currentText())
    percep10= window.findChild(QComboBox, 'percep10')
    p10=int(percep10.currentText())
    percep11= window.findChild(QComboBox, 'percep11')
    p11=int(percep11.currentText())
    percep12= window.findChild(QComboBox, 'percep12')
    p12=int(percep12.currentText())
    AND = {
    'entradaTreinamento': [
        [ p1, p2, p9],
        [ p3, p4, p10],
        [ p5, p6, p11],
        [ p7, p8, p12]
    ],}
    perc.TreinamentoAND(AND['entradaTreinamento'])
    w0,w1,b,bias=perc.TreinamentoAND(AND['entradaTreinamento'])
    pes1=str(w0)
    pes2=str(w1)
    pesb=str(b)
    bi=str(bias)
    peso1=window.findChild(QLabel, 'peso1percep')
    peso1.setText(pes1)
    peso2=window.findChild(QLabel, 'peso2percep')
    peso2.setText(pes2)
    pesob=window.findChild(QLabel, 'pesobpercep')
    pesob.setText(pesb)
    biast=window.findChild(QLabel, 'bias')
    biast.setText(bi)
    calcular_teste_percep= window.findChild(QPushButton, 'botaotestePercep')
    calcular_teste_percep.clicked.connect(on_botaotestePercep_clicked)



QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
app = QApplication([])
window = uic.loadUi("FrontHebbPercep.ui")

calcular_treino = window.findChild(QPushButton, 'botaotreinoHebb')
calcular_treino.clicked.connect(on_botaotreinoHebb_clicked)

calcular_treino_percep = window.findChild(QPushButton, 'botaotreinoPercep')
calcular_treino_percep.clicked.connect(on_botaotreinoPercep_clicked)

window.show()
app.exec_()
