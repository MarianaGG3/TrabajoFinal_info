from modelo import *
from vista import *
import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    vista_= VentanaPrincipal()
    vista_.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
