from modelo import *
from controlador import coordinador
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QLabel, QWidget, QLineEdit, QTableWidgetItem,QPushButton
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator, QFont
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



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

    def mostrar_imagen(self, ruta):
        
        img = mpimg.imread(ruta)
        plt.imshow(img)
        plt.title('Imagen ingresada')
        plt.axis('off')

    #     eficiencia = "Eficiente" if conteo > 100 else "No eficiente"
    #     plt.figtext(0.5, 0.01, eficiencia, wrap=True, horizontalalignment='center', fontsize=12)
    #     plt.show()

    def close(self):
        QApplication.quit()


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
        
        self.mostrar_imagen(ruta, T)

    def mostrar_imagen(self, ruta):
        img = mpimg.imread(ruta)
        plt.imshow(img)
        plt.title('Imagen ingresada')
        plt.axis('off')

        eficiencia = "Eficiente" if conteo > 100 else "No eficiente"
        plt.figtext(0.5, 0.01, eficiencia, wrap=True, horizontalalignment='center', fontsize=12)
        plt.show()
        


    
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
            I = Imagen()
            T = I.ConteoPart(ruta)

            img = {'Ruta': ruta, 'Codigo': codigo, 'Numero_nano': T, 'Eficiencia': ''}
            isUnique = self.controller.add_img(img)
            if isUnique:
                msgBox = QMessageBox()
                msgBox.setText("Datos agregados exitosamente")
                msgBox.setWindowTitle(None)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

            self.mostrar_imagen(ruta, T)

    def mostrar_imagen(self, ruta, conteo):
        img = mpimg.imread(ruta)
        plt.imshow(img)
        plt.title(f'Imagen ingresada - Partículas: {conteo}')
        plt.axis('off')
        eficiencia = "Eficiente" if conteo > 100 else "No eficiente"
        plt.figtext(0.5, 0.01, eficiencia, wrap=True, horizontalalignment='center', fontsize=12)
        plt.show()

        I = Imagen()
        T = I.ConteoPart(ruta)
        
            


