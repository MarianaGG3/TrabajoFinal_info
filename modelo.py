from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
import cv2
import numpy as np
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt


class Imagen:
    def __init__(self):
        self.__ruta=""
        self.__usuario=int


    def asignarRuta(self,i):
        self.__numero_imagen=i

    def asignarUsuario(self, u):
        self.__usuario=u

    def verRuta(self):
        return self.__numero_imagen

    def verUsuario(self):
        return self.__usuario

    def ConteoPart(self, nombre_imagen):
        #nombre_imagen=input("ingrese el nombre de la imagen a realizar el conteo:")
        ima= cv2.imread(nombre_imagen)
        ima=cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
        imgB=ima[:,:,2]

        Umb,img=cv2.threshold(imgB ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        R=cv2.medianBlur(img, 5)

        kernel= np.ones((1,1),np.uint8)
        imaOp=cv2.morphologyEx(R, cv2.MORPH_CLOSE, kernel, iterations = 1)

        elem,mask=cv2.connectedComponents(imaOp)
        A = elem - 1
        return A

class ImagenDato:
    def __init__(self, host='localhost', database='final_infoII', user='root', password=''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conectar_db()
        self.crear_tabla_imagen()

    def conectar_db(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None

    def crear_tabla_imagen(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS imagenes (
            Codigo VARCHAR(255) PRIMARY KEY,
            Ruta VARCHAR(255),
            Numero_nano VARCHAR(255),
            Eficiencia VARCHAR(255)
        );
        """
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
        except Error as e:
            print(f"Error al crear la tabla: {e}")
    
    def cerrar_db(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def agregar_imagen(self,imagen:dict):
        if not self.buscar_imagen(imagen['Codigo']):
            query = "INSERT INTO imagenes (Codigo, Ruta, Numero_nano, Eficiencia) VALUES (%s, %s, %s, %s)"
            values = (imagen['Codigo'], imagen['Ruta'], imagen['Numero_nano'], imagen['Eficiencia'])
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        return False
        

    def eliminar_imagen(self, imagen_codigo: str):
        query = "DELETE FROM imagenes WHERE Codigo = %s"
        self.cursor.execute(query, (imagen_codigo,))
        self.connection.commit()
        return self.cursor.rowcount
    
    def buscar_imagen(self, imagen_codigo= str):
        query = "SELECT * FROM imagenes WHERE Codigo = %s"
        self.cursor.execute(query, (imagen_codigo,))
        return self.cursor.fetchone()


        

    




