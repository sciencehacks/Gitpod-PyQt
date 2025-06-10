from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel

app = QApplication([])

win = QWidget()
win.setWindowTitle("Radio Button")
win.resize(200, 120)

male = QRadioButton("Male", win)
male.move(20, 20)

female = QRadioButton("Female", win)
female.move(20, 50)

label = QLabel("", win)
label.move(20, 80)

male.toggled.connect(lambda: label.setText("Male") if male.isChecked() else "")
female.toggled.connect(lambda: label.setText("Female") if female.isChecked() else "")

win.show()
app.exec_()
