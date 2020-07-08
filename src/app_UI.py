import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        send_Button_Font = QtGui.QFont()
        send_Button_Font.setPointSize(9)

        text_font = QtGui.QFont()
        text_font.setPointSize(11)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Texting App")

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.sendButton = QtWidgets.QPushButton(self.centralWidget)

        self.sendButton.setFont(send_Button_Font)
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setText("Send")
        self.gridLayout.addWidget(self.sendButton, 1, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.chatBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.chatBrowser.setFont(text_font)
        self.chatBrowser.setObjectName("chatBrowser")
        self.gridLayout.addWidget(self.chatBrowser, 0, 0, 1, 2)

        self.sendInput = QtWidgets.QTextEdit(self.centralWidget)
        self.sendInput.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sendInput.setFont(text_font)
        self.sendInput.setObjectName("sendInput")
        self.sendInput.setPlaceholderText("Type Text Here")
        self.gridLayout.addWidget(self.sendInput, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralWidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
