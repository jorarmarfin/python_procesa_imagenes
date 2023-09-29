
import os
import cv2
def recorta_rostro():
    # Directorio de entrada y salida
    directorio_entrada = os.getcwd()
    directorio_salida = 'recorte'
    archivo_salida = 'salida.txt'
    # Crea el directorio de salida si no existe
    os.makedirs(directorio_salida, exist_ok=True)
    with open(archivo_salida, 'w') as f:
        # Carga el clasificador de detección de rostros preentrenado
        clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
