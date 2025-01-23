#!/usr/bin/env python3

from vehiculo import Vehiculo
from flota import Flota

if __name__ == "__main__":

    flota = Flota()
    flota.agregar_vehiculo(Vehiculo("7811 BXC", "Renault", "Clio"))
    flota.agregar_vehiculo(Vehiculo("1281 AAA", "Honda", "Civic"))
    flota.agregar_vehiculo(Vehiculo("5435 DFS", "Citroen", "C3"))

    flota.mostrar_vehiculos()
    flota.alquilar_vehiculo("1281 AAA")
    flota.mostrar_vehiculos()
    flota.alquilar_vehiculo("1281 AAA")
    flota.recuperar_vehiculo("1281 AAA")
    flota.recuperar_vehiculo("1281 AAA")
    flota.mostrar_vehiculos()