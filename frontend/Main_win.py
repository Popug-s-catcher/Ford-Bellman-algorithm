from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from frontend.Input_Dialog_win import InputDialog
from frontend.Log_win import LogDialog
from frontend.Help_win import HelpDialog
from backend.Graph import Graph
from backend.FB import FB_alg
import networkx as nx


class MainWin(QtWidgets.QDialog):       # main window class
    def __init__(self):                 # constructor
        super().__init__()
        self.graph = Graph()            # creating the graph
        self.log_data = ""              # log data field

    def setupUi(self, Dialog):              # setting up window's widgets
        Dialog.setObjectName("Main_win")      # setting the name of the main window object
        Dialog.setFixedSize(1123, 859)            # setting the size of the window

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(850, 550, 261, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # start button of an algorithm
        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_button.setMaximumSize(QtCore.QSize(260, 50))
        self.start_button.setBaseSize(QtCore.QSize(10, 10))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.start_alg_button)

        self.verticalLayout.addWidget(self.start_button)


        # 'generate' button of graph
        self.reset_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reset_button.setMaximumSize(QtCore.QSize(260, 50))
        self.reset_button.setObjectName("reset_button")
        self.reset_button.clicked.connect(self.reset_button_action)

        self.verticalLayout.addWidget(self.reset_button)


        # input graph button
        self.input_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.input_button.setMaximumSize(QtCore.QSize(260, 50))
        self.input_button.setObjectName("input_button")
        self.input_button.clicked.connect(self.input_button_clicked)

        self.verticalLayout.addWidget(self.input_button)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 821, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.name.setObjectName("name")

        self.verticalLayout_2.addWidget(self.name)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(849, 9, 261, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # log button
        self.log_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.log_button.setMaximumSize(QtCore.QSize(59, 59))
        self.log_button.setObjectName("log")
        self.log_button.clicked.connect(self.log_button_clicked)

        # help button
        self.help_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.help_button.setMaximumSize(QtCore.QSize(59, 59))
        self.help_button.setObjectName("help")
        self.help_button.clicked.connect(self.help_button_clicked)

        self.horizontalLayout_4.addWidget(self.log_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.help_button, 0, QtCore.Qt.AlignHCenter)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 821, 771))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")


        # drawing field
        self.drawing_field = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.drawing_field.setContentsMargins(0, 0, 0, 0)
        self.drawing_field.setObjectName("drawing_field")
        self.fig = plt.figure(figsize= (5, 4))              # setting the size of drawing plane
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.drawing_field.addWidget(self.canvas)


        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(850, 110, 261, 301))

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        # output panel
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_4)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 257, 297))
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 261, 301))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(850, 450, 261, 91))

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # line area for inputting end-vertex
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # show path button
        self.show_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.show_button.setObjectName("show_button")
        self.show_button.clicked.connect(self.show_button_clicked)

        self.horizontalLayout_2.addWidget(self.show_button)

        # cancel showing path button
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

        self.horizontalLayout_2.addWidget(self.cancel_button)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        # labels for outputting panel and showing path area
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(850, 420, 261, 21))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(850, 80, 131, 21))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(980, 80, 131, 21))

        # initialize labels by default
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # reset graph function activation
    def reset_button_action(self):
        self.input_button.setText("Input graph")    # changing the name of the button 'Change graph'
        self.fig = plt.cla()                        # clearing the drawing field, path's line input, answer field,
        self.canvas.draw()                          # log data
        self.textBrowser.clear()
        self.lineEdit.clear()
        self.log_data = ""
        del self.graph                              # recreating the graph
        self.graph = Graph()

    # alert raising function
    def alert_func(self, title, message):
        alert = QtWidgets.QMessageBox.critical(self, title, message, QtWidgets.QMessageBox.Ok)

    # show button action
    def show_button_clicked(self):              # function that shows the chosen path
        if len(self.graph.paths) == 0:          # checking for an empty field
            return
        line = self.lineEdit.text()             # reading the field
        edges_path = []
        try:                                    # checking the correctness of type of entered number
            num = int(line)
        except Exception:
            self.alert_func("Wrong type!", "Inputting value must be an integer number!")
            return

        if not (0 <= num < self.graph.N):       # checking the correctness of entered value
            self.alert_func("Wrong value!", "Inputting value must be a natural number before %d!" % (self.graph.N))
            return

        # getting the path until the vertex with the name of entered number
        for i in range(len(self.graph.paths[num]) - 1):
            edges_path.append((self.graph.paths[num][i], self.graph.paths[num][i + 1]))
        if not edges_path or edges_path[0][0] != self.graph.start:    # checking the ability to start the path from
            edges_path = None                                    # the start vertex and the existence of chosen path
        self.drawing_graph_func(num, edges_path)                 # drawing the path

    # cancel button activation
    def cancel_button_clicked(self):        # erase the selected path and clear the text line
        self.lineEdit.clear()
        if len(self.graph.paths) == 0:
            return
        self.drawing_graph_func(-2, None)

    # input button action activation function
    def input_button_clicked(self):
        dlg = InputDialog(self.graph)               # calling the Input Dialog window
        dlg.exec()
        self.graph.checking()                       # checking data correctness in case of incorrect input
        if self.graph.N is None:                    # returning if no graph entered
            return
        self.input_button.setText("Change graph")   # changing the name of the button
        self.drawing_graph_func(-1, None)           # drawing the entered graph

    # log button action activation function
    def log_button_clicked(self):
        dlg = LogDialog(self.log_data)              # opening the log window
        dlg.exec()

    # help button action activation function
    def help_button_clicked(self):
        dlg = HelpDialog()              # opening the help window
        dlg.exec()

    # drawing graph function
    def drawing_graph_func(self, num, edges_path):
        self.fig = plt.cla()                            # clearing the drawing field
        G = nx.MultiDiGraph()                           # creating digraph for drawing
        for key in self.graph.edges.keys():             # adding edges
            G.add_edge(key[0], key[1])
        pos = nx.shell_layout(G)                        # setting the pose
        options = {
            'node_color': 'green',  # color of node
            'node_size': 1500,  # size of node
            'width': 1,  # line width of edges
            'arrowstyle': '-|>',  # array style for directed graph
            'arrowsize': 18,  # size of arrow
            'edge_color': 'blue',  # edge color
        }
        try:
            nx.draw(G, pos, with_labels=True, arrows=True, **options)   # drawing the graph
            if num != -1:                                               # drawing the start vertex
                if edges_path is not None:                             # drawing the path
                    nx.draw_networkx(
                        G,
                        pos,
                        with_labels=True,
                        edgelist=edges_path,
                        edge_color="red",
                        nodelist=self.graph.paths[num],
                        node_size=1500,
                        node_color="yellow",
                        arrowstyle='-|>',
                        arrowsize=18,
                        width=2,
                    )
                nx.draw_networkx_nodes(G, pos, node_size=1500, nodelist=[self.graph.start], node_color="orange")
            nx.draw_networkx_edge_labels(G, pos, self.graph.edges, font_color='black')      # drawing the labels
        except nx.NetworkXError:
            self.fig = plt.cla()                        # clear field in case of an error
        self.fig = plt.figure(1, figsize=(5, 4))        # setting a figure where to draw
        self.canvas.draw()                              # finally draw the graph on a field

    # start action button
    def start_alg_button(self):
        if self.graph.N is None:        # returning if no graph entered
            return
        self.textBrowser.clear()        # clearing the text plain
        self.log_data = ""              # clearing the log data

        # calling the algorithm function and getting answer-data and log-data
        data, self.log_data = FB_alg(self.graph.N, self.graph.start, self.graph.edges, self.graph.paths)
        self.textBrowser.setText(data)      # initializing the text plain with the answer-data
        self.drawing_graph_func(-2, None)   # drawing the start vertex in graph and graph itself


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate      # initialize labels by default
        Dialog.setWindowTitle(_translate("Main_win", "Main window"))
        self.start_button.setText(_translate("Dialog", "Start the algorithm"))
        self.reset_button.setWhatsThis(_translate("Dialog", "<html><head/><body><p>button</p></body></html>"))
        self.reset_button.setText(_translate("Dialog", "Reset"))
        self.input_button.setText(_translate("Dialog", "Input graph"))
        self.name.setText(_translate("Dialog",
            "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Visualization of the Ford-Bellman algorithm</span></p></body></html>"))
        self.log_button.setText(_translate("Dialog", "log"))
        self.help_button.setText(_translate("Dialog", "?"))
        self.show_button.setText(_translate("Dialog", "Show"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog",
                                    "<html><head/><body><p><span style=\" font-size:10pt;\">Path until:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "End-vertex"))
        self.label_4.setText(_translate("Dialog", "Distance"))