from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLineEdit,QLabel,QRadioButton,QComboBox,QVBoxLayout,QHBoxLayout)
import sys

app=QApplication([])
win=QWidget()

l1=QLabel('Enter Your Name:')
l2=QLabel('something')

li=QLineEdit()

cb=QComboBox()
cb.addItems(['student','Teacher','Staff'])

r1=QRadioButton('Male')
r2=QRadioButton('Female')

pb=QPushButton('submit')

lay_1=QHBoxLayout()
lay_2=QVBoxLayout()
lan=QHBoxLayout()
lay_1.addWidget(l1)
lay_1.addWidget(li)

lay_2.addLayout(lay_1)
lay_2.addWidget(cb)
lay_2.addWidget(r1)
lay_2.addWidget(r2)
lay_2.addWidget(pb)

lan.addLayout(lay_2)

name=QLabel('name here')
cbl=QLabel('profession here')

rbl=QLabel('Gender here')

lay_2.addWidget(name)
lay_2.addWidget(cbl)
lay_2.addWidget(rbl)

pb.clicked.connect(lambda : name.setText(li.text()))
cb.currentTextChanged.connect(lambda text:cbl.setText(text))
r1.toggled.connect(lambda :rbl.setText('Male') if r1.isChecked() else '' )
r2.toggled.connect(lambda :rbl.setText('Female') if r1.isChecked() else '' )


win.setLayout(lan)

win.show()
app.exec_()