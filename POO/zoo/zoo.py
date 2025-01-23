class Zoo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        print(f"\n[+] Mostrando los animales del zoo")
        for animal in self.animales:
            print(f"\t{animal}")

    def alimentar_animales(self):
        print(f"\n[+] Alimentando a todos los animales...")
        for animal in self.animales:
            animal.alimentar()

    def liberar_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                print(f"\n[+] Liberando a {nombre}...")
                self.animales.remove(animal)
                return
        
        print(f"\n[+] No se ha encontrado ningún animal llamado {nombre}...")
                