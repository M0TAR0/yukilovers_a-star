# Demo: A* vs. Dijkstra en el plano de un restaurante

## 1. Idea de la demo

Ruta más corta para un mesero a mesas, cocina, salidas de emergencia, otras personas: Dijkstra y A*, sobre el mismo plano de un restaurante y las mismas metas

## 2. Archivos

| Archivo                   | Qué contiene                                                      |
| ------------------------- | ----------------------------------------------------------------- |
| `src/grafo.py`            | Clase `Grafo` (lista de adyacencia: `nodo -> [(destino, peso)]`). |
| `src/mapa_restaurante.py` | El plano (`MAPA`), costos por celda y construcción del grafo.     |
| `src/dijkstra.py`         | Dijkstra con min-heap (`heapq`) y `reconstruir_camino`.           |
| `src/a_estrella.py`       | A* con min-heap y heurística Manhattan.                           |
| `src/interfaz.py`         | Visualización con pygame (paso a paso).                           |
| `src/analisis.py`         | Compara A* y Dijkstra en **una** meta (`MESA_01`).                |
| `src/analisis2.py`        | Promedios sobre **todas** las metas alcanzables.                  |

## 3. Simbología del plano

(De `src/mapa_restaurante.py`)

```
#  Pared                      .  Camino
K  Cocina                     E  Entrada
S  Salida de emergencia       M  Mesa
C  Comensal                   F  Comida tirada en el piso
L  Loza rota                  P  Mascota
W  Mesero                     G  Gerente
   (espacio) Exterior del restaurante
```

Costo de entrar a cada tipo de celda transitable: `COSTO_CELDA = {".": 1, "K": 1, "E": 1, "S": 1, "F": 3, "L": 5}`

Es decir: caminar cuesta 1, pisar comida tirada cuesta 3 y pisar loza rota cuesta 5. Paredes, mesas, comensales, mascotas, meseros y gerentes son obstáculos.

## 4. Cómo se construye el grafo

1. Nodos de celdas transitables y aristas de movimiento (4 direcciones). Las aristas son dirigidas: el peso es el costo de ENTRAR a la celda destino.
2. Nodos objetivo. Los elementos sobre celdas transitables (E, S, F, L) se alcanzan desde sus propias celdas; los elementos que son obstáculos (M, C, P, W, G) se alcanzan desde las celdas transitables adyacentes. Las aristas hacia un objetivo son dirigidas y de peso 0, para que nunca se pueda atravesar un objetivo como atajo.
3. Nodo objetivo COCINA: alcanzable desde cualquier celda de cocina.

```
Plano: 55 filas x 76 columnas
Nodos de celda transitables: 3014
Nodos objetivo: 181
Aristas dirigidas: 11593
```

## 5. Implementación de los algoritmos

|                      | Dijkstra (`dijkstra.py`) | A* (`a_estrella.py`)                     |
| -------------------- | ------------------------ | ---------------------------------------- |
| Prioridad en el heap | `nuevo_g`                | `f = nuevo_g + heuristica(vecino, meta)` |
| Open set             | `heapq`                  | `heapq`                                  |
| Closed set           | `set`                    | `set`                                    |
| Predecesores         | dict `padre`             | dict `padre`                             |
| Resto del código     | idéntico                 | idéntico                                 |

### Heurística (`a_estrella.py`)

```python
def heuristica(nodo, meta):
    """Distancia Manhattan a la celda más cercana de la meta, menos 1
    (a las mesas, comensales, etc. se llega desde una celda vecina)."""
```

- Es **Manhattan** porque el movimiento es en 4 direcciones
- Es **admisible**: cada paso cuesta al menos 1, y Manhattan cuenta el mínimo de pasos; el "−1" cubre que a las metas que son obstáculos se llega desde una celda vecina.
- Para los nodos objetivo (los que no tienen coma, como `MESA_04`) devuelve 0.

### Detalles de implementación

- **Entradas viejas en el heap:** `if actual in cerrados: continue` ("entrada vieja, ya se cerró por un camino mejor"). En lugar de actualizar la prioridad de un nodo que ya está en el heap, se inserta otra entrada y se ignora la vieja.
- **Desempate:** el heap guarda tuplas `(f, nodo)`. Si dos nodos tienen la misma f, Python compara el nombre del nodo (texto). No hay un criterio de desempate pensado (por ejemplo, preferir menor h).
- **Sin solución:** si el heap se vacía, el generador termina sin entregar camino (`camino` queda en `None`).

## 7. Origen del código

Video: _Llama Elitista — ¿Por qué este Algoritmo está en tantos Videojuegos? A_ Explicado* — https://www.youtube.com/watch?v=hQa9JTtq4Ok
