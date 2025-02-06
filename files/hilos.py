import threading
import time
import requests

dominios = [
    "https://google.es",
    "https://wikipedia.org",
    "https://yahoo.com",
]

def realizar_peticion(url):
    response = requests.get(url)
    print(f"\tURL [{url}]: {len(response.content)} bytes")

print(f"\n[+] Búsqueda sin hilos")
start_time = time.time()
for url in dominios:
    realizar_peticion(url)
end_time = time.time()
print(f"[+] Tiempo total transcurrido: {round(end_time - start_time, 2)} seconds")

print(f"\n[+] Búsqueda con hilos")
hilos = []
start_time = time.time()
for url in dominios:
    hilo = threading.Thread(target=realizar_peticion, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()
end_time = time.time()
print(f"[+] Tiempo total transcurrido: {round(end_time - start_time, 2)} seconds")