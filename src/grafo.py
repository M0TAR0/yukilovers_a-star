class Grafo:
    def __init__(self) -> None:
        self.vertex = {}

    def agregar_nodo(self, nodo: str):
        if nodo in self.vertex:
            return

        self.vertex.update({nodo: []})

    def agregar_arista(self, v: str, destino: str, peso=1, dirigido=False):
        self.agregar_nodo(v)
        self.agregar_nodo(destino)

        self.vertex[v].append((destino, peso))

        if dirigido:
            return

        self.vertex[destino].append((v, peso))

    def obtener_vecinos(self, nodo: str):
        return self.vertex.get(nodo, [])

    def mostrar_grafo(self):
        print(self.vertex)
