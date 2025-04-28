from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def on_click():
    label.setText("Button Clicked!")

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

label = QLabel("Hello")
button = QPushButton("Click Me")
button.clicked.connect(on_click)

layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()