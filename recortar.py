import cv2
import os

def recorta_rostros(args):
    # Directorio de entrada y salida
    directorio_entrada = os.getcwd()
    directorio_salida = 'recorte'
    archivo_salida = 'salida.txt'

    # Crea el directorio de salida si no existe
    os.makedirs(directorio_salida, exist_ok=True)