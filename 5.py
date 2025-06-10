import sys
from PyQt5.QtWidgets import(QApplication,QWidget,QLabel,QPushButton)
a=QApplication([])
#window initialize
win=QWidget()
win.setWindowTitle('Button and label')
win.setGeometry(100,100,300,200)

#label

label=QLabel('hello eveyone and world',win)
label.move(100,100)

#button
b=QPushButton('click me',win)
b.move(100,50)
b.clicked.connect(lambda :label.setText('You done'))

win.show()
a.exec_()