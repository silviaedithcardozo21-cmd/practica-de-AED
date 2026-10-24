import csv

# Estacion de monitoreo de temperatura ambiente.
# M = 4 sensores; N = 10 lecturas por sensor.
# Los valores base forman curvas de temperatura; el sensor 3 tiene una tendencia
# ascendente mas marcada. Luego se inyectan dos rachas altas conocidas.

M = 4
N = 10

valores_base = {
    1: [22.1, 22.8, 23.4, 24.0, 24.5, 25.1, 24.7, 23.9, 23.2, 22.6],
    2: [21.5, 22.0, 22.6, 23.1, 23.5, 23.0, 22.7, 22.2, 21.8, 21.4],
    3: [20.0, 21.8, 23.9, 25.7, 27.6, 29.8, 31.5, 30.9, 31.1, 31.7],
    4: [24.1, 23.8, 24.4, 24.0, 25.2, 24.8, 25.0, 25.4, 25.1, 24.7]
}

# Inyeccion deliberada de anomalías: valores superiores al umbral de 32 °C.
valores_base[2][2:5] = [33.5, 34.2, 35.1]       # Sensor 2, posiciones 3 a 5
valores_base[3][8:10] = [33.1, 34.0]             # Sensor 3, drift/tendencia; solo 2 lecturas altas
valores_base[4][6:10] = [36.2, 37.0, 35.8, 36.5] # Sensor 4, posiciones 7 a 10

with open("lecturas_sensores.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    for sensor in range(1, M + 1):
        for nro in range(1, N + 1):
            escritor.writerow([sensor, nro, f"{valores_base[sensor][nro-1]:.1f}"])

print("Archivo lecturas_sensores.csv generado correctamente.")
