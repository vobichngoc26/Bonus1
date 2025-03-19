from PyQt6.QtWidgets import QApplication, QMainWindow
from bonus1.MainWindowEx import MainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowEx()
myui.setupUi(mainwindow)
myui.show()
app.exec()