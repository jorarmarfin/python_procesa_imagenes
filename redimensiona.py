from PIL import Image
import os

COLOR_ROJO = "\033[91m"
COLOR_RESET = "\033[0m"
def redimensionar_imagenes(ancho_deseado=2048):
    # Directorio actual
    directorio_actual = os.getcwd()

    # Variable para almacenar los mensajes
    mensajes = []

    # Recorre todas las imágenes en el directorio actual
    for archivo in os.listdir(directorio_actual):
        if archivo.endswith(('.jpg', '.jpeg', '.png')):  # Filtra por extensiones de imagen
            ruta_archivo = os.path.join(directorio_actual, archivo)
            try:
                with Image.open(ruta_archivo) as img:
                    ancho_original, alto_original = img.size
                    if ancho_original < 1000 or ancho_deseado != 2048:
                        # Calcula el alto proporcional
                        alto_deseado = int(alto_original * (ancho_deseado / ancho_original))
                        
                        # Redimensiona la imagen manteniendo la proporción
                        img_resized = img.resize((ancho_deseado, alto_deseado), Image.ANTIALIAS)
                        
                        # Guarda la imagen redimensionada (sobrescribe la original)
                        img_resized.save(ruta_archivo)
                        
                        mensaje = f"Imagen redimensionada: {ruta_archivo}"
                        mensajes.append(mensaje)
                        print(f"{COLOR_ROJO}{mensaje}{COLOR_RESET}")
            except Exception as e:
                mensaje = f"Error al procesar la imagen {ruta_archivo}: {str(e)}"
                mensajes.append(mensaje)
                print(f"{COLOR_ROJO}{mensaje}{COLOR_RESET}")

    if mensajes:
        with open("redimensionamiento_log.txt", "w") as log_file:
            for mensaje in mensajes:
                log_file.write(mensaje + "\n")

    print("Proceso de redimensionamiento completado.")

# Ejecuta la función si se llama desde este script
if __name__ == "__main__":
    import sys

    # Verifica si se proporciona un ancho personalizado como argumento
    if len(sys.argv) > 1:
        try:
            ancho_personalizado = int(sys.argv[1])
            redimensionar_imagenes(ancho_personalizado)
        except ValueError:
            print(f"{COLOR_ROJO}El argumento debe ser un número entero válido.{COLOR_RESET}")
    else:
        redimensionar_imagenes()  # Usa el valor predeterminado de 2048 si no se proporciona un argumento
