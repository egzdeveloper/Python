import os

directorio_actual = os.getcwd()
print(f"\n[+] Directorio actual: {directorio_actual}")

files = os.listdir(directorio_actual)

print(f"\n[+] Lista de archivos en directorio actual:")
for file in files:
    print(file)

if not os.path.exists('directorio_nuevo'):
    print(f"\n[+] Creación de un nuevo directorio")
    files = os.listdir(directorio_actual)
    print(f"\n[+] Lista de archivos en directorio actual:")
    for file in files:
        print(file)

print(f"\n[+] ¿Existe el archivo 'mi-archivo.txt'?")
if os.path.exists('directorio_nuevo/mi-archivo.txt'):
    print(True)
else:
    print(False)
    print("Se crea el fichero mi-archivo.txt")
    os.mkdir('directorio_nuevo/mi-archivo.txt')
    print(f"\n[+] ¿Existe el archivo 'mi-archivo.txt'?: {os.path.exists('directorio_nuevo/mi-archivo.txt')}")

get_env = os.getenv('TERM')
print(f"\n[+] Valor de la variable 'TERM': {get_env}")