class Vehiculo:
    def __init__(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"\tError: El vehículo ya está alquilado")

    def recuperar(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"\tError: El vehículo ya se encuentra disponible")

    def __str__(self):
        return f" - {self.marca} {self.modelo} [{self.matricula}] - {'Disponible' if self.disponible else 'Alquilado'}"