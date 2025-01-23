#!/usr/bin/env python3

from animal import Animal
from zoo import Zoo

if __name__ == "__main__":

    zoo = Zoo('Zoo de Barcelona')

    gato = Animal('Michi', 'Gato')
    perro = Animal('Toby', 'Perro')

    zoo.agregar_animal(gato)
    zoo.agregar_animal(perro)

    zoo.mostrar_animales()
    zoo.alimentar_animales()
    zoo.mostrar_animales()

    zoo.liberar_animal('Toby')
    zoo.mostrar_animales()