#!/usr/bin/env python3
# (execute in terminal with	`chmod +x main.py` and `./main.py`)
#
# TinySort
#
# Extremely lightweight modeling software, used for production at readproduct.com/careers
#
#
#
# Created by Vlad Usatii in 2 Hours
#
# Full Open-Source Code
# MIT License
# Product
#

# qt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *

# sys tools
import sys, os
import webbrowser

# pil
from PIL import Image, ImageColor

# ml experimenting
import cv2

# math
import math
import random
import numpy as np
import scipy.misc as smp
import pandas as pd

# sdl2
import sdl2
import sdl2.ext

import subprocess

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

		# important text and buttons
		label(text="tinysort", style="color: rgb(255, 255, 255);font:32pt 'Proxima Nova';", X=0, Y=1080//6, posX=1920//2, posY=1080//16)

		self.quitBtn = QPushButton('╳', self)
		self.quitBtn.setStyleSheet("background-color: transparent;border:0px solid white;color: rgb(255, 255, 255);")
		self.quitBtn.setToolTip('Quit')
		self.quitBtn.setGeometry(0, 0, 50, 50)
		self.quitBtn.clicked.connect(self.close)

		self.needData = QPushButton('Confused about data? Read this.', self)
		self.needData.setStyleSheet("background-color: transparent;color: rgb(31, 128, 255);")
		self.needData.setToolTip("You will be taken to our documentation PDF.")
		self.needData.setGeometry(1920//5.75, 1080//2.5, 300, 50)
		self.needData.clicked.connect(lambda: self.learnAboutData())

	
		self.importBtn = QPushButton('Open Editor', self)
		self.importBtn.setStyleSheet("background-color: transparent;border:2px solid white;color: rgb(255, 255, 255);padding: 5px;")
		self.importBtn.setToolTip('Open the 2D and 3D editor before importing your .csv file.')
		self.importBtn.setGeometry(1920//4 - 210, 1080//4, 200, 50)
		self.importBtn.clicked.connect(lambda: self.openEditor())

		self.openSourceBtn = QPushButton('Fork on GitHub', self)
		self.openSourceBtn.setStyleSheet("background-color: black;border:2px solid black;color: rgb(255, 255, 255);padding: 5px;")
		self.openSourceBtn.setToolTip('Fork on my GitHub')
		self.openSourceBtn.setGeometry(1920//4 + 10, 1080//4, 200, 50)
		self.openSourceBtn.clicked.connect(lambda: webbrowser.open('https://github.com/VladUsatii/tinysort'))


		# credits text
		label(text="Open Source 2021 by readproduct.com. Created by Vlad Usatii.", style="color: rgb(150, 150, 150);font:14pt 'Proxima Nova';", X=0, Y=1080//2.25, posX=1920//2, posY=1080//16)
		

		self.oldPos = self.pos()
		self.show()

	def learnAboutData(self):
		# dialog process
		file = "/Users/vladusatii/Dev/sorting/documentation.pdf"
		webbrowser.open_new(file)

	def openEditor(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.AnyFile)
		dialog.setFilter(QDir.Files)
		if dialog.exec_():
			file_name = dialog.selectedFiles()
			if file_name[0] != "":
				with open(file_name[0], 'r') as f:
					self.useVc(list(f.readlines()), f.name)
			else:
				sys.exit(0)
		self.close()

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


	def useVc(self, coords, filename):
		ew = EditingWindow(filename)
		data = np.zeros((1920//2, 1080//2, 3), dtype=np.uint8)
		"""
		FILE STRUCTURE:
		X   Y   COLOR R   COLOR G   COLOR B
		X   Y   COLOR R   COLOR G   COLOR B
		... ...          ... ... ...
		"""
		coord_all = []
		for line in coords:
			coord_all.append(line.split())

		while True:
			for line in coord_all:
				if line[0].isdigit() and line[1].isdigit() and line[2].isdigit() and line[3].isdigit() and line[4].isdigit():
					x = int(line[0])
					y = int(line[1])
					r = int(line[2])
					g = int(line[3])
					b = int(line[4])
					data[x:x+10, y:y+10] = [r, g, b] # add as many as needed
				else:
					raise ValueError("\n\nThis file does not match the format 'X Y R G B'. Please revise and try again.\n\n")
			ew.blit(data.swapaxes(0, 1))
	
			# update page with changes
			updates = sdl2.ext.get_events()
			for event in updates:
				if event.type == sdl2.SDL_QUIT:
					sys.exit(0)


# base blitting template
class EditingWindow(object):
	def __init__(self, name):
		sdl2.ext.init()
		self.surf = sdl2.ext.Window(str(os.environ.get("USER")) + "\'s 2D Model --  " + str(name), size=(1920//2, 1080//2))
		self.surf.show()

	def blit(self, vc):
		win = sdl2.ext.pixels3d(self.surf.get_surface())
		win[:, :, 0:3] = vc.swapaxes(0, 1)
		self.surf.refresh()



app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: #121212}")

if __name__ == '__main__':
	running = False
	Screen()
	sys.exit(app.exec_())
