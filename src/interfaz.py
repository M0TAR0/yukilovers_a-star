import sys

import pygame

from a_estrella import a_estrella
from dijkstra import dijkstra
from mapa_restaurante import ELEMENTOS, MAPA, grafo, id_celda, leer_mapa

# Controles:
#   ESPACIO: un paso   A: automático   D: cambiar algoritmo   R: reiniciar
#   Clic izquierdo: inicio   Clic derecho: meta (mesa, comensal, salida, cocina...)

TAM = 25  # tamaño de cada celda en píxeles
CELDAS = leer_mapa(MAPA)
FILAS, COLUMNAS = len(CELDAS), len(CELDAS[0])

NEGRO, GRIS, ROJO, VERDE = (0, 0, 0), (200, 200, 200), (255, 0, 0), (0, 255, 0)
AMARILLO, AZUL, MORADO = (255, 255, 0), (173, 216, 230), (209, 125, 212)
COLORES = {
    "#": (50, 50, 50),
    " ": (25, 25, 35),
    ".": (245, 245, 245),
    "K": (250, 220, 180),
    "E": (100, 180, 255),
    "S": (60, 200, 120),
    "M": (139, 90, 43),
    "C": (230, 150, 60),
    "F": (200, 170, 0),
    "L": (170, 170, 210),
    "P": (255, 105, 180),
    "W": (60, 90, 200),
    "G": (130, 30, 160),
}

pygame.init()
ventana = pygame.display.set_mode((COLUMNAS * TAM, FILAS * TAM + 30))

# Información de letra:
fuente_numeros = pygame.font.SysFont(None, 14)
fuente_info = pygame.font.SysFont(None, 22)

algoritmo = "A*"
inicio = id_celda(*ELEMENTOS["ENTRADA"][0])
meta = "COCINA"


def objetivo_en(f, c):
    for nombre, celdas in ELEMENTOS.items():
        if (f, c) in celdas:
            return nombre


def reiniciar():
    global busqueda, valores, cerrados, camino, auto
    busqueda = (a_estrella if algoritmo == "A*" else dijkstra)(grafo, inicio, meta)
    valores, cerrados, camino, auto = {}, set(), None, False


def siguiente_paso():
    global valores, cerrados, camino, auto
    try:
        valores, cerrados, camino = next(busqueda)
    except StopIteration:  # ya terminó (o no hay ruta)
        auto = False


def dibujar():
    ventana.fill(NEGRO)
    for f in range(FILAS):
        for c in range(COLUMNAS):
            nodo, celda = id_celda(f, c), pygame.Rect(c * TAM, f * TAM, TAM, TAM)
            color = COLORES[CELDAS[f][c]]
            if camino and nodo in camino:
                color = MORADO
            elif nodo in cerrados:
                color = AZUL
            elif nodo in valores:
                color = AMARILLO
            pygame.draw.rect(ventana, VERDE if nodo == inicio else color, celda)
            pygame.draw.rect(
                ventana, ROJO if (f, c) in ELEMENTOS[meta] else GRIS, celda, 1
            )
            if nodo in valores:
                texto = fuente_numeros.render(str(valores[nodo]), True, NEGRO)
                ventana.blit(texto, texto.get_rect(center=celda.center))

    costo = valores[meta] if camino else "-"
    info = (
        f"{algoritmo} | Meta: {meta} | Costo: {costo} | "
        "ESPACIO paso  A auto  D algoritmo  R reiniciar  Clic izq/der: inicio/meta"
    )
    ventana.blit(fuente_info.render(info, True, GRIS), (8, FILAS * TAM + 8))


reiniciar()
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                siguiente_paso()
            elif evento.key == pygame.K_a:
                auto = not auto
            elif evento.key == pygame.K_d:
                algoritmo = "Dijkstra" if algoritmo == "A*" else "A*"
                reiniciar()
            elif evento.key == pygame.K_r:
                reiniciar()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            f, c = evento.pos[1] // TAM, evento.pos[0] // TAM
            if evento.button == 1 and id_celda(f, c) in grafo.vertex:
                inicio = id_celda(f, c)
                reiniciar()
            elif evento.button == 3 and objetivo_en(f, c):
                meta = objetivo_en(f, c)
                reiniciar()

    if auto:
        siguiente_paso()
    dibujar()
    pygame.display.flip()
    reloj.tick(60)
