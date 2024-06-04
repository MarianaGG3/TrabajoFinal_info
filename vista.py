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
        self.im=Mostrar_info()
        self.agg=AgregarUsuario()
        #conteo_ = ConteoPart(self)
        self.ingresar.clicked.connect(self.agg.show)
        self.imag.clicked.connect(self.im.show)
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
        self.tabla= Mostrar_info()
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
            eficiencia = "Eficiente" if T > 100 else "No eficiente"

            img = {'Ruta': ruta, 'Codigo': codigo, 'Numero_nano': T, 'Eficiencia': eficiencia}
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
class Mostrar_info(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ventana_datos.ui', self)
        self.controller = coordinador()
        self.setup()

    def setup(self):
        self.busqueda.clicked.connect(self.buscar_imagen)
        self.tabla.verticalHeader().setVisible(False)
        self.readimagen()
        self.tableUpdate()

    def readimagen(self):
        self.listimagen = self.controller.search_img()

    def buscar_imagen(self):
        buscar = self.buscar.text()
        self.listimagen = self.controller.search_img(buscar)
        self.tableUpdate()

    def tableUpdate(self):
        self.tabla.setRowCount(len(self.listimagen))
        self.tabla.setColumnCount(6)
        columnas = ["Codigo", "Ruta", "Numero_nano", "Eficiencia", "Eliminar", "Ver"]
        columnLayout = ['Codigo', 'Ruta', 'Numero_nano', 'Eficiencia']
        self.tabla.setHorizontalHeaderLabels(columnas)
        for row, Imagen in enumerate(self.listimagen):
            for column in range(4):
                item = QTableWidgetItem(str(Imagen[columnLayout[column]]))
                self.tabla.setItem(row, column, item)
            
            btn = QPushButton('Borrar', self)
            btn.clicked.connect(lambda ch, r=row: self.Eliminar(r))
            self.tabla.setCellWidget(row, 4, btn)

            btn2 = QPushButton('visualizar', self)
            btn2.clicked.connect(lambda ch, r=row: self.Ver(r))
            self.tabla.setCellWidget(row, 5, btn2)
                
        self.tabla.setColumnWidth(0, 60)
        self.tabla.setColumnWidth(1, 110)
        self.tabla.setColumnWidth(2, 120)
        self.tabla.setColumnWidth(3, 60)
        self.tabla.setColumnWidth(4, 60)
        self.tabla.setColumnWidth(5, 60)

    def Eliminar(self, row):
        cod = self.tabla.item(row, 0).text()
        deleted = self.controller.del_img(cod)
        if deleted:
            self.readimagen()
            self.tableUpdate()
    def Ver(self,row):
        ruta= self.tabla.item(row,1).text()
        self.mostrar_imagen(ruta)

    def mostrar_imagen(self, ruta):
        img = mpimg.imread(ruta)
        plt.imshow(img)
        plt.title('Imagen ingresada')
        plt.axis('off')
        plt.show()
    
            


