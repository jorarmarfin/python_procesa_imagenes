find . -type f -exec sh -c 'if [ -e "/mnt/DATOS/OCAD/2024-1/IEN/fotos/{}" ]; then rm "{}"; fi' \;