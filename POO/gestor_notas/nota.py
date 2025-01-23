#!/usr/bin/env python3

class Nota:
    def __init__(self, contenido):
        self.contenido = contenido

    def coincide(self, texto):
        return texto in self.contenido

    def __str__(self):
        return self.contenido