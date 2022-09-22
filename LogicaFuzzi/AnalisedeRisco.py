from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox


def on_CalcularpushButton_clicked():
    risco_label.setVisible(True)
    calcular_btn.setVisible(False)
    dinheiro=  valor_dinheiro.value()

    udP= (dinheiro-50)/(30-50)
    if dinheiro<=30:
        udP=1
    elif dinheiro>=50:
        udP=0
    udR1= (dinheiro-30)/(50-30)
    udR2= (dinheiro-70)/(50-70)
    if dinheiro<50 and dinheiro>30 :
        udR= udR1
    elif dinheiro==50 :
        udR=1
    elif dinheiro<=30 or dinheiro>=70:
        udR=0   
    else:
        udR= udR2
    udA= (dinheiro-50)/(70-50)
    if dinheiro<=50:
        udA=0
    elif dinheiro>=70:
        udA=1    
    
    pessoas= num_pessoas.value()
    
    upI= (pessoas-70)/(30-70)
    if pessoas>=70:
        upI=0
    elif pessoas<=30:
        upI=1
    upS= (pessoas-30)/(70-30)
    if pessoas>=70:
        upS=1
    elif pessoas<=30:
        upS=0
    
    #Se UdP OU UpI ENTÃO UrA
    if udP>=upI:
        urA1=udP
    else:
        urA1=upI

    #Se UdP E UpS ENTÃO UrA
    if udP<=upS:
        urA2=udP
    else:
        urA2=upS
    
    if urA1>=urA2:
        urA=urA1
    else:
        urA=urA2
    
    #Se UdR E UpS ENTÃO UrM
    if udR<=upS:
        urM=udR
    else:
        urM=upS

    #Se UdA E UpS ENTÃO UrB
    if udA<=upS:
        urB=udA
    else:
        urB=upS

    kog= ((10+20+30)*urB+(40+50+60)*urM+(70+80+90)*urA)/(urB*3+urM*3+urA*3)

    if kog<35:
        risco_label.setText("O projeto se classifica na categoria de risco baixo\nCentro geométrico= "+str(kog))
    elif kog>=35 and kog<65:
        risco_label.setText("O projeto se classifica na categoria de risco médio\nCentro geométrico= "+str(kog))
    else:
        risco_label.setText("O projeto se classifica na categoria de risco alto\nCentro geométrico= "+str(kog))
    
    
    print("----------------------------------------")


def on_action_reset_triggered():
    risco_label.setVisible(False)
    calcular_btn.setVisible(True)



if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi("LogFuzzi.ui")

    risco_label = window.findChild(QLabel, 'riscoLabel')
    risco_label.setVisible(False)

    calcular_btn = window.findChild(QPushButton, 'CalcularpushButton')
    calcular_btn.clicked.connect(on_CalcularpushButton_clicked)

    valor_dinheiro = window.findChild(QSpinBox, 'DinheiroBox')

    num_pessoas = window.findChild(QSpinBox, 'PessoaBox')

    action_reset = window.findChild(QAction, 'actionReset')
    action_reset.triggered.connect(on_action_reset_triggered)

    window.show()

    app.exec_()