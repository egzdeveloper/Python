import numpy as np
from prettytable import PrettyTable

# Sensores
s1 = np.array([3, 6, 8, 1, 4, 7, 9, 2, 5, 3, 8, 6, 9, 1, 7])
s2 = np.array([2, 5, 1, 9, 3, 6, 8, 7, 4, 2, 5, 1, 9, 6, 3])
s3 = np.array([9, 7, 4, 2, 8, 5, 3, 6, 1, 9, 7, 4, 2, 8, 5])

# Clase
clase = np.array([1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1])

# Pesos
pesos_h = np.array([
    [1, -1, 1],       # peso_h0
    [-0.5, 1, -0.5],  # peso_h1
    [0.5, 1, -0.25],  # peso_h2
    [1, -0.5, 1]      # peso_h3
])
peso_y = np.array([-1, -0.5, 1, -0.25])

def relu(x):
    # Aplicación de la función ReLu en la capa oculta
    return np.maximum(x, 0)

def heaviside(x):
    # Aplicación de la función heaviside en la salida
    return np.where(x > 0, 1, 0)

def calcular_capa_oculta(sensores, pesos):
    return relu(np.dot(sensores, pesos.T))

def calcular_salida(h, pesos):
    return np.dot(h, pesos)

def calcular_metricas(salida, clase):
    # Cálculo de la matriz de confusión y las métricas F1
    tp = np.sum((salida == 1) & (clase == 1))
    fp = np.sum((salida == 0) & (clase == 1))
    fn = np.sum((salida == 1) & (clase == 0))
    tn = np.sum((salida == 0) & (clase == 0))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * sensitivity / (precision + sensitivity) if (precision + sensitivity) > 0 else 0

    return tp, fp, fn, tn, precision, sensitivity, f1

# Cálculo de las capas y la salida
sensores = np.stack((s1, s2, s3), axis=1)
h = calcular_capa_oculta(sensores, pesos_h)
y = calcular_salida(h, peso_y)
salida = heaviside(y)

# Calcular métricas
tp, fp, fn, tn, precision, sensitivity, f1 = calcular_metricas(salida, clase)

# Creación de la tabla con todos los datos
table = PrettyTable()
table.add_column("S1", s1)
table.add_column("S2", s2)
table.add_column("S3", s3)
for i in range(h.shape[1]):
    table.add_column(f"H{i}", h[:, i])
table.add_column("Y", y)
table.add_column("Salida", salida)
table.add_column("Clase", clase)


# Representación de los resultados
print(f"\n[+] La tabla de la red neuronal con todas sus salidas es la siguiente:")
print(f"\n{table}\n")
print(f"[+] Los resultados de la matriz de confusión son:")
print(f"\tPositivo verdadero (tp): {tp}")
print(f"\tFalso positivo (fp): {fp}")
print(f"\tFalso negativo (fn): {fn}")
print(f"\tNegativo verdadero (tn): {tn}\n")
print(f"[+] Cálculo de la matriz F1:")
print(f"\tPrecisión: {round(precision, 3)}")
print(f"\tSensibilidad: {round(sensitivity, 3)}")
print(f"\tF1: {round(f1, 3)}\n")




