import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QTextEdit

# Importa la función desde redimensionar.py
from redimensionar import redimensiona_imagenes

def ejecutar_redimensionar():
    text_edit.clear()
    # Llama a la función redimensiona_imagenes desde redimensionar.py
    mensajes = redimensiona_imagenes()
    
    # Agrega los mensajes al QTextEdit
    text_edit.append("Mensajes de redimensionar_imagenes:")
    text_edit.append(mensajes)

# Crear una aplicación PyQt
app = QApplication(sys.argv)

# Crear una ventana principal
window = QMainWindow()
window.setWindowTitle('Ventana Principal')
window.setGeometry(100, 100, 1044, 700)

# Crear un botón llamado "Redimensionar"
button_redimensionar = QPushButton('Redimensionar', window)
button_redimensionar.setGeometry(10, 10, 150, 30)

# Conectar el botón a la función "ejecutar_redimensionar"
button_redimensionar.clicked.connect(ejecutar_redimensionar)

# Crea un QTextEdit para mostrar los mensajes
text_edit = QTextEdit(window)
text_edit.setGeometry(10, 50, 1024, 400)  # Ajusta la posición y el tamaño del QTextEdit


# Mostrar la ventana principal
window.show()

# Iniciar el bucle de eventos de la aplicación
sys.exit(app.exec_())
