import heapq


def reconstruir_camino(padre, nodo):
    camino = [nodo]
    while nodo in padre:
        nodo = padre[nodo]
        camino.append(nodo)
    return camino[::-1]


def dijkstra(grafo, inicio, meta):
    """Cada vez que se pide un paso (next) expande un nodo y entrega:
    (valor de cada nodo visto, nodos cerrados, camino o None)."""
    g = {inicio: 0}  # costo acumulado desde el inicio
    padre = {}
    abiertos = [(0, inicio)]
    cerrados = set()

    while abiertos:
        _, actual = heapq.heappop(abiertos)
        if actual in cerrados:  # entrada vieja, ya se cerró por un camino mejor
            continue
        cerrados.add(actual)

        if actual == meta:
            yield g, cerrados, reconstruir_camino(padre, meta)
            return

        for vecino, peso in grafo.obtener_vecinos(actual):
            nuevo_g = g[actual] + peso
            if nuevo_g < g.get(vecino, float("inf")):
                g[vecino] = nuevo_g
                padre[vecino] = actual
                heapq.heappush(abiertos, (nuevo_g, vecino))

        yield g, cerrados, None
