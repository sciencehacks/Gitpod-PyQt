import sys
from PyQt5.QtWidgets import(QApplication,QMainWindow,QLabel,QPushButton,QWidget,QVBoxLayout,QHBoxLayout)
from PyQt5.QtCore import Qt

class ham(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello")
        self.setGeometry(100,100,200,200)
        self.init_ui()

    def init_ui(self):
      b1=QPushButton("BUTTON 1")
      b2=QPushButton('BUTTON 2')
      b3=QPushButton('BUTTON 3')
      label=QLabel('HELLO UTSHO')
      ha=QHBoxLayout()
      va=QVBoxLayout()
      v=va.addWidget
      vl=va.addLayout()
      h=ha.addWidget()
      h(b1)
      h(b2)
      v(label)
      v(h)
      v(b3)
     
      self.setLayout(v)

        

    



if __name__=="__main__":
    a=QApplication(sys.argv)
    window=ham()
    window.show()
    sys.exit(a.exec_())