# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './app/test_app.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TestGUI(object):
    def setupUi(self, TestGUI):
        TestGUI.setObjectName(_fromUtf8("TestGUI"))
        TestGUI.resize(800, 600)
        self.centralwidget = QtGui.QWidget(TestGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridWidget = QtGui.QWidget(self.centralwidget)
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button = QtGui.QPushButton(self.gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setObjectName(_fromUtf8("button"))
        self.gridLayout.addWidget(self.button, 1, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.gridWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 2)
        self.led = LedWidget(self.gridWidget)
        self.led.setDiameter(18)
        self.led.setColor(QtGui.QColor(0, 255, 0))
        self.led.setState(True)
        self.led.setObjectName(_fromUtf8("led"))
        self.gridLayout.addWidget(self.led, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)
        TestGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TestGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TestGUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TestGUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TestGUI.setStatusBar(self.statusbar)

        self.retranslateUi(TestGUI)
        QtCore.QMetaObject.connectSlotsByName(TestGUI)

    def retranslateUi(self, TestGUI):
        TestGUI.setWindowTitle(_translate("TestGUI", "Test GUI", None))
        self.button.setText(_translate("TestGUI", "Eu gosto de tudo", None))

from ledwidget import LedWidget
