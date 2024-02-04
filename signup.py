from PyQt5 import QtCore, QtGui, QtWidgets
import requests  # Used for HTTP POST request

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 675)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 391, 651))
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(10)
        self.label_3.setMidLineWidth(36)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 341, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 600, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 60, 331, 531))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        # Name
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        
        # Age
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        
        # Gender ComboBox
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_gender = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_gender.addItems([" ", "M", "F", "Prefer not to say"])  # Add your options here
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_gender)
        
        # Contact
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        
        # Home Location
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        
        # Emergency Contact Name
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        
        # Emergency Contact Number
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        
        # Current Location
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        
        # Log Summarization
        # self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        # self.label_11.setObjectName("label_11")
        # self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_11)
        # self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        # self.lineEdit_8.setObjectName("lineEdit_8")
        # self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        
        # Race/Ethnicity ComboBox
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.comboBox_race = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_race.addItems(["American Indian", "Asian", "African American", "Native Hawaiian", "White"])  # Add your options here
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.comboBox_race)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.submit_data)  # Connect the button click to the submit function

    def submit_data(self):
        data = {
            "user_name": self.lineEdit.text(),
            "user_age": self.lineEdit_2.text(),
            "user_gender": self.comboBox_gender.currentText(),
            "user_contact": self.lineEdit_3.text(),
            "user_home_location": self.lineEdit_4.text(),
            "user_emergency_contact_name": self.lineEdit_5.text(),
            "user_emergency_contact": self.lineEdit_6.text(),
            "user_current_location": self.lineEdit_7.text(),
            "user_log_summarization": "00:00, Task 0",
            "user_race": self.comboBox_race.currentText()
        }
        
        response = requests.post("https://remembrall-cd7db0135b38.herokuapp.com/user/", json=data)
        
        if response.status_code == 201:
            print("Data submitted successfully.")
            QtWidgets.QMessageBox.information(None, "Success", "Data submitted successfully!")
        else:
            print("Failed to submit data. Error code:", response.status_code)
            QtWidgets.QMessageBox.warning(None, "Failed", f"Failed to submit data. Error code: {response.status_code}")

        import os 
        cmd = 'python3 train.py ' + str(self.lineEdit.text())
        os.system(cmd)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Remembrall Sign-up"))
        self.label.setText(_translate("Form", "Remembrall Sign-up Form"))
        self.pushButton.setText(_translate("Form", "Sign-up User"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_4.setText(_translate("Form", "Age"))
        self.label_5.setText(_translate("Form", "Gender"))
        self.label_6.setText(_translate("Form", "Contact"))
        self.label_7.setText(_translate("Form", "Home Location"))
        self.label_8.setText(_translate("Form", "Emergency Contact Name"))
        self.label_9.setText(_translate("Form", "Emergency Contact Number"))
        self.label_10.setText(_translate("Form", "Current Location"))
        # self.label_11.setText(_translate("Form", "Log Summarization"))
        self.label_12.setText(_translate("Form", "Race/Ethnicity"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
