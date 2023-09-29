# Procesa imagenes


## Como usarlo
crear el ejecutable y colocarlo dentro de la carpeta de fotos a procesar

## compilar
~~~
pyinstaller --onefile init.py
~~~

## Comandos
~~~
find . -type f -exec sh -c 'if [ -e "/mnt/DATOS/OCAD/2024-1/IEN/fotos/{}" ]; then rm "{}"; fi' \;

~~~
