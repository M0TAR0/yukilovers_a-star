import time

from a_estrella import a_estrella
from dijkstra import dijkstra
from mapa_restaurante import ELEMENTOS, grafo, id_celda

inicio = id_celda(*ELEMENTOS["ENTRADA"][0])
meta = "MESA_01"


def ejecutar(algoritmo):
    t0 = time.perf_counter()
    for valores, cerrados, camino in algoritmo(grafo, inicio, meta):
        pass
    tiempo = (time.perf_counter() - t0) * 1000
    return valores[meta], len(cerrados), tiempo


costo_d, nodos_d, tiempo_d = ejecutar(dijkstra)
costo_a, nodos_a, tiempo_a = ejecutar(a_estrella)

print("Inicio:", inicio, " Meta:", meta)
print()
print("Camino")
print("  Dijkstra: óptimo, costo", costo_d)
print("  A*:       óptimo si h es admisible, costo", costo_a)
print()
print("Exploración")
print("  Dijkstra: se expande en todas direcciones, como una onda")
print("  A*:       se orienta hacia la meta")
print()
print("Nodos explorados")
print("  Dijkstra:", nodos_d)
print("  A*:      ", nodos_a)
print()
print("Prioridad")
print("  Dijkstra: g(n)")
print("  A*:       f(n) = g(n) + h(n)")
print()
print("Tiempo de ejecución")
print(f"  Dijkstra: {tiempo_d:.2f} ms")
print(f"  A*:       {tiempo_a:.2f} ms  (calcular h agrega un costo por nodo)")
