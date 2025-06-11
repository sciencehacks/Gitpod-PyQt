import sys
from PyQt5.QtWidgets import(QApplication,QWidget,QLineEdit,QComboBox,QRadioButton,QLabel,QPushButton,QHBoxLayout,QVBoxLayout)


app=QApplication([])
win=QWidget()

label_1=QLabel('')
label_2=QLabel('')
label_3=QLabel('')
label_4=QLabel('')

lie=QLineEdit()
cb=QComboBox()
cb.addItems(['Hey','Good','Boy','Girl'])
pb=QPushButton('Press me')
rd=QRadioButton('student')
rd_1=QRadioButton('teacher')

lay=QHBoxLayout()
vl=QVBoxLayout()

lay.addWidget(label_1)

vl.addWidget(label_2)
vl.addWidget(label_3)
lay.addWidget(lie)

vl.addWidget(pb)
vl.addWidget(rd)
vl.addWidget(rd_1)
vl.addWidget(cb)
lay.addLayout(vl)

cb.currentTextChanged.connect(lambda text:label_3.setText(text))
pb.clicked.connect(lambda :label_1.setText(lie.text()))
rd.toggled.connect(lambda : label_2.setText('Student') if rd.isChecked else '')
rd_1.toggled.connect(lambda : label_2.setText('Teacher') if rd.isChecked else '')
win.setLayout(lay)
win.show()
app.exec_()