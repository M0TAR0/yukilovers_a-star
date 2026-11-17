import heapq

from dijkstra import reconstruir_camino
from mapa_restaurante import ELEMENTOS, POSICIONES


def heuristica(nodo, meta):
    """Distancia Manhattan a la celda más cercana de la meta, menos 1
    (a las mesas, comensales, etc. se llega desde una celda vecina)."""

    if "," not in nodo:
        return 0
    f, c = POSICIONES[nodo]
    return max(0, min(abs(f - mf) + abs(c - mc) for mf, mc in ELEMENTOS[meta]) - 1)


def a_estrella(grafo, inicio, meta):
    """Cada vez que se pide un paso (next) expande un nodo y entrega:
    (valor f de cada nodo visto, nodos cerrados, camino o None)."""
    g = {inicio: 0}
    f = {inicio: heuristica(inicio, meta)}  # f = g + h
    padre = {}
    abiertos = [(f[inicio], inicio)]
    cerrados = set()

    while abiertos:
        _, actual = heapq.heappop(abiertos)
        if actual in cerrados:  # entrada vieja, ya se cerró por un camino mejor
            continue
        cerrados.add(actual)

        if actual == meta:
            yield f, cerrados, reconstruir_camino(padre, meta)
            return

        for vecino, peso in grafo.obtener_vecinos(actual):
            nuevo_g = g[actual] + peso
            if nuevo_g < g.get(vecino, float("inf")):
                g[vecino] = nuevo_g
                f[vecino] = nuevo_g + heuristica(vecino, meta)
                padre[vecino] = actual
                heapq.heappush(abiertos, (f[vecino], vecino))

        yield f, cerrados, None
