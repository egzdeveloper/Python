class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                print(f"\n[+] Alquilando {vehiculo.marca} {vehiculo.modelo} [{vehiculo.matricula}]")
                vehiculo.alquilar()  

    def recuperar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                print(f"\n[+] Recuperando {vehiculo.marca} {vehiculo.modelo} [{vehiculo.matricula}]")
                vehiculo.recuperar()  

    def mostrar_vehiculos(self):
        print(f"\n[+] Mostrando la flota de vehículos")
        for vehiculo in self.vehiculos:
            print(vehiculo)