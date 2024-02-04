import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore

class VideoCapture(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(VideoCapture, self).__init__(*args, **kwargs)
        self.video = cv2.VideoCapture(1)  # 0 for the primary camera
        
        # Get the size of the screen
        screen = QtWidgets.QApplication.primaryScreen().size()
        self.display_width = screen.width()
        self.display_height = screen.height()
        self.setFixedSize(self.display_width, self.display_height)
        
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.image_label)

        # Update timer
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)  # Interval in ms to get the latest frame
        self.timer.timeout.connect(self.update_frame)
        self.timer.start()

        # Close button
        self.closeButton = QtWidgets.QPushButton('Close', self)
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setGeometry(self.display_width - 100, 10, 90, 30)  # Adjust size and position as needed

    def update_frame(self):
        ret, frame = self.video.read()
        if ret:
            # Resize frame to fit the screen
            frame = cv2.resize(frame, (self.display_width, self.display_height), interpolation=cv2.INTER_AREA)
            frame = cv2.flip(frame, 1)
            # Convert the frame to Qt format
            image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
            # Set the pixmap of the label to the captured frame
            self.image_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def closeEvent(self, event):
        super(VideoCapture, self).closeEvent(event)
        self.video.release()  # Release the video stream

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = VideoCapture()

    # Set window style to frameless and set the geometry to cover the whole screen
    win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    win.setGeometry(0, 0, win.display_width, win.display_height)

    win.show()  # Show the window
    sys.exit(app.exec_())
