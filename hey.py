from PyQt5.QtWidgets import(QApplication,QVBoxLayout
,QHBoxLayout,QLabel,QWidget,QPushButton)
import sys

class ham(QWidget):
   def __init__(self):
     super().__init__()
     self.setWindowTitle('Hello World')
     self.setGeometry(200,200,300,300)
     self.init_ui()

   def init_ui(self):
        v=QVBoxLayout()
        h=QHBoxLayout()
        l1=QPushButton('hey')
        l2=QPushButton('hey')
        l3=QPushButton('hey')
        lab=QLabel('hello in the world of PYQT ')
        
        
        h.addWidget(l1)
        h.addWidget(l2)
        
        v.addWidget(lab)
        v.addLayout(h)
        v.addWidget(l3)
        self.setLayout(v)
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ham()
    window.show()
    sys.exit(app.exec_())


