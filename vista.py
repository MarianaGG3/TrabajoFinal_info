from modelo import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QLabel, QWidget, QLineEdit, QTableWidgetItem,QPushButton
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator, QFont
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('interfaz_menu.ui',self)

        self.ingresar_pac.clicked.connect(self.AgregarPac)
        self.ingresar_imagen.clicked.connect(self.AsignarImagenes)
        self.conteo.clicked.connect(self.ConteoPart)
        self.salir.clicked.connect(self.close)

    def AgregarPac(self):
        name = self.nombre.text()
        id = self.id.text()
        if not id or not name or not last_name or not age:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            pat = {'id':id, 'nombre':name, 'apellido': last_name, 'edad': age}
            isUnique = self.controller.add_patient(pat)
            