from PyQt5 import QtWidgets
from Main_win import MainWin


if __name__ == "__main__":                  # main function that runs the main window
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainWin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
