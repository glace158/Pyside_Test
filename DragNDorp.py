import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QTextEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class ListView(QListView):
	def __init__(self):
		super().__init__()
		self.setAcceptDrops(True)
		self.setModel(QStandardItemModel(0, 1))

	def dragEnterEvent(self, event):
		event.accept() if event.mimeData().hasText() else event.ignore()

	def dragMoveEvent(self, event):
		event.accept() if event.mimeData().hasText() else event.ignore()

	def dropEvent(self, event):
		if event.mimeData().hasText():
			event.setDropAction(Qt.CopyAction)
			self.model().appendRow(QStandardItem(event.mimeData().text()))
			event.accept()
		else:
			event.ignore()


class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.window_width, self.window_height = 1200, 800
		self.setMinimumSize(self.window_width, self.window_height)

		layout = QHBoxLayout()
		self.setLayout(layout)

		textEdit = QTextEdit()
		lstView = ListView()

		layout.addWidget(textEdit)
		layout.addWidget(lstView)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget {
			font-size: 30px;
		}
	''')
	
	myApp = MyApp()
	myApp.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')