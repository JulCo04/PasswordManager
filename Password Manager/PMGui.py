
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
from random import choice, shuffle, randint

class Ui_MainWindow(object):
        # GUI Generated by using PyQt Designer and converted to a python file
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(450, 450)
                MainWindow.setStyleSheet("#MainWidget {\n"
        "    background-color: rgb(19, 24, 42)\n"
        "}")
                MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("#centralwidget {\n"
        "    background-color: rgb(33, 53, 85)\n"
        "}")
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(100, 200, 64, 16))
                self.label.setObjectName("label")
                self.companyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.companyLineEdit.setGeometry(QtCore.QRect(170, 200, 113, 20))
                self.companyLineEdit.setStyleSheet("#companyLineEdit {\n"
        "    background-color: rgb(240, 240, 240)\n"
        "}")
                self.companyLineEdit.setObjectName("companyLineEdit")
                self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.emailLineEdit.setGeometry(QtCore.QRect(170, 240, 113, 20))
                self.emailLineEdit.setStyleSheet("#emailLineEdit {\n"
        "    background-color: rgb(240, 240, 240)\n"
        "\n"
        "}")
                self.emailLineEdit.setObjectName("emailLineEdit")
                self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.usernameLineEdit.setGeometry(QtCore.QRect(170, 280, 113, 20))
                self.usernameLineEdit.setStyleSheet("#usernameLineEdit {\n"
        "    background-color: rgb(240, 240, 240)\n"
        "\n"
        "}")
                self.usernameLineEdit.setObjectName("usernameLineEdit")
                self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.passwordLineEdit.setGeometry(QtCore.QRect(170, 320, 113, 20))
                self.passwordLineEdit.setStyleSheet("#passwordLineEdit {\n"
        "    background-color: rgb(240, 240, 240)\n"
        "\n"
        "}")
                self.passwordLineEdit.setObjectName("passwordLineEdit")
                self.passwordPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.passwordPushButton.setGeometry(QtCore.QRect(290, 320, 111, 23))
                self.passwordPushButton.setStyleSheet("#passwordPushButton {\n"
        "    background-color: rgb(79, 112, 156);\n"
        "    color : rgb(240, 240, 240)\n"
        "}")
                self.passwordPushButton.setObjectName("passwordPushButton")
                self.addPushButton = QtWidgets.QPushButton(self.centralwidget)
                self.addPushButton.setEnabled(True)
                self.addPushButton.setGeometry(QtCore.QRect(200, 350, 41, 21))
                self.addPushButton.setStyleSheet("#addPushButton {\n"
        "    background-color: rgb(79, 112, 156);\n"
        "    color : rgb(240, 240, 240)\n"
        "}")
                self.addPushButton.setObjectName("addPushButton")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(120, 10, 200, 181))
                self.label_5.setObjectName("label_5")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(100, 240, 37, 16))
                self.label_6.setObjectName("label_6")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(100, 280, 69, 16))
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(100, 320, 68, 16))
                self.label_3.setObjectName("label_3")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
                self.menubar.setObjectName("menubar")
                self.menuFile = QtWidgets.QMenu(self.menubar)
                self.menuFile.setObjectName("menuFile")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.toolBar = QtWidgets.QToolBar(MainWindow)
                self.toolBar.setObjectName("toolBar")
                MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
                self.actionClose = QtWidgets.QAction(MainWindow)
                self.actionClose.setObjectName("actionClose")
                self.menuFile.addAction(self.actionClose)
                self.menubar.addAction(self.menuFile.menuAction())

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #---------------------------------------------------------------------------#
                # Custom functionality
                self.passwordPushButton.clicked.connect(self.generatePassword)
                self.addPushButton.clicked.connect(self.saveToTxt)
                self.actionClose.triggered.connect(exit)
        #---------------------------------------------------------------------------#


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#f0f0f0;\">Company:</span></p></body></html>"))
                self.passwordPushButton.setText(_translate("MainWindow", "Generate Password"))
                self.addPushButton.setText(_translate("MainWindow", "Enter"))
                self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/lock200.png\"/></p></body></html>"))
                self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#f0f0f0;\">Email:</span></p></body></html>"))
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#f0f0f0;\">Username:</span></p></body></html>"))
                self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#f0f0f0;\">Password:</span></p></body></html>"))
                self.menuFile.setTitle(_translate("MainWindow", "File"))
                self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
                self.actionClose.setText(_translate("MainWindow", "Close"))

        #---------------------------------------------------------------------------#
        # User interactive functions

        # Generate a password with random characters
        def generatePassword(self):

                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

                password_letters = [choice(letters) for _ in range(randint(8, 10))]
                password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
                password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

                password_list = password_letters + password_symbols + password_numbers
                shuffle(password_list)

                password = "".join(password_list)

                self.passwordLineEdit.setText(password)
        
        # Adds function to button to save login information to a text file
        def saveToTxt(self):

                company = self.companyLineEdit.text()
                email = self.emailLineEdit.text()
                username = self.usernameLineEdit.text()
                password = self.passwordLineEdit.text()

                # If one of the fields are empty
                if ((len(company) == 0 ) or (len(email) == 0) or (len(username) == 0) or (len(password) == 0)):
                        message = QMessageBox()
                        message.setText("One of your entries are empty")
                        message.exec_()
                else:
                        with open("data.txt", "a") as data_file:
                                data_file.write(f"{company} | {email} | User: {username} | Pass: {password}\n")
                                self.companyLineEdit.clear()
                                self.emailLineEdit.clear()
                                self.usernameLineEdit.clear()
                                self.passwordLineEdit.clear()
        #---------------------------------------------------------------------------#

import source_rc


