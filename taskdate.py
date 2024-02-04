import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # Increase the width by 20%
        original_width = 320
        width_increase_factor = 1.2
        MainWindow.resize(int(original_width * width_increase_factor), 591)

        # Make the window frameless and set window opacity
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowOpacity(0.8)  # Adjust opacity from 0.0 to 1.0 as needed
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Optional: for full transparency

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ... [setup other widgets] ...
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, int(281 * width_increase_factor), 551))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(10)
        self.label.setMidLineWidth(36)
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 30, int(221 * width_increase_factor), 41))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color: white;")  # Set background to white

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 90, int(221 * width_increase_factor), 31))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("background-color: white; font-weight: bold;")  # Set background to white and make the font bold

        # Create a scroll area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 130, int(221 * width_increase_factor), 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # Create a content widget for the scroll area
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, int(219 * width_increase_factor), 399))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Create a vertical layout inside the content widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        # Fetch the tasks from the API and add them to the layout
        tasks = self.fetchTasks()
        for i in range(0, len(tasks), 2):  # Assuming 'tasks' is a list like ['time1', 'task1', 'time2', 'task2', ...]
            time = tasks[i]
            task = tasks[i + 1]
            taskWidget = QtWidgets.QWidget()
            taskLayout = QtWidgets.QVBoxLayout(taskWidget)
            timeLabel = QtWidgets.QLabel(time)
            taskLabel = QtWidgets.QLabel(task)
            checkBox = QtWidgets.QCheckBox("Done")
            separator = QtWidgets.QFrame()
            separator.setFrameShape(QtWidgets.QFrame.HLine)
            separator.setFrameShadow(QtWidgets.QFrame.Sunken)

            taskLayout.addWidget(timeLabel)
            taskLayout.addWidget(taskLabel)
            taskLayout.addWidget(checkBox)
            taskLayout.addWidget(separator)
            timeLabel.setWordWrap(True)
            taskLabel.setWordWrap(True)

            # Connect the toggleTask method to the checkBox stateChanged signal
            checkBox.stateChanged.connect(lambda state, cb=checkBox, tl=timeLabel, tl2=taskLabel: self.toggleTask(cb, tl, tl2))

            self.verticalLayout.addWidget(taskWidget)

        # Add a close button, adjust its position according to the increased width
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(int(290 * width_increase_factor), 0, 30, 30))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setText("X")
        self.closeButton.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        current_time = datetime.now()
        formatted_date_time = current_time.strftime("%d/%m/%Y Time: %H:%M %p")
        self.label_3.setText(_translate("MainWindow", "Date: " + formatted_date_time))
        self.label_7.setText(_translate("MainWindow", "Taskboard"))

    def fetchTasks(self):
        user_name = 'Firasat'
        url = 'https://remembrall-cd7db0135b38.herokuapp.com/user/' + user_name + "/"
        try:
            r1 = requests.get(url)
            my_json = r1.json()
            # print(my_json)
            response = json.loads(my_json['user_log_summarization'])
            # print(response[0])
            print()
        except Exception as e:
            print(f"Error fetching tasks: {e}")
            response = []
        return response
    
    def toggleTask(self, checkBox, timeLabel, taskLabel):
        # When a task is checked/unchecked, change its appearance
        font = taskLabel.font()
        if checkBox.isChecked():
            font.setStrikeOut(True)
        else:
            font.setStrikeOut(False)
        taskLabel.setFont(font)

class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)
        self._drag_pos = QtCore.QPoint()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = CustomMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())