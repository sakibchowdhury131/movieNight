# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from paho.mqtt import client as mqtt_client
import sys
from player import Window
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt

class Ui_credWindow(object):


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(729, 462)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(180, 120, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(180, 180, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(180, 210, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(180, 240, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditBroker = QtWidgets.QLineEdit(self.widget)
        self.lineEditBroker.setGeometry(QtCore.QRect(320, 120, 241, 25))
        self.lineEditBroker.setInputMask("")
        self.lineEditBroker.setClearButtonEnabled(False)
        self.lineEditBroker.setObjectName("lineEditBroker")
        self.lineEditPort = QtWidgets.QLineEdit(self.widget)
        self.lineEditPort.setGeometry(QtCore.QRect(320, 150, 241, 25))
        self.lineEditPort.setInputMask("")
        self.lineEditPort.setObjectName("lineEditPort")
        self.lineEditUsername = QtWidgets.QLineEdit(self.widget)
        self.lineEditUsername.setGeometry(QtCore.QRect(320, 180, 241, 25))
        self.lineEditUsername.setInputMask("")
        self.lineEditUsername.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setGeometry(QtCore.QRect(320, 210, 241, 25))
        self.lineEditPassword.setAutoFillBackground(False)
        self.lineEditPassword.setInputMask("")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setMaxLength(32767)
        self.lineEditPassword.setFrame(True)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditTopic = QtWidgets.QLineEdit(self.widget)
        self.lineEditTopic.setGeometry(QtCore.QRect(320, 240, 241, 25))
        self.lineEditTopic.setObjectName("lineEditTopic")
        self.pushButtonConnect = QtWidgets.QPushButton(self.widget)
        self.pushButtonConnect.setGeometry(QtCore.QRect(380, 300, 89, 25))
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(180, 350, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(250, 350, 211, 17))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.pushButtonConnect.clicked.connect(self.connect_clicked)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Movie Night v1.1"))
        self.label.setText(_translate("mainWindow", "Broker: "))
        self.label_2.setText(_translate("mainWindow", "Port:"))
        self.label_3.setText(_translate("mainWindow", "User Name:"))
        self.label_4.setText(_translate("mainWindow", "Password:"))
        self.label_5.setText(_translate("mainWindow", "Topic:"))
        self.lineEditBroker.setPlaceholderText(_translate("mainWindow", "IP address of the server"))
        self.lineEditPort.setPlaceholderText(_translate("mainWindow", "typically 1883"))
        self.lineEditUsername.setPlaceholderText(_translate("mainWindow", "Some Broker don\'t require username"))
        self.lineEditTopic.setPlaceholderText(_translate("mainWindow", "topic must be same for the group"))
        self.pushButtonConnect.setText(_translate("mainWindow", "Connect"))
        self.label_6.setText(_translate("mainWindow", "Provide Server Credentials"))
        self.label_7.setText(_translate("mainWindow", "Status: "))
        self.label_8.setText(_translate("mainWindow", "Not Connected"))
    
    
    
    
    def connect_clicked(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.label_8.setText("Connected")
                print("Connected to MQTT Broker!")
                self.client.loop_stop()
                self.client.disconnect()
                secondScreen.startServer(self.broker, self.port, self.username, self.password, self.topic)
                p = widget.palette()
                p.setColor(QPalette.Window, Qt.black)
                widget.setPalette(p)
                widget.setCurrentIndex(widget.currentIndex()+1)
                

            else:
                self.label_8.setText("Failed to Connect")
                print("Failed to connect, return code %d\n", rc)



        self.broker = self.lineEditBroker.text()
        self.port = int(self.lineEditPort.text())
        self.username = self.lineEditUsername.text()
        self.password = self.lineEditPassword.text()
        self.topic = self.lineEditTopic.text()

        self.label_8.setText("Connecting...")

        print(self.broker)
        print(self.port)
        print(self.username)
        print(self.password)
        print(self.topic)
        print("UI shown")
        


        self.client = mqtt_client.Client()
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    

        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    credWindow = QtWidgets.QMainWindow()
    credui = Ui_credWindow()
    credui.setupUi(credWindow)


    secondScreen = Window()

    widget.addWidget(credWindow)
    widget.addWidget(secondScreen)
    widget.setWindowTitle("movie Night")
    widget.setGeometry(350, 100, 850, 500)
    widget.setWindowIcon(QIcon('network.png'))
    widget.show()
    sys.exit(app.exec_())