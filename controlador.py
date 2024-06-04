from modelo import *
from vista import *
import sys
from PyQt5.QtWidgets import QApplication

class coordinador:
    def __init__(self):
        self.database = ImagenDato()

    def add_img(self, data: dict):
        return self.database.agregar_imagen(data)

    def del_img(self, img_cod: str):
        return self.database.eliminar_imagen(img_cod)

    def search_img(self, img_cod: str = ''):
        return self.database.buscar_imagen(img_cod)



def main():
    app = QApplication(sys.argv)
    vista_= VentanaPrincipal()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
