import sys
from PyQt5.QtWidgets import(QApplication,QWidget,QLineEdit,QLabel,QPushButton)
a=QApplication([])
#window initialize
win=QWidget()
win.setWindowTitle('Button and label')
win.setGeometry(100,100,300,200)

#label
label=QLabel("Give the name:",win)
label.move(100,50)

#line edit
lie=QLineEdit(win)
lie.move(100,70)

#output

output=QLabel("                             ",win) 
output.move(100,120)
def op():
    name=lie.text()
    output.setText(f'Hello,{name     }')

#submit
b=QPushButton('Submit',win)
b.move(100,100)
b.clicked.connect(op)

win.show()
a.exec_()

