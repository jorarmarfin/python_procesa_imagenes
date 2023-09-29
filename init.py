import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QTextEdit

from redimensionar import redimensiona_imagenes
from recortar import recorta_rostros

class OpenCVThread(QThread):
    finished = pyqtSignal()

    def run(self):
        # Tu función de OpenCV aquí
        recorta_rostros()
        # Realiza las operaciones de OpenCV

        # Emite la señal de finalización cuando termine
        self.finished.emit()

class OpenPictureThread(QThread):
    finished = pyqtSignal(str)

    def run(self):
        # Realiza las operaciones de OpenCV
        texto = redimensiona_imagenes()
        # Emite la señal de finalización cuando termine
        self.finished.emit(texto)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 1044, 700)
        # Crear un botón llamado "Redimensionar"
        button_redimensionar = QPushButton('Redimensionar', self)
        button_redimensionar.setGeometry(10, 10, 150, 30)

        # Crear un botón llamado "Cortar"
        button_cortar = QPushButton('Extrae rostro', self)
        button_cortar.setGeometry(180, 10, 150, 30)

        # Conectar el botón a la función "ejecutar_redimensionar"
        button_redimensionar.clicked.connect(self.startPictureThread)


        # Crea un QTextEdit para mostrar los mensajes
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 50, 1024, 400)  # Ajusta la posición y el tamaño del QTextEdit

    def startPictureThread(self):
        self.thread = OpenPictureThread()
        self.thread.finished.connect(self.onPictureFinished)
        self.thread.start()

    def onPictureFinished(self,text):
        # Aquí puedes realizar acciones después de que la función de OpenCV haya terminado
        self.text_edit.append(text)


if __name__ == '__main__':
    # Crear una aplicación PyQt
    app = QApplication(sys.argv)
    window = MainWindow()
    # Mostrar la ventana principal
    window.show()
    # Iniciar el bucle de eventos de la aplicación
    sys.exit(app.exec_())
