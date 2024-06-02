from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pydicom
import matplotlib.pyplot as plt


class Imagen:
    def __init__(self):
        self.__numero_imagen=int
        self.__usuario=""


    def asignarNumeroImagen(self,i):
        self.__numero_imagen=i

    def asignarUsuario(self, u):
        self.__usuario=u

    def verNumeroImagen(self):
        return self.__numero_imagen

    def verUsuario(self):
        return self.__usuario

    def ConteoPart(self):
        nombre_imagen=input("ingrese el nombre de la imagen a realizar el conteo:")
        ima= cv2.imread(nombre_imagen)
        ima=cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
        imgB=ima[:,:,2]

        Umb,img=cv2.threshold(imgB ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        R=cv2.medianBlur(img, 5)

        kernel= np.ones((15,15),np.uint8)
        imaOp=cv2.morphologyEx(R, cv2.MORPH_CLOSE, kernel, iterations = 1)

        elem,mask=cv2.connectedComponents(imaOp)
        print(f'El número de nanoparticulas que se encuentran en la imagen es de:{elem-1}')

class Paciente:
    def __init__(self):
        self.__nombre="" 
        self.__cedula=0 
        self.__imagenes = {} 

    def AsignarNombre(self,n):
        self.__nombre=n 

    def AsignarCedula(self,c):
        self.__cedula=c 
    
    def TieneImagenes(self,nombre):
        return nombre.lower() in self.__imagenes 
  
    
    def AsignarImagenes(self,i):
        self.__imagenes[i.VerNombre().lower()] = i

    def VerNombre(self):
        return self.__nombre 

    def VerCedula(self):
        return self.__cedula 




