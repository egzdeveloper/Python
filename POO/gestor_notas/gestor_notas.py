#!/usr/bin/env python3

import pickle
from nota import Nota

class GestorNotas:
    def __init__(self, archivo = 'notas.pkl'):
        self.archivo = archivo

        try:
            with open(self.archivo, 'rb') as f:
                self.notas = pickle.load(f)

        except FileNotFoundError:
            self.notas = []

    def actualizar(self):
        with open(self.archivo, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.actualizar()

    def leer_notas(self):
        print("\n[+] Mostrando todas las notas:")
        return self.notas

    def buscar_nota(self, texto):
        print(f"\n[+] Mostrando las notas que coinciden con el criterio de búsqueda:")
        return [nota for nota in self.notas if nota.coincide(texto)]

    def eliminar_nota(self, index):
        if index < len(self.notas):
            del self.notas[index]
            self.actualizar()