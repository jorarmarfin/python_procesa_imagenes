import os
import sys
import redimensiona
import recorta
import fondo_blanco
import depura
import recorte_unitario

# Códigos ANSI para colores
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_AMARILLO = "\033[93m"
COLOR_AZUL = "\033[94m"
COLOR_RESET = "\033[0m"  # Restablecer el color a su valor predeterminado


def funcion0():
    depura.imagenes()


def funcion1():
    # Verifica si se proporciona un ancho personalizado como argumento
    if len(sys.argv) > 1:
        try:
            ancho_personalizado = int(sys.argv[1])
            redimensiona.redimensionar_imagenes(ancho_personalizado)
        except ValueError:
            imprimir_texto_coloreado("El argumento debe ser un número entero válido.", COLOR_ROJO)
    else:
        # Solicita el ancho deseado si no se proporciona un argumento
        try:
            ancho_deseado = int(input("Introduce el ancho deseado (por defecto: 2048): "))
        except ValueError:
            ancho_deseado = 2048  # Valor predeterminado en caso de entrada no válida
        redimensiona.redimensionar_imagenes(ancho_deseado)


def funcion2():
    recorta.rostro()


def function3():
    fondo_blanco.cambiar_fondo_blanco()


def funcion5():
    recorte_unitario.rostro_unitario()


def menu():
    while True:
        imprimir_texto_coloreado("Menú:", COLOR_VERDE)
        imprimir_texto_coloreado("0. Depura imagenes", COLOR_AZUL)
        imprimir_texto_coloreado("1. Redimensionar imagen", COLOR_AZUL)
        imprimir_texto_coloreado("2. Recortar rostro", COLOR_AZUL)
        imprimir_texto_coloreado("3. Recortar rostro unitario", COLOR_AZUL)
        imprimir_texto_coloreado("4. Cambiar fondo de imagen", COLOR_AZUL)
        imprimir_texto_coloreado("5. Salir", COLOR_AZUL)

        opcion = input("Selecciona una opción: ")

        if opcion == '0':
            funcion0()
        elif opcion == '1':
            funcion1()
        elif opcion == '2':
            funcion2()
        elif opcion == '3':
            funcion5()
        elif opcion == '4':
            function3()
        elif opcion == '5':
            imprimir_texto_coloreado("Adiós.", COLOR_ROJO)
            break
        else:
            imprimir_texto_coloreado("Opción no válida. Introduce un número del 1 al 4.", COLOR_AZUL)


def imprimir_texto_coloreado(texto: any, color: any):
    print(f"{color}{texto}{COLOR_RESET}")


if __name__ == "__main__":
    menu()
