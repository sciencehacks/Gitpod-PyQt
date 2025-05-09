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
      h=QHBoxLayout()
      v=QVBoxLayout()
      h.addWidget(b1)
      h.addWidget(b2)
      v.addWidget(label)
      v.addLayout(h)
      v.addWidget(b3)
     
      self.setLayout(v)

        

    



if __name__=="__main__":
    a=QApplication(sys.argv)
    window=ham()
    window.show()
    sys.exit(a.exec_())