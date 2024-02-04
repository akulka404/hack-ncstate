import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QFont, QIcon, QColor


class TickerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.history_texts = []  # Initialize an empty list to store history of texts
        self.mouse_pressed = False  # Track if the mouse is pressed
        self.old_pos = self.pos()  # Store the old position of the window
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 700, 550)  # Adjust window size and position
        self.setWindowTitle('Text Ticker with History Log')
        self.setWindowIcon(QIcon('app_icon.png'))  # Set window icon

        # Set the window transparent
        self.setWindowOpacity(0.9)  # Set the transparency (1.0 is opaque, 0.0 is fully transparent)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the window background transparent
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove the window frame

        # Create a QVBoxLayout instance with margins and spacing
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(10)

        # Close Button
        self.closeButton = QPushButton('X')
        self.closeButton.setFixedSize(QSize(24, 24))
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 12px;
                background-color: red;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        # Close button layout (aligning to the right)
        self.closeButtonLayout = QHBoxLayout()
        self.closeButtonLayout.addWidget(self.closeButton, 0, Qt.AlignRight | Qt.AlignTop)
        self.layout.addLayout(self.closeButtonLayout)

        # Create a QLabel for displaying the history log
        self.history_label = QLabel(self)
        self.history_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.history_label.setFont(QFont("Arial", 12))  # Set font for history log
        self.history_label.setWordWrap(True)

        # Add a frame and background color to the history label
        self.history_label.setFrameStyle(QFrame.Panel | QFrame.Sunken)  # Use QFrame for frame style
        self.history_label.setAutoFillBackground(True)
        palette = self.history_label.palette()
        palette.setColor(self.history_label.backgroundRole(), QColor(240, 240, 240))
        self.history_label.setPalette(palette)

        # Create a QLineEdit for text input
        self.line_edit = QLineEdit(self)
        self.line_edit.setFont(QFont("Arial", 12))  # Set font for line_edit

        # Style the QLineEdit
        self.line_edit.setStyleSheet("QLineEdit {"
                                     "border: 1px solid gray;"
                                     "border-radius: 5px;"
                                     "padding: 5px;"
                                     "background-color: white;"
                                     "}")

        # Add the history label and line edit to the layout
        self.layout.addWidget(self.history_label, 1)  # Add history label to layout with stretch factor
        self.layout.addWidget(self.line_edit)  # Add line edit to layout without stretch factor

        # Set the layout for the main window
        self.setLayout(self.layout)

        # Connect the returnPressed signal of the QLineEdit to the slot method
        self.line_edit.returnPressed.connect(self.update_history)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            self.old_pos = event.globalPos()


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mouse_pressed:
            delta = QPoint (event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def update_history(self):
        # Get the entered text and clear the input field
        entered_text = self.line_edit.text().strip()
        if entered_text:  # Check if the text is not empty
            self.history_texts.append(entered_text)  # Append the text to the history list
            self.line_edit.clear()  # Clear the input field
            # Update the history label with the accumulated texts
            self.history_label.setText('\n'.join(self.history_texts))

    
    def mouseReleaseEvent(self, event):
        self.mouse_pressed = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TickerWidget()
    ex.show()
    sys.exit(app.exec_())
