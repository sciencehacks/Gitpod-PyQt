import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QVBoxLayout)
class hat(QWidget):


   
        def __init__(self):
          super().__init__()
          self.setWindowTitle("Signals and Slots Demo (PyQt5)")
          self.click_count = 0
          self.init_ui()

        def init_ui(self):
            self.button=QPushButton("Press me")
            self.label=QLabel('you have not pressed')
            self.button.clicked.connect(self.obp)

            v=QVBoxLayout()
            v.addWidget(self.label)
            v.addWidget (self.button)
            self.setLayout(v)

        def obp(self):
                self.cc+=1
                self.label.setText('hue')
                

if __name__=='__main__':
    a=QApplication(sys.argv)
    w= hat()
    w.show()
    sys.exit(a.exec_())
    