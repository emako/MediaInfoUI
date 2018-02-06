import sys
from PyQt5.QtWidgets import QTextEdit, QPushButton, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QMimeData, QSize, QRect
from PyQt5.QtGui import QDrag
import MediaInfoTodo as mitd

path = ''
mi = ''

class Ui_MediaInfo(QWidget):
    def setupUi(self, MediaInfo):
        MediaInfo.setObjectName("MediaInfo")
        MediaInfo.resize(700, 800)
        MediaInfo.setMinimumSize(QSize(700, 800))
        MediaInfo.setMaximumSize(QSize(700, 800))
        MediaInfo.setAcceptDrops(True)
        self.exitBt = QtWidgets.QPushButton(MediaInfo)
        self.exitBt.setGeometry(QRect(606, 771, 93, 28))
        self.exitBt.setObjectName("exitBt")
        self.saveBt = SaveBt('Save', MediaInfo)
        self.copyBt = CopyBt('Copy', MediaInfo)
        self.mediainfoEdit = TextEdit(self.copyBt.getMi(), MediaInfo)
		
        self.retranslateUi(MediaInfo)
        QtCore.QMetaObject.connectSlotsByName(MediaInfo)
		
        self.exitBt.clicked.connect(MediaInfo.close)
        self.copyBt.clicked.connect(self.copyBt.copyBt_click)
        self.saveBt.clicked.connect(self.saveBt.saveBt_click)

    def retranslateUi(self, MediaInfo):
        _translate = QtCore.QCoreApplication.translate
        MediaInfo.setWindowTitle(_translate("MediaInfo", "MediaInfo"))
        self.exitBt.setText(_translate("MediaInfo", "Exit"))
        self.mediainfoEdit.setPlaceholderText(_translate("MediaInfo", "Please drag and drop a media file here ..."))


class TextEdit(QTextEdit):
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.setObjectName("mediainfoEdit")
		self.setMinimumSize(QSize(700, 770))
		self.setMaximumSize(QSize(700, 770))
		self.setGeometry(QRect(0, 0, 700, 770))
		self.setText(title)

	def dragEnterEvent(self, event):
		event.accept()

	def dropEvent(self, event):
		global path
		global mi
		for url in event.mimeData().urls():
			path = url.toString()[8:]
			mi = mitd.GetMediaInfo(path)
			self.setText(mi)
			print(mi)
			break

class SaveBt(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.setObjectName("saveBt")
		self.setGeometry(QRect(406, 771, 93, 28))

	def saveBt_click(self, flag):
		global mi
		if mi != '':
			with open('{path}.txt'.format(path=path), 'w+') as f:
				f.write(mi)

class CopyBt(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.setObjectName("saveBt")
		self.setGeometry(QRect(506, 771, 93, 28))

	def copyBt_click(self, flag):
		global mi
		if mi != '':
			clipboard = QtWidgets.QApplication.clipboard()
			clipboard.setText(mi)
			
	def getPath(self):
		global path
		return path
		
	def getMi(self):
		global mi
		mi = mitd.GetMediaInfo(path)
		return mi

class SysArgv():
	def __init__(self, argv):
		global path
		global mi
		try:
			path = argv[1]
			print(path)
		except:
			pass
		if path != '':
			mi = mitd.GetMediaInfo(path)

			
"""
global path
global mi
if path != '':
mi = mitd.GetMediaInfo(path)
self.mediainfoEdit.setText(mi)
print(mi)
"""