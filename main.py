from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer

from PyQt5.QtCore import QTimer

timer = QTimer()


app = QApplication([]) # This is the main class of the GUI applicatiob control flow
window = QWidget() # Is the base object for all GUI objects in pyqt5
window.setWindowTitle("Disappearing Text")
layout = QVBoxLayout()

# Create and set the label's text
label = QLabel("Disappearing Text When Typing")
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)  # Add the label to the layout

# Create a QTimer for delayed checking
delayed_timer = QTimer()
delayed_timer.setInterval(5000)  # Set the interval to 1 second
delayed_timer.setSingleShot(True)

# Create the QTextEdit widget
input_field = QTextEdit()
layout.addSpacing(15)
layout.addWidget(input_field)  # Add the text edit widget to the layout

def disappear_text():
    input_field.toPlainText()
    restart_timer()

def on_timer_timeout():
    input_field.clear()

timer = QTimer()
timer.setInterval(5000)
timer.timeout.connect(on_timer_timeout)

def restart_timer():
    timer.stop()
    timer.start()

input_field.textChanged.connect(disappear_text)



# Set the layout for the window
window.setLayout(layout)

# Set the geometry of the window
window.setGeometry(100, 100, 600, 600)

# Show the main window
window.show()

# Execute the application
app.exec_()


