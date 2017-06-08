import sys

from PyQt4 import QtGui, QtCore

from app.test_app import Ui_TestGUI

class TestGUI(QtGui.QMainWindow):

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_TestGUI()
        self.ui.setupUi(self)

        self.QMainWindow = QtGui.QMainWindow(self)
        self.main_widget = QtGui.QWidget(self)
        self.__connect()

    def __connect(self):

        self.ui.button.clicked.connect(self.dummy)
        self.ui.button.clicked.connect(self.toggle_led)

    @QtCore.pyqtSlot()
    def dummy(self):
        print("Dummy SLOT activated")

    @QtCore.pyqtSlot()
    def toggle_led(self):
        print("Toggling LED.")
        self.ui.led.toggle()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    gui = TestGUI()
    gui.show()
    app.exec_()
