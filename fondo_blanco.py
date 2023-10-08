import os
import subprocess

def cambiar_fondo_blanco(directorio_entrada="con_fondo", directorio_salida="sin_fondo"):
    """
    Cambia el fondo de las imágenes en el directorio de entrada a blanco y guarda las imágenes resultantes en el directorio de salida en formato JPEG.
    
    Args:
        directorio_entrada (str): Directorio de entrada con las imágenes originales (por defecto: "con_fondo").
        directorio_salida (str): Directorio de salida para guardar las imágenes procesadas (por defecto: "sin_fondo").
    """
    # Crea el directorio de salida si no existe
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Recorre todas las imágenes en el directorio de entrada
    for archivo_png in os.listdir(directorio_entrada):
        if archivo_png.endswith('.png'):
            # Construye las rutas de entrada y salida
            ruta_entrada = os.path.join(directorio_entrada, archivo_png)
            nombre_salida = os.path.splitext(archivo_png)[0] + '.jpeg'
            ruta_salida = os.path.join(directorio_salida, nombre_salida)

            # Ejecuta el comando convert para cambiar el fondo a blanco
            comando = [
                "convert",
                ruta_entrada,
                "-background",
                "white",
                "-flatten",
                ruta_salida
            ]

            try:
                # Ejecuta el comando
                subprocess.run(comando, check=True)
                print(f"Imagen con fondo cambiado a blanco guardada: {ruta_salida}")
            except subprocess.CalledProcessError as e:
                print(f"Error al procesar la imagen {ruta_entrada}: {e}")

    print("Proceso completado. Las imágenes con fondo cambiado a blanco se han guardado en el directorio 'sin_fondo' en formato JPEG.")
