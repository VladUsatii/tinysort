#!python3
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys, os
import webbrowser

class Screen(QMainWindow):
	def __init__(self):
		super().__init__()

		self.mwidget = QMainWindow(self)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setFixedSize(1920//2, 1080//2)
		self.center()

		def label(text, style, X, Y, posX, posY):
			self.lbl = QLabel(self)
			self.lbl.setText(text)
			self.lbl.setStyleSheet(style)
			self.lbl.setGeometry(X, Y, posX, posY)
			self.lbl.setAlignment(Qt.AlignCenter)

		def imp():
			print("Yeet")


		# important text and buttons
		label(text="tinysort", style="color: rgb(255, 255, 255);font:32pt 'Proxima Nova';", X=0, Y=1080//6, posX=1920//2, posY=1080//16)

		self.quitBtn = QPushButton('╳', self)
		self.quitBtn.setStyleSheet("background-color: transparent;border:0px solid white;color: rgb(255, 255, 255);")
		self.quitBtn.setToolTip('Quit')
		self.quitBtn.setGeometry(0, 0, 50, 50)
		self.quitBtn.clicked.connect(self.close)
	
		self.importBtn = QPushButton('Import Data (.csv)', self)
		self.importBtn.setStyleSheet("background-color: transparent;border:2px solid white;color: rgb(255, 255, 255);padding: 5px;")
		self.importBtn.setToolTip('Import data in the form of a csv file, only. This is so that we can read your data in the correct formatting.')
		self.importBtn.setGeometry(1920//4 - 210, 1080//4, 200, 50)

		self.openSourceBtn = QPushButton('Fork on GitHub', self)
		self.openSourceBtn.setStyleSheet("background-color: black;border:2px solid black;color: rgb(255, 255, 255);padding: 5px;")
		self.openSourceBtn.setToolTip('Fork on my GitHub')
		self.openSourceBtn.setGeometry(1920//4 + 10, 1080//4, 200, 50)
		self.openSourceBtn.clicked.connect(lambda: webbrowser.open('https://github.com/VladUsatii/tinysort'))


		# credits text
		label(text="Copyright © 2020 readproduct.com. All rights reserved.", style="color: rgb(150, 150, 150);font:14pt 'Proxima Nova';", X=0, Y=1080//2.25, posX=1920//2, posY=1080//16)
		

		self.oldPos = self.pos()
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		delta = QPoint(event.globalPos() - self.oldPos)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()

app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: #121212;border: 0px solid white;}")

screen = Screen()

if __name__ == '__main__':
	Screen()
	sys.exit(app.exec_())
