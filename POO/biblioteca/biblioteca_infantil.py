from biblioteca import Biblioteca

class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_infantiles = {}

    def agregar_libro(self, libro, infantil):
        super().agregar_libro(libro)
        self.libros_infantiles[libro.id] = infantil

    def prestar_libro(self, id, infantil):
        if id in self.libros and self.libros_infantiles[id] == infantil and not self.libros[id].prestado:
            self.libros[id].prestado = True
        else:
            print(f"No es posible prestar el libro con ID {id}")