from PyQt5 import QtCore, QtWidgets


class HelpDialog(QtWidgets.QDialog):                # help window class
    def __init__(self):
        super().__init__()

        self.setObjectName("help_win")              # setting the name of the help window object
        self.setFixedSize(500, 730)                       # setting the size of the window

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 730))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 497, 727))

        self.help_panel = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.help_panel.setObjectName("help_panel")
        self.help_panel.setGeometry(QtCore.QRect(0, 0, 500, 727))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        # initialize text area by default
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, help_win):                          # initialize text area by default
        _translate = QtCore.QCoreApplication.translate
        help_win.setWindowTitle(_translate("help_win", "Help"))

        self.help_panel.setPlainText(_translate("input_win", "\t\tИнструкция\n\nОписание кнопок:\n\n"
                                                             "'Start the algorithm' - запускает алгоритм, если граф "
                                                             "введён, в ином случае не делает ничего.\n\n"
                                                             "'Reset' - сбрасывает граф: чистит поле отрисовки графа,\n"
                                                "удаляет введённый граф, чисти журнал действий и поле ответа.\n\n"
                                                "'Input graph' - кнопка открывает диалоговое окно ввода графа. \n"
                                                "Граф вводится в окошко ввода текста, в соответствии с правилами \n"
                                                "ввода, написанными справа от окошка, после чего \n"
                                                "нажимается кнопка 'Approve' для проверки корректности ввода данных: \n"
                                      "если есть ошибки ввода - появляются оповещения об оных, в ином случае \n"
                                "программа принимает данные и граф отрисовывается на левой панели главного окна. Также"
                                " диалоговое окно обладает кнопками 'Reset' - отчистки поля - и 'Open file' - открытия"
                                " окна проводника для выбора файла загрузки данных.\n\n"
                                "'Log' - кнопка открывающая диалоговое окно журнала действий алгоритма. По умолчанию и "
                                "в случае, если граф не загружен или загружен, но кнопка старта алгоритма не была нажата, "
                                "открывается пустое окно; при нажатии показывает пошаговые действия алгоритма, "
                                "после нажатия 'Start the algorithm'. \n\n"
                                "'?' - кнопка открытия окна с инструкцией о пользовании приложением.\n\n"
                                "'Show' - кнопка показывающая путь. Введите в строку выше вершину, путь до которой от стартовой "
                                "хотите увидеть и нажмите эту кнопку.\n\n"
                                "'Cancel' - отмена отображения пути.\n\n"))
