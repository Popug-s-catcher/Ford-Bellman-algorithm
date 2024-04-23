from PyQt5 import QtCore, QtWidgets


class InputDialog(QtWidgets.QDialog):               # class of the input window
    def __init__(self, graph):                      # getting the graph object by the constructor
        super().__init__()
        self.graph = graph                          # holds the object of Graph class

        self.setObjectName("input_win")             # the name of the input window object
        self.setFixedSize(720, 590)                       # setting the size of the window

        # vertical layout of text plain
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 311, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Text plain
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)

        # Vertical layout of input rules
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 20, 361, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Rules
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        # Rule num_1
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        # Rule num_2
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        # Rule num_3
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)

        # Rule num_4
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)

        # Button layout
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 470, 681, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Reset button
        self.pushButton_Reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Reset.setMaximumSize(QtCore.QSize(90, 40))
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.horizontalLayout.addWidget(self.pushButton_Reset)
        self.pushButton_Reset.clicked.connect(self.reset_button_clicked)

        # Approve button
        self.pushButton_Approve = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Approve.setMaximumSize(QtCore.QSize(90, 40))
        self.pushButton_Approve.setObjectName("pushButton_Approve")
        self.horizontalLayout.addWidget(self.pushButton_Approve)
        self.pushButton_Approve.clicked.connect(self.approve_button_clicked)

        # Open file button
        self.pushButton_Open_file = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Open_file.setMaximumSize(QtCore.QSize(90, 40))
        self.pushButton_Open_file.setObjectName("pushButton_Open_file")
        self.horizontalLayout.addWidget(self.pushButton_Open_file)
        self.pushButton_Open_file.clicked.connect(self.open_file_button_clicked)

        # initialize lables by default
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    # open_file button action
    def open_file_button_clicked(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",    # returns the name of the selected file
                                       "../cursed Ford-Bellman/tests",          # folder with tests
                                       "Text files (*.txt)")[0]                 # openning only '.txt' files
        if not file_name:                                       # returns in case of an empty file name
            return
        file = open(file_name, 'r')                             # openning file for reading
        with file:                                              # reading the file and uploading it to the text plain
            data = file.read()
            self.plainTextEdit.setPlainText(data)

    # reset button action
    def reset_button_clicked(self):
        self.plainTextEdit.clear()              # clears text plain

    # checking whitespace function
    def whitespace_func(self, text):
        if len(text) == 0 or text[0] == '' or text[0].isspace():        # function tries the line for emptiness
            return True                                                 # returns True if it is
        return False                                                    # False otherwise

    # checking line's length function
    def length_check(self, line):
        if self.whitespace_func(line):                   # checking for an empty entered line
            self.alert_func("Empty line!", "Empty line are not allowed!")
            return False
        if self.whitespace_func(line):                   # checking for an empty entered line afterwards
            self.alert_func("Empty line!", "Empty line afterwards are not allowed!")
            return False
        if len(line) != 3:                                          # checking for the right number of elements in line
            self.alert_func("Incorrect line!", "There should be 3 elements per line, except the first two!")
            return False
        return True

    # alert raising function
    def alert_func(self, title, message):
        alert = QtWidgets.QMessageBox.critical(self, title, message, QtWidgets.QMessageBox.Ok)

    # approve button action
    def approve_button_clicked(self):
        linear_text = self.plainTextEdit.toPlainText()                  # getting the line of the text from text plain
        text = self.plainTextEdit.toPlainText().split('\n')             # and splitting it

        if self.whitespace_func(text) is True:                          # checking for an empty line
            self.alert_func("Wrong input!", "The field is empty!")
            return

        try:                                                       # checking the right type of the number of vertices
            N = int(text[0])
        except Exception:
            self.alert_func("Wrong input!", "The first line must be the digit!")
            return

        try:
            start = int(text[1])
        except Exception:
            self.alert_func("Wrong input!", "The second line must be the digit!")
            return

        if len(text) == 2:                  # checking for entered edges
            self.alert_func("Wrong input!", "Edges are not entered!")
            return
        if not (0 <= start < N):            # checking for the correct number of the start vertex
            self.alert_func("Wrong start vertex number!",
                            "The number of the start vertex must be less then number of vertices!")
            return
        if not (2 <= N <= 30):              # checking for the right amount of vertices
            self.alert_func("Wrong value of vertices number!",
                            "The number of vertices must be in [2; 30]")
            return

        self.graph.N = N                # initializing the fields of the graph object
        self.graph.start = start
        self.graph.edges.clear()        # and clearing dictionaries before initializing in case of saved data
        self.graph.paths.clear()

        for i in range(2, len(text)):           # reading 'edges' part of text
            line = list(text[i].split())        # splitting the string
            if not self.length_check(line):     # checking for 3 elements per line
                return

            try:                                # checking the names of the vertices for the correct name type
                sv = int(line[0])
                ev = int(line[1])
            except Exception:
                self.alert_func("Wrong verticies names!",
                                "The names of the adjacent verticies must be the integer numbers!")
                return

            if not (0 <= sv < N):               # checking start vertex name
                self.alert_func("Wrong vertex name!", "Wrong name of start vertex!")
                return

            if not (0 <= ev < N):               # checking name of adjacent vertex
                self.alert_func("Wrong vertex name!", "Wrong name of adjacent vertex!")
                return

            if sv == ev:                        # checking for a loop
                self.alert_func("Loop error!", "There must be no loop in graph!")
                return

            try:                                # checking the correct weight type
                weight = int(line[2])
            except Exception:
                self.alert_func("Wrong weight value!", "Weight value must be integer number!")
                return

            if not (-50 <= weight <= 50):       # checking weight value
                self.alert_func("Wrong weight value!", "The weight value is incorrect!")
                return
            self.graph.edges[(sv, ev)] = weight     # adding the edge to the graph
        self.graph.config = linear_text         # saving graph configuration
        self.close()                            # closing the window

    def retranslateUi(self, input_win):         # initializing labels by default
        _translate = QtCore.QCoreApplication.translate
        input_win.setWindowTitle(_translate("input_win", "Graph Input"))
        if self.graph.config is None:
            # setting the instruction by default
            self.plainTextEdit.setPlainText(_translate("input_win", "\"Количество вершин графа N\"\n"
                                                                    "\"Стартовая вершина s\"\n"
                                                            "\"Вершина a1\" \"Смежная ей b1\" \"Вес ребра a1-b1\"\n"
                                                       "...\n"
                                                       "\"Вершина aN\" \"Смежная ей bN\" \"Вес ребра aN-bN\"\n"))
        else:
            # or the configuration when the graph is entered
            self.plainTextEdit.setPlainText(_translate("input_win", self.graph.config))
        self.label.setText(_translate("input_win",
                                      "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; "
                                      "text-decoration: underline;\""
                                      ">Правила валидного ввода данных:</span></p></body></html>"))
        self.label_2.setText(_translate("input_win", "1) Сперва вводится количество вершин графа N, "
                                                     "затем \nстартовая вершина, "
                                                     "затем строки (вершина; \nей смежная; ребро меж ними)"))
        self.label_3.setText(_translate("input_win", "2) Названиями вершин служат целые числа в \nинтервале [0, N)"))
        self.label_4.setText(_translate("input_win", "3) В графе не должно быть петель (т.е. \nтакого ввода, как, "
                                                     "к примеру, 5 5 2)"))
        self.label_5.setText(_translate("input_win", "4) Вес ребра должен быть целым числом в интервале \n[-50, 50]"))
        self.pushButton_Reset.setText(_translate("input_win", "Reset"))
        self.pushButton_Approve.setText(_translate("input_win", "Approve"))
        self.pushButton_Open_file.setText(_translate("input_win", "Open file"))
