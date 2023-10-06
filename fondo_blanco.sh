#!/bin/bash

# Ruta del directorio donde se encuentran las imágenes PNG
directorio="."

# Itera a través de los archivos PNG en el directorio
for archivo_png in "$directorio"/*.png; do
    if [ -f "$archivo_png" ]; then
        # Obtiene el nombre del archivo sin la extensión
        nombre_sin_extension="${archivo_png%.*}"

        # Define el nombre del archivo JPEG de salida
        archivo_jpeg="$nombre_sin_extension.jpeg"

        # Convierte la imagen PNG en JPEG con fondo blanco
        convert "$archivo_png" -background white -flatten "$archivo_jpeg"

        # Comprueba si la conversión fue exitosa
        if [ $? -eq 0 ]; then
            echo "Se ha convertido $archivo_png a $archivo_jpeg"
        else
            echo "Error al convertir $archivo_png"
        fi
    fi
done

