import sys

print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"[+] Total de argumentos: {len(sys.argv)}")
print(f"[+] Argumentos: {', '.join(parameter for parameter in sys.argv)}")