from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi



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

class Paciente:
    def __init__(self):
        self.__nombre="" 
        self.__cedula=0 
        self.__imagenes = {} 

    def AsignarNombre(self,n):
        self.__nombre=n 

    def AsignarCedula(self,c):
        self.__cedula=c 
    #metodo para verificar medicamentos
    def TieneImagenes(self,nombre):
        return nombre.lower() in self.__imagenes 
  
    #metodo para asignar un solo medicamento
    def AsignarImagenes(self,i):
        self.__imagenes[i.VerNombre().lower()] = i

    def VerNombre(self):
        return self.__nombre 

    def VerCedula(self):
        return self.__cedula 




