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
        button_1=QPushButton("p_1")
        button_2=QPushButton("P_2")
        C_l1=QLabel('hey')
        C_l2=QLabel('bye')

        h_l=QHBoxLayout()
        h_l.addWidget(button_1)
        h_l.addWidget(button_2)

        v_l=QVBoxLayout
        v_l.addWidget(C_l1)
        
        v_l.addLayout(h_l)
        v_l.addWidget(C_l2)

        self.setLayout(v_l)

    



if __name__=="__main__":
    a=QApplication(sys.argv)
    window=ham()
    window.show
    sys.exit(a.exec_())