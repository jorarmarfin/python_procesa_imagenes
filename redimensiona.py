from PIL import Image
import os

# Directorio actual
directorio_actual = os.getcwd()

# Ancho deseado después de la redimensión
ancho_deseado = 2048

# Variable para almacenar los mensajes
mensajes = []

# Recorre todas las imágenes en el directorio actual
for archivo in os.listdir(directorio_actual):
    if archivo.endswith(('.jpg', '.jpeg', '.png')):  # Filtra por extensiones de imagen
        ruta_archivo = os.path.join(directorio_actual, archivo)
        try:
            with Image.open(ruta_archivo) as img:
                ancho_original, alto_original = img.size
                if ancho_original < 1000:
                    # Calcula el alto proporcional
                    alto_deseado = int(alto_original * (ancho_deseado / ancho_original))
                    
                    # Redimensiona la imagen manteniendo la proporción
                    img_resized = img.resize((ancho_deseado, alto_deseado), Image.ANTIALIAS)
                    
                    # Guarda la imagen redimensionada (sobrescribe la original)
                    img_resized.save(ruta_archivo)
                    
                    mensaje = f"Imagen redimensionada: {ruta_archivo}"
                    print(mensaje)
        except Exception as e:
            mensaje = f"Error al procesar la imagen {ruta_archivo}: {str(e)}"
            print(mensaje)

print("Proceso completado. Las imágenes han sido redimensionadas.")
