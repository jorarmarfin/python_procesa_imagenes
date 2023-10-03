import cv2
import os

# Directorio de entrada y salida
directorio_entrada = os.getcwd()
directorio_salida = 'recorte'
archivo_salida = 'salida.txt'

# Crea el directorio de salida si no existe
os.makedirs(directorio_salida, exist_ok=True)

# Abre un archivo de salida para registrar las respuestas
with open(archivo_salida, 'w') as f:
    # Carga el clasificador de detección de rostros preentrenado
    clasificador_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Proporciones para el recorte
    proporcion_ancho = 3
    proporcion_alto = 4

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

                        ancho_recorte = w
                        alto_recorte = int(ancho_recorte * proporcion_alto / proporcion_ancho)

                        rostro_recortado = imagen[y - 250:y + alto_recorte-80, x-80:x + ancho_recorte+100]

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