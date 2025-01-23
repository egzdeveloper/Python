class Libro:
    def __init__(self, id, autor, titulo):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.prestado = False
    
    def __str__(self):
        return f"Libro ({self.id}, {self.autor}, '{self.titulo}')"
    
    def __repr__(self):
        return self.__str__()