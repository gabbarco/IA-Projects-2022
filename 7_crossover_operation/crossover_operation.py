import sys, random, string, poplib
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLineEdit, QLabel


def on_cross_pushbutton_clicked():
    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover()
        son1_label_3.setVisible(False)
        son2_label_3.setVisible(False)
    else:
        offsprings = pmx_crossover()
        son1_label_3.setVisible(True)
        son2_label_3.setVisible(True)

    son1_label_1.setText(offsprings[0])
    son1_label_2.setText(offsprings[1])
    son1_label_3.setText(offsprings[2])
    son2_label_1.setText(offsprings[3])
    son2_label_2.setText(offsprings[4])
    son2_label_3.setText(offsprings[5])


def on_method_combobox_current_text_changed():
    if method_combo_box.currentText()=="PMX":
        father_line_edit.setInputMask('AAAAAAAAAA')
        father_line_edit.setText('ABCDEFGHIJ')
        mother_line_edit.setInputMask('AAAAAAAAAA')
        mother_line_edit.setText('JHIGFEDCBA')  
    else:
        father_line_edit.setInputMask('BBBBBBBBBB')
        father_line_edit.setText('0000000000')
        mother_line_edit.setInputMask('BBBBBBBBBB')
        mother_line_edit.setText('1111111111')
    print('combo box changed')

def pmx_crossover():
    cromossomopai= father_line_edit.text()
    cromossomomae= mother_line_edit.text()
    corte1 = random.randint(0,len(cromossomopai)-2)
    corte2 = random.randint(corte1+1,len(cromossomomae)-1)
    cortepai=''
    cortemae=''
    corte1pai=''
    corte1mae=''
    corte2pai=''
    corte2mae=''
    for i in range(0,corte1):
        cortepai=cortepai+(cromossomopai[i])
        corte1mae= corte1mae+(cromossomomae[i])
    for i in range(corte1,corte2):
        cortemae=cortemae+(cromossomomae[i])
        corte1pai= corte1pai+(cromossomopai[i])
    for i in range(corte2,10):
        corte2pai=corte2pai+(cromossomopai[i])
        corte2mae= corte2mae+(cromossomomae[i])
    # Troca de caracteres repetidos
    for i in range(0,len(cortemae)):
        for j in range(0,len(cortepai)):
            if (cortemae[i]==cortepai[j]):
                cortepai=cortepai.replace(cortepai[j],corte1pai[i])
            
            if (corte1pai[i]==corte1mae[j]):
                corte1mae=corte1mae.replace(corte1mae[j],cortemae[i])
        for h in range(0,len(corte2pai)):
            if (cortemae[i]==corte2pai[h]):
                corte2pai=corte2pai.replace(corte2pai[h],corte1pai[i])
            
            if (corte1pai[i]==corte2mae[h]):
                corte2mae=corte2mae.replace(corte2mae[h],cortemae[i])
    # Esta função está retornando 6 valores.
    # Ao criar o corpo da função você deve ordená-los de acordo com
    # as linhas 17 a 22 deste arquivo.
    return cortepai,cortemae,corte2pai,corte1mae,corte1pai,corte2mae


def simple_cut_crossover():
    cromossomopai= father_line_edit.text()
    cromossomomae= mother_line_edit.text()
    corte= random.randint(0,len(cromossomopai)-1)
    cortepai=''
    cortemae=''
    corte1pai=''
    corte1mae=''
    for i in range(0,corte):
        cortepai=cortepai+(cromossomopai[i])
        corte1mae= corte1mae+(cromossomomae[i])
    for i in range(corte,10):
        cortemae= cortemae+(cromossomomae[i])
        corte1pai= corte1pai+(cromossomopai[i])
    return cortepai,cortemae,'',corte1mae,corte1pai,''


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    # Loading widgets elements from ui file
    window = uic.loadUi("crossover_operation.ui")
    window.show()

    # Getting widgets elements
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    son1_label_1 = window.findChild(QLabel, 'son1Label1')
    son1_label_2 = window.findChild(QLabel, 'son1Label2')
    son1_label_3 = window.findChild(QLabel, 'son1Label3')
    son2_label_1 = window.findChild(QLabel, 'son2Label1')
    son2_label_2 = window.findChild(QLabel, 'son2Label2')
    son2_label_3 = window.findChild(QLabel, 'son2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')

    # Connecting
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)

    sys.exit(app.exec_())
