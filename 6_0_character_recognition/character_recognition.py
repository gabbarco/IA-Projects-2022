import sys
from gui import Gui
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    gui = Gui()
    gui.window.show()
    sys.exit(app.exec_())