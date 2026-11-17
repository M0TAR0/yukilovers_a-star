from grafo import Grafo

MAPA = """
######################################                      ######SSS###### 
#KKKKKKKKKKKKKKKKKKKKK#..............#                      #.............# 
#KKKKKKKKKKKKKKKKKKKKK#.############.#                      #.............# 
#KK################KKK#........G.....#                      #..MM....MMC..# 
#KKKKKKKKKKKKKKKKKKKKK#..............########################..MMC..CMMC..# 
#KKKKKKKKKKKKKKKKKKKKK#......W..............................#.............# 
#KKKKKKKKKKKKKKKKKKKKK............................C.........#.G...........# 
#KK####KKKK####KKKKKKK....MMC.....MM......MM.....CMM........#.......F.....# 
#KK####KKKK####KKKKKKK#...MM......MM......MM.....CMMC.......#.............# 
#KKKKKKKKKKKKKKKKKKKKK#....C................................#.............# 
#KKKKKKKKKKKKKKKKKWKKK#.......................................CMM....MMC..# 
#KKKKKKKKKKKKKKKKKKKKK#.....F.................................CMM....MM...# 
#KKKKKKKKKKKKKKKKKKKKK#...............L...................................# 
#########...###########.....................................#.....P.......# 
#...................#.......................................#...F.........# 
#...................#....CMM......MM.....CMMC.....MM........#.............# 
#..............CC...#.....MM......MM......MM......MM........#.............# 
#........MM....MM...#......................C................#..MM....MMC..# 
#........MM....MM...#.......................................#..MM....MMC..# 
#...............C...#...........P...........................#......W......# 
######..............#........................F..............#.............# 
     #......W.......#.......................................#.....L.......# 
     #.......F......#.............................C.......................# 
     #..............#....CMM.....CMM.....CMM.....CMMC.....................# 
     #...C...............CMMC....CMMC.....MM......MM........#.CMM.........# 
     #...MM....MM..........C.......C...............C........#.CMMC........# 
     #...MM....MM.......................F...................#.............# 
     #...CC....CC...#..........................W............#.........##### 
     S..............#................................L................#     
     S..........L...#.................................................#     
     #..............#.....C...............C.......C...................#     
     #.........CC...#....CMM.....CMM.....CMMC....CMM..................#     
     #...MM....MM...#....CMM......MM.....CMM.....CMMC.................#     
     #...MM....MM...#......C..........................................S     
     #...CC.....C...#....................W............................S     
     #..............#.................................................#     
     #..............#...L.............................................#     
######................................................................#     
############...#####################....#################...###########     
#................G...........................#................###.....#     
#..........C.............C...................#.......####.....###.....#     
#..CMMMC..CMMMC...MMM...CMMM.....C...........#.......####.............#     
#...MMM....MMM....MMM....MMM....CMMC...MMC...#........................##### 
#.....C......C.............C.....MM....MM....###############################
#.......W...............................C....#............................# 
#.................F....P.....................#...C....W.C.................# 
#............................................#..CMMMC...MMMC..CMMMC.......# 
#..CMMMC...MMMC..CMMMC...MMM.................#...MMM....MMM....MMM........# 
#...MMM....MMM....MMM....MMM...F.............#....LC......................S 
#.....C.............C......C.................#............................S 
#......L...................#######EEEE########...C.............C..........# 
#..........................#                ##...MMMC...MMMC..CMMMC.......# 
#..........................#                ##...MMM....MMM....MMM........# 
#..........................#                ##............P......C........# 
########SSS#################                ############################### 
"""

# Simbología del plano
#   #  Pared                      .  Camino
#   K  Cocina                     E  Entrada
#   S  Salida de emergencia       M  Mesa
#   C  Comensal                   F  Comida tirada en el piso
#   L  Loza rota                  P  Mascota
#   W  Mesero                     G  Gerente
#      (espacio) Exterior del restaurante

# Costo de entrar a cada tipo de celda transitable
COSTO_CELDA = {".": 1, "K": 1, "E": 1, "S": 1, "F": 3, "L": 5}

NOMBRE_GRUPO = {
    "M": "MESA",
    "C": "COMENSAL",
    "S": "SALIDA_EMERGENCIA",
    "E": "ENTRADA",
    "F": "COMIDA_PISO",
    "L": "LOZA_ROTA",
    "P": "MASCOTA",
    "W": "MESERO",
    "G": "GERENTE",
}

DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def leer_mapa(texto):
    filas = [f for f in texto.split("\n") if f != ""]
    ancho = max(len(f) for f in filas)
    return [list(f.ljust(ancho)) for f in filas]


def id_celda(f, c):
    return f"{f},{c}"


INDIVIDUALES = {"C", "F", "L", "P", "W", "G"}


def agrupar(celdas, simbolo):
    """Agrupa celdas contiguas del mismo símbolo en un solo elemento (orden de lectura).
    Comensales, comida, loza, mascotas, meseros y gerentes son siempre individuales."""
    alto, ancho = len(celdas), len(celdas[0])
    visto = set()
    grupos = []
    for f in range(alto):
        for c in range(ancho):
            if celdas[f][c] != simbolo or (f, c) in visto:
                continue
            pila = [(f, c)]
            visto.add((f, c))
            grupo = []
            while pila:
                a, b = pila.pop()
                grupo.append((a, b))
                for df, dc in DIRECCIONES:
                    na, nb = a + df, b + dc
                    if (
                        simbolo not in INDIVIDUALES
                        and 0 <= na < alto
                        and 0 <= nb < ancho
                        and (na, nb) not in visto
                        and celdas[na][nb] == simbolo
                    ):
                        visto.add((na, nb))
                        pila.append((na, nb))
            grupos.append(sorted(grupo))
    return grupos


def construir_grafo(texto=MAPA):
    celdas = leer_mapa(texto)
    alto, ancho = len(celdas), len(celdas[0])
    grafo = Grafo()
    posiciones = {}  # nodo -> (fila, columna) para uso en heurísticas
    elementos = {}  # nodo objetivo -> lista de celdas que ocupa

    def transitable(f, c):
        return 0 <= f < alto and 0 <= c < ancho and celdas[f][c] in COSTO_CELDA

    # 1) Nodos de celdas transitables y aristas de movimiento (4 direcciones).
    #    Las aristas son dirigidas: el peso es el costo de ENTRAR a la celda destino.
    for f in range(alto):
        for c in range(ancho):
            if not transitable(f, c):
                continue
            nodo = id_celda(f, c)
            grafo.agregar_nodo(nodo)
            posiciones[nodo] = (f, c)
            for df, dc in DIRECCIONES:
                nf, nc = f + df, c + dc
                if transitable(nf, nc):
                    grafo.agregar_arista(
                        nodo,
                        id_celda(nf, nc),
                        peso=COSTO_CELDA[celdas[nf][nc]],
                        dirigido=True,
                    )

    # 2) Nodos objetivo. Los elementos sobre celdas transitables (E, S, F, L) se
    #    alcanzan desde sus propias celdas; los elementos que son obstáculos
    #    (M, C, P, W, G) se alcanzan desde las celdas transitables adyacentes.
    #    Las aristas hacia un objetivo son dirigidas y de peso 0, para que nunca
    #    se pueda atravesar un objetivo como atajo.
    for simbolo, prefijo in NOMBRE_GRUPO.items():
        grupos = agrupar(celdas, simbolo)
        for i, grupo in enumerate(grupos, start=1):
            nombre = prefijo if simbolo == "E" else f"{prefijo}_{i:02d}"
            grafo.agregar_nodo(nombre)
            elementos[nombre] = grupo
            posiciones[nombre] = (
                sum(p[0] for p in grupo) / len(grupo),
                sum(p[1] for p in grupo) / len(grupo),
            )
            origenes = set()
            for f, c in grupo:
                if transitable(f, c):
                    origenes.add((f, c))
                else:
                    for df, dc in DIRECCIONES:
                        if transitable(f + df, c + dc):
                            origenes.add((f + df, c + dc))
            for f, c in sorted(origenes):
                grafo.agregar_arista(id_celda(f, c), nombre, peso=0, dirigido=True)

    # 3) Nodo objetivo COCINA: alcanzable desde cualquier celda de cocina.
    cocina = [(f, c) for f in range(alto) for c in range(ancho) if celdas[f][c] == "K"]
    grafo.agregar_nodo("COCINA")
    elementos["COCINA"] = cocina
    posiciones["COCINA"] = (
        sum(p[0] for p in cocina) / len(cocina),
        sum(p[1] for p in cocina) / len(cocina),
    )
    for f, c in cocina:
        grafo.agregar_arista(id_celda(f, c), "COCINA", peso=0, dirigido=True)

    return grafo, posiciones, elementos


grafo, POSICIONES, ELEMENTOS = construir_grafo()

if __name__ == "__main__":
    celdas = [n for n in grafo.vertex if "," in n]
    objetivos = [n for n in grafo.vertex if "," not in n]
    aristas = sum(len(v) for v in grafo.vertex.values())
    print(f"Plano: {len(leer_mapa(MAPA))} filas x {len(leer_mapa(MAPA)[0])} columnas")
    print(f"Nodos de celda transitables: {len(celdas)}")
    print(f"Nodos objetivo: {len(objetivos)}")
    print(f"Aristas dirigidas: {aristas}")
    print("Objetivos:", ", ".join(objetivos))
    print("Vecinos de la celda 50,35 (entrada):", grafo.obtener_vecinos("50,35"))
