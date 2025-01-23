class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {'Alimentado' if self.alimentado else 'Hambriento'}"
    
    def alimentar(self):
        self.alimentado = True