#!/usr/bin/env python3

import os
import pickle
from gestor_notas import GestorNotas

def main():

    gestor = GestorNotas()

    while True:
        print(f"\n---------------MENÚ----------------")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar una nota")
        print("4. Eliminar una nota")
        print("5. Salir")

        opcion = int(input("\n[+] Escoge una opción (1-5): "))

        if opcion == 1:
            contenido = input("\n[+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == 2:
            notas = gestor.leer_notas()
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == 3:
            texto = input("\n[+] Ingresa el texto a buscar en las notas: ")
            notas = gestor.buscar_nota(texto)
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == 4:
            index = int(input("\n[+] Introduce el número de la nota: "))
            gestor.eliminar_nota(index)

        elif opcion == 5:
            print("\n")
            break

        else:
            print("Elige una opción válida (1-5)...") 

        input(f"\n[+] Presiona <Enter> para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()