import sys
from PyQt5.QtWidgets import(QApplication,QWidget,QLineEdit,QPushButton,QComboBox,QRadioButton,QLabel)
app=QApplication([])


#window setup
window=QWidget()
window.setWindowTitle('Hello World')
window.setGeometry(200,200,300,400)



#label_1
la_1=QLabel('Enter your name:',window)
la_1.move(10,21)



#label_2
fruit=QLabel('              ',window)
fruit.move(10,40)

#Label_3
la_2=QLabel('What                     ',window)
la_2.move(10,60)




#line_edit
lie=QLineEdit(window)
lie.move(120,20)





#pushbutton

b=QPushButton('submit',window)
b.move(120,50)
 #pushbutton signal
b.clicked.connect(lambda :la_1.setText(lie.text()))


#radio button
rad=QRadioButton('student',window)
rad.move(120,100)
rad_2 = QRadioButton('Professional',window)
rad_2.move(120,120)
rad_3=QRadioButton('পাগল',window)
rad_3.move(120,140)
rad.toggled.connect(lambda:la_2.setText('Student') if rad.isChecked() else '')
rad_2.toggled.connect(lambda: la_2.setText('Professional') if rad_2.isChecked() else '')
rad_3.toggled.connect(lambda: la_2.setText('পাগল') if rad_3.isChecked() else '')


#combobox

c=QComboBox(window)
c.move(120,80)
c.addItems(['Good','Bad','Nice'])



#combox signal
c.currentTextChanged.connect(lambda text: fruit.setText(text))



#output handeler
window.show()
app.exec_()