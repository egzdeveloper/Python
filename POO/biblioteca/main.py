#!/usr/bin/env python3

from libro import Libro
from biblioteca_infantil import BibliotecaInfantil

if __name__ == '__main__':

    biblioteca = BibliotecaInfantil()
    
    libro1 = Libro(1, 'Edu García', '¿Cómo ser un Lammer de Potencia máxima?')
    libro2 = Libro(2, 'Pepito Manolete', 'Aprende a colorear desde cero')

    biblioteca.agregar_libro(libro1, infantil = False)
    biblioteca.agregar_libro(libro2, infantil = True)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    biblioteca.prestar_libro(1, infantil = False)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}\n")

    biblioteca.prestar_libro(2, infantil = True)
    biblioteca.prestar_libro(1, infantil = False)

    print(f"\n[+] Libros prestados: {biblioteca.mostrar_libros_prestados}\n")
