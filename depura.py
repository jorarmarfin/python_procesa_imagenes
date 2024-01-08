import subprocess

def imagenes():
    # Comando de ejemplo
    comando = 'find . -type f -exec sh -c \'if [ -e "/mnt/DATOS/OCAD/2024-1/ADMISION/fotos/{}" ]; then rm "{}"; fi\' \\;'

    # Ejecuta el comando y captura la salida
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Imprime la salida estándar y la salida de error
    print("Salida estándar:")
    print(resultado.stdout)

    print("Salida de error:")
    print(resultado.stderr)

    # Verifica el código de salida (0 significa éxito)
    if resultado.returncode == 0:
        print("El comando se ejecutó con éxito.")
    else:
        print("El comando falló con código de salida:", resultado.returncode)
