class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro):
        if libro.id not in self.libros:
            self.libros[libro.id] = libro
        else:
            print("No es posible agregar el libro con ID {libro.id}")

    def prestar_libro(self, id):
        if id in self.libros and not self.libros[id].prestado:
            self.libros[id].prestado = True
        else:
            print(f"No es posible prestar el libro con ID {id}")

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.prestado]

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.prestado]