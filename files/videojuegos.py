#!/usr/bin/env python3

juegos = ["Super Mario Bros", "The Elder Scrolls", "Call of Duty", "Blasphemous"]
max = 500

# Géneros
generos = {
    "Super Mario Bros": "Aventura",
    "The Elder Scrolls": "Rol",
    "Call of Duty": "Shooter",
    "Blasphemous": "Indie"
}

# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "The Elder Scrolls": (600, 20),
    "Call of Duty": (60, 120),
    "Blasphemous": (924, 3)
}

# Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Edu", "Pepe", "Juan"},
    "The Elder Scrolls": {"Marcelo", "Jose", "Luis"},
    "Call of Duty": {"Sergio", "Juan", "Edu"},
    "Blasphemous": {"Sergio", "Pepe", "Antonio", "Alberto"},
}


# Sumario
def sumario(juego):
    print(f"\n[Info] Resumen del juego {juego}")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Stock disponible: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

for juego in juegos:
    if ventas_y_stock[juego][0] > max:
        sumario(juego)

total_ventas = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > max)
print(f"\n[Info] Total de ventas: {total_ventas()}")