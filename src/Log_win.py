from PyQt5 import QtCore, QtWidgets


class LogDialog(QtWidgets.QDialog):             # log window class
    def __init__(self, log_data):               # getting the log data by the constructor
        super().__init__()

        self.logs = log_data                    # holds the log data

        self.setObjectName("log_win")           # setting the name of the log window object
        self.setFixedSize(730, 500)                   # setting the size of the window

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 730, 500))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 727, 497))

        self.log_panel = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.log_panel.setObjectName("log_panel")
        self.log_panel.setGeometry(QtCore.QRect(0, 0, 730, 500))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        # initialize text area by default
        self.retranslateUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, log_win):                           # initialize text area by default via log data
        _translate = QtCore.QCoreApplication.translate
        log_win.setWindowTitle(_translate("log_win", "Log"))

        self.log_panel.setPlainText(_translate("log_win", self.logs))
