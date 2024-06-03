from modelo import *
from controlador import coordinador
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QLabel, QWidget, QLineEdit, QTableWidgetItem,QPushButton
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator, QFont
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("interfaz_menu.ui",self)
        self.setup()
        

    def setup(self):
        usu= ImagenDato()
        im=Imagen()
        self.agg=AgregarUsuario()
        #conteo_ = ConteoPart(self)
        self.ingresar.clicked.connect(self.agg.show)
        #self.ingresar_imagen.clicked.connect(im.AsignarImagenes)
        self.conteo.clicked.connect(self.abrir_conteo)
        self.salir.clicked.connect(self.close)

    def abrir_conteo(self):
        conteo_ = ConteoPart(self)
        conteo_.show()

    def close(self):
        QApplication.quit()



#No se ha creado
class ConteoPart(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("conteo.ui",self)
        self.setup()

    def setup(self):
        self.Aceptar.clicked.connect(self.conteo)
        self.Salir.clicked.connect(self.salir)

    def conteo(self):
        ruta = self.ruta.text()
        I = Imagen()
        T = I.ConteoPart(ruta)
        msgBox = QMessageBox()
        msgBox.setText("la imagen ingresada tiene: {}" .format(T))
        msgBox.setWindowTitle("conteo")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    
    def salir(self):
        self.hide()


class AgregarUsuario(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("agregar_pac.ui",self)
        self.controller= coordinador()
        self.setup()

    def setup(self):
        self.agregar.clicked.connect(self.agregar_img)


    def agregar_img(self):
        codigo = self.codigo.text()
        ruta = self.ruta.text()
        if not ruta or not codigo:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:

            img = {'Ruta':ruta, 'Codigo':codigo, 'Numero_nano':T,'Eficiencia': ''}
            isUnique = self.controller.add_img(img)
            if isUnique:
                msgBox = QMessageBox()
                msgBox.setText("Datos agregados exitosamente")
                msgBox.setWindowTitle(None)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

        I = Imagen()
        T = I.ConteoPart(ruta)
        msgBox = QMessageBox()
        msgBox.setText("la imagen ingresada tiene: {}" .format(T))
        msgBox.setWindowTitle("conteo")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
                
                
            


