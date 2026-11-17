import time

from a_estrella import a_estrella
from dijkstra import dijkstra
from mapa_restaurante import ELEMENTOS, grafo, id_celda

inicio = id_celda(*ELEMENTOS["ENTRADA"][0])


def promedios(algoritmo):
    costos, nodos, tiempos = [], [], []
    for meta in ELEMENTOS:
        t0 = time.perf_counter()
        for valores, cerrados, camino in algoritmo(grafo, inicio, meta):
            pass
        if camino is None:  # meta inalcanzable
            continue
        tiempos.append((time.perf_counter() - t0) * 1000)
        costos.append(valores[meta])
        nodos.append(len(cerrados))
    return [sum(x) / len(x) for x in (costos, nodos, tiempos)]


print("Inicio:", inicio, " Metas:", len(ELEMENTOS))
print(f"{'':10}{'Costo':>10}{'Nodos':>10}{'Tiempo (ms)':>13}")
for nombre, algoritmo in (("Dijkstra", dijkstra), ("A*", a_estrella)):
    costo, nodos, tiempo = promedios(algoritmo)
    print(f"{nombre:10}{costo:>10.2f}{nodos:>10.2f}{tiempo:>13.3f}")
