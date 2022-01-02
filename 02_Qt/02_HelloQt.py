from PySide2 import QtWidgets

class MyQtUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Qt UI")
        self.setGeometry(300, 50, 766, 980)

        lWristSelectButton = QtWidgets.QPushButton("Select L_Wrist", self)
        lWristSelectButton.setGeometry(300, 150, 766, 100)
        lWristSelectButton.clicked.connect(self.onLWristSelectButtonClicked)

        rWristSelectButton = QtWidgets.QPushButton("Select R_Wrist", self)
        rWristSelectButton.setGeometry(300, 250, 766, 100)
        rWristSelectButton.clicked.connect(self.onRWristSelectButtonClicked)
      
        lShoulderSelectButton = QtWidgets.QPushButton("Select L_Shoulder", self)
        lShoulderSelectButton.setGeometry(300, 350, 766, 100)
        lShoulderSelectButton.clicked.connect(self.onLShoulderSelectButtonClicked)

        rShoulderSelectButton = QtWidgets.QPushButton("Select R_Shoulder", self)
        rShoulderSelectButton.setGeometry(300, 450, 766, 100)
        rShoulderSelectButton.clicked.connect(self.onRShoulderSelectButtonClicked)

        self.show()

    def onLWristSelectButtonClicked(self):
        print("TODO: Select L_Wrist")

    def onRWristSelectButtonClicked(self):
        print("TODO: Select R_Wrist")

    def onLShoulderSelectButtonClicked(self):
        print("TODO: Select L_Shoulder")

    def onRShoulderSelectButtonClicked(self):
        print("TODO: Select R_Shoulder")

app = QtWidgets.QApplication()
myQtUI = MyQtUI()
app.exec_()