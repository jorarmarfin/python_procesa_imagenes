import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QTextEdit

from redimensionar import redimensiona_imagenes


def ejecutar_redimensionar():
    text_edit.clear()
    # Llama a la función redimensiona_imagenes desde redimensionar.py
    mensajes = redimensiona_imagenes()
    
    # Agrega los mensajes al QTextEdit
    text_edit.append("Mensajes de redimensionar_imagenes:")
    text_edit.append(mensajes)

def ejecutar_cortar_rostro():
    # Llama a la función recorta_rostro desde recorte.py
    exec(open("recorte.py").read())
    

# Crear una aplicación PyQt
app = QApplication(sys.argv)

# Crear una ventana principal
window = QMainWindow()
window.setWindowTitle('Ventana Principal')
window.setGeometry(100, 100, 1044, 700)

# Crear un botón llamado "Redimensionar"
button_redimensionar = QPushButton('Redimensionar', window)
button_redimensionar.setGeometry(10, 10, 150, 30)

# Crear un botón llamado "Cortar"
button_cortar = QPushButton('Extrae rostro', window)
button_cortar.setGeometry(180, 10, 150, 30)

# Conectar el botón a la función "ejecutar_redimensionar"
button_redimensionar.clicked.connect(ejecutar_redimensionar)

# Conectar el botón a la función "ejecutar_cortar_rostro"
button_cortar.clicked.connect(ejecutar_cortar_rostro)

# Crea un QTextEdit para mostrar los mensajes
text_edit = QTextEdit(window)
text_edit.setGeometry(10, 50, 1024, 400)  # Ajusta la posición y el tamaño del QTextEdit


# Mostrar la ventana principal
window.show()

# Iniciar el bucle de eventos de la aplicación
sys.exit(app.exec_())
