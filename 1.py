import sys
from PyQt5.QtWidgets import(QApplication,QMainWindow,QLabel,QPushButton,QWidget)
from PyQt5.QtCore import Qt

class eam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('utsho')
        self.setGeometry(500,500,600,600)
        c_l=QLabel('Love you Kulchum!')
        c_l.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(c_l)
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=eam()
    window.show()
    sys.exit(app.exec_())