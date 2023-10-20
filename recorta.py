import cv2
import os
import urllib.request

def rostro():
    # Directorio de entrada y salida
    directorio_entrada = os.getcwd()
    directorio_salida = 'recorte'
    archivo_salida = 'salida.txt'

    # Crea el directorio de salida si no existe
    os.makedirs(directorio_salida, exist_ok=True)

    # Abre un archivo de salida para registrar las respuestas
    with open(archivo_salida, 'w') as f:
        # Descarga el clasificador de detección de rostros desde la web de OpenCV
        url_clasificador = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml"
        nombre_archivo_clasificador = "haarcascade_frontalface_alt.xml"

        urllib.request.urlretrieve(url_clasificador, nombre_archivo_clasificador)

        # Carga el clasificador de detección de rostros
        clasificador_rostros = cv2.CascadeClassifier(nombre_archivo_clasificador)

        # Proporciones para el recorte
        margin_y = 0.60
        margin_y2 = 0.3
        margin_x = 0.1

        # Recorre todas las imágenes en el directorio de entrada
        for archivo in os.listdir(directorio_entrada):
            if archivo.endswith(('.jpg', '.jpeg', '.png')):
                ruta_archivo = os.path.join(directorio_entrada, archivo)
                imagen = cv2.imread(ruta_archivo)

                try:
                    if imagen is not None:
                        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                        rostros = clasificador_rostros.detectMultiScale(imagen_gris, scaleFactor=1.3, minNeighbors=5)

                        if len(rostros) > 0:
                            x, y, w, h = rostros[0]  # Obtiene las coordenadas del primer rostro

                            delta_y = int(margin_y * y)
                            delta_y2 = int(margin_y2 * y)
                            delta_x = int(margin_x * x)
                            x1, y1 = x - delta_x, y - delta_y
                            x2, y2 = x + w + delta_x, y + h + delta_y2

                            rostro_recortado = imagen[y1:y2, x1:x2]

                            nombre_base, extension = os.path.splitext(archivo)
                            nombre_recorte = os.path.join(directorio_salida, f"{nombre_base}{extension}")

                            if cv2.imwrite(nombre_recorte, rostro_recortado):
                                respuesta = f"Rostro recortado y guardado en {nombre_recorte}."
                            else:
                                respuesta = f"Error al guardar la imagen recortada"
                        else:
                            respuesta = f"No se detectaron rostros en la imagen: {archivo}"
                    else:
                        respuesta = f"Error al cargar la imagen: {archivo}"
                except Exception as e:
                    respuesta = f"Error al procesar la imagen {archivo}: {str(e)}"

                # Escribe la respuesta en el archivo de salida
                f.write(respuesta + '\n')

    print("Proceso completado. Los resultados se han registrado en 'salida.txt'.")

# Puedes llamar a esta función en tu script principal
if __name__ == "__main__":
    rostro()
