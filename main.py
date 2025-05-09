import sys
from PyQt5.QtWidgets import(QLabel,QWidget,QApplication,QPushButton)
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=QWidget()
    window.setWindowTitle('hey')
    window.setGeometry(100,100,100,100)
    window.show()
    sys.exit(app.exec_()) 