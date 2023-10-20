import cv2
import os
import urllib.request
import sys


def rostro_unitario():
    # Solicita el nombre del archivo de imagen
    nombre_archivo = input("Ingresa el nombre del archivo de imagen (por ejemplo, foto.jpg): ")

    # Verifica si el archivo de imagen especificado existe
    if not os.path.isfile(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.")
        sys.exit(1)

    # Crea una carpeta llamada "recorte" si no existe
    carpeta_recorte = 'recorte'
    os.makedirs(carpeta_recorte, exist_ok=True)

    # Carga la imagen
    imagen = cv2.imread(nombre_archivo)

    # Descarga el clasificador de detección de rostros desde la web de OpenCV
    url_clasificador = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml"
    nombre_archivo_clasificador = "haarcascade_frontalface_alt.xml"

    urllib.request.urlretrieve(url_clasificador, nombre_archivo_clasificador)

    # Carga el clasificador de detección de rostros
    clasificador_rostros = cv2.CascadeClassifier(nombre_archivo_clasificador)

    # Convierte la imagen a escala de grises (la detección de rostros funciona mejor en imágenes en escala de grises)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detecta rostros en la imagen
    rostros = clasificador_rostros.detectMultiScale(imagen_gris, 1.3, 5)

    # Proporciones para el recorte
    margin_y = 0.20
    margin_y2 = 0.10
    margin_x = 0.1

    # Si se detectan rostros, recorta la región del primer rostro encontrado
    if len(rostros) > 0:
        x, y, w, h = rostros[0]  # Obtiene las coordenadas del primer rostro

        delta_y = int(margin_y * y)
        delta_y2 = int(margin_y2 * y)
        delta_x = int(margin_x * x)
        x1, y1 = x - delta_x, y - delta_y
        x2, y2 = x + w + delta_x, y + h + delta_y2
        print(y, delta_y, y1)

        rostro_recortado = imagen[y1:y2, x1:x2]

        # Obtén la extensión del archivo original
        nombre_base, extension = os.path.splitext(os.path.basename(nombre_archivo))

        # Guarda la región del rostro recortado en un archivo en la carpeta "recorte"
        nombre_recorte = os.path.join(carpeta_recorte, f"{nombre_base}{extension}")

        # Intenta guardar la región del rostro recortado en un archivo
        if cv2.imwrite(nombre_recorte, rostro_recortado):
            print(f"Rostro recortado y guardado en {nombre_recorte}.")
        else:
            print("Error al guardar la imagen recortada.")
    else:
        print(f"No se detectaron rostros en la imagen. {nombre_archivo}")


if __name__ == "__main__":
    rostro_unitario()
