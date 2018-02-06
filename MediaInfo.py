import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5 import QtGui
from MediaInfoUI import *
from MediaInfoICO import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	argv = SysArgv(sys.argv)
	mainWindow = QMainWindow()
	ui = Ui_MediaInfo()
	ui.setupUi(mainWindow)
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(":/MediaInfo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	mainWindow.setWindowIcon(icon)
	mainWindow.show()
	sys.exit(app.exec_())