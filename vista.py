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
        self.setup()
        pac= Paciente()

    def setup(self):
        pac= Paciente()
        self.agg=Agregar_pac()
        self.conteo=pac.ConteoPart()
        self.ingresar_pac.clicked.connect(self.agg.show)
        self.ingresar_imagen.clicked.connect(pac.AsignarImagenes)
        self.conteo.clicked.connect(self.conteo)
        self.salir.clicked.connect(self.close)


#No se ha creado
class ConteoPart(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('conteo.ui',self)
        self.setup()

    def setup(self):
        pass


class Agregar_pac(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('agregar_pac.ui',self)
        self.setup()

    def setup(self):
        self.agregar.clicked.connect(self.AgregarPac)


    def AgregarPac(self):
        name = self.nombre.text()
        id = self.id.text()
        if not id or not name:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:

            pat = {'id':id, 'nombre':name}
            #self.close()
            msgBox = QMessageBox()
            msgBox.setText("paciente agregado exitosamente")
            msgBox.setWindowTitle(None)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            
            #isUnique = self.controller.add_patient(pat)


