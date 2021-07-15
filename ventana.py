from PyQt5.QtWidgets import*
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from lexico import getTokensLexer
from sintactico import getSintatic


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Calculadora Ruby"
        self.top = 100
        self.left = 300
        self.width = 900
        self.height = 600
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout(self)
        self.label = QLabel("Bienvenidos")
        self.label.setFont(QtGui.QFont("Sanserif", 20))
        self.label.setStyleSheet('color:red')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(self.label)

        self.hbox = QHBoxLayout(self)
        self.buttonclear = QPushButton("Limpiar")
        self.buttonclear.setMaximumWidth(100)
        self.buttonclear.setMinimumHeight(60)
        self.buttonclear.setIcon(QtGui.QIcon("clear.png"))
        self.buttonclear.setIconSize(QtCore.QSize(100, 60))

        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setPlaceholderText("Ingrese el codigo aqui")

        self.hbox.addWidget(self.textEdit)
        self.hbox.addWidget(self.buttonclear)
        self.vbox.addLayout(self.hbox)

        self.createButtons()
        self.vbox.addWidget(self.groupBox)

        self.hbox2 = QHBoxLayout(self)
        self.textEditLex = QPlainTextEdit(self)
        self.textEditSint = QPlainTextEdit(self)
        self.textEditLex.setReadOnly(True)
        self.textEditSint.setReadOnly(True)
        self.hbox2.addWidget(self.textEditLex)
        self.hbox2.addWidget(self.textEditSint)
        self.vbox.addLayout(self.hbox2)

        self.buttonclear.clicked.connect(self.clear)


        self.setLayout(self.vbox)


        self.show()

    def createButtons(self):
        self.groupBox = QGroupBox(self)
        self.hbox2 = QHBoxLayout(self)
        self.button = QPushButton("Lexico")
        self.button.setMinimumHeight(40)
        self.button2 = QPushButton("Sintactico y Semantico")
        self.button2.setMinimumHeight(40)
        self.button.clicked.connect(self.showLexer)
        self.button2.clicked.connect(self.showSintatic)
        self.hbox2.addWidget(self.button)
        self.hbox2.addWidget(self.button2)
        self.groupBox.setLayout(self.hbox2)



    def showLexer(self):
        self.textEditLex.clear()
        self.textEditLex.insertPlainText("TOKENS\n")
        self.textEditLex.insertPlainText(getTokensLexer(self.textEdit.toPlainText()))


    def clear(self):#borrar
        self.textEdit.clear()
        self.textEditLex.clear()
        self.textEditSint.clear()

    def showSintatic(self):
        self.textEditSint.clear()
        sin = getSintatic(self.textEdit.toPlainText())
        print(sin)

        if (len(sin)>0):
            self.textEditSint.insertPlainText(sin)
        else:
            self.textEditSint.insertPlainText("No existe error")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


