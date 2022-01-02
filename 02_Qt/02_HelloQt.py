from PySide2 import QtWidgets

class MySelectButton(QtWidgets.QPushButton):

    _name: str 
    _posX: int
    _posY: int


    def __init__(self, name: str, x: int, y: int, parent: QtWidgets.QWidget):
        super().__init__(f'select {name}', parent)

        self._name = name
        self._posX = x
        self._posY = y

        self.setGeometry(self._posX, self._posY, 200, 40)
        self.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        print(f'Select {self._name}')

class MyQtUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Qt UI")
        self.setGeometry(300, 50, 766, 980)

        MySelectButton("L_Wrist", 10, 10, self)

        MySelectButton("R_Wrist", 220, 10, self)
      
        MySelectButton("L_Shoulder", 430, 10, self)

        MySelectButton("R_Shoulder", 640, 10, self)
      

        self.show()


app = QtWidgets.QApplication()
myQtUI = MyQtUI()
app.exec_()