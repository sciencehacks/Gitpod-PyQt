from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

app = QApplication([])

window = QWidget()
window.setWindowTitle("Combo Box Example")
window.setGeometry(100, 100, 300, 150)

label = QLabel("Choose a fruit:", window)
label.move(20, 30)

# Combo box
combo = QComboBox(window)
combo.addItems(["Apple", "Banana", "Cherry"])
combo.move(20, 60)

result = QLabel("", window)
result.move(20, 100)

def on_combo_change(text):
    result.setText(f"You selected:   {text             }                     ")

combo.currentTextChanged.connect(on_combo_change)

window.show()
app.exec_()
