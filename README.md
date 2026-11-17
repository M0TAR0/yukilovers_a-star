# TEMA 3: A* (A estrella)

Estructura de Datos y Algoritmos II <br>
Grupo 01

🧑‍🏫 Profesor: Daniel Vargas Sánchez

**Integrantes:**

| Nombre                        | Número de cuenta |
| ----------------------------- | ---------------- |
| Rodríguez May Diego Antonio   | 323061289        |
| Barrera López Itzel Angélica  | 426058720        |
| Miriam Aydee Fragoso Martinez | 323232119        |
| Ontiveros Mota Romel          | 426057637        |

Fecha de entrega: 17 de noviembre de 2026

<hr>

## Descripción

A* es un algoritmo de búsqueda informada, lo que significa que aprovecha una función heurística para guiar su búsqueda hacia el objetivo. Encuentra el camino más corto entre un nodo inicial y un nodo objetivo evitando obstáculos y buscando reducir el costo del recorrido.

Objetivo del trabajo (de `INSTRUCTIONS.md`): _mostrar cómo A\* extiende Dijkstra con una estimación de la distancia a la meta para explorar menos nodos._

La demo (Python) compara A* y Dijkstra sobre el plano de un restaurante: ruta más corta para un mesero hacia mesas, comensales, la cocina, salidas, etc., con obstáculos y celdas de distinto costo (comida tirada y loza rota).

**f(n) = g(n) + h(n)**

- **g(n):** costo real acumulado desde el nodo origen hasta n.
- **h(n):** estimación heurística del costo de n a la meta.
- **f(n):** costo total estimado del camino que pasa por n.

## Contenido del repositorio

| Archivo                                                            | Contenido                                                                                  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| [`docs/TEORIA.md`](docs/TEORIA.md)                                 | Contexto y teoría: lo de la presentación, más el material ampliado de la predocumentación. |
| [`docs/DEMO.md`](docs/DEMO.md)                                     | Cómo está hecha la demo: plano, grafo, algoritmos, controles.                              |
| [`docs/ANALISIS.md`](docs/ANALISIS.md)                             | Mediciones A* vs. Dijkstra e interpretación.                                               |
| [`BIBLIOGRAFIA.md`](BIBLIOGRAFIA.md)                               | Referencias.                                                                               |
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md), [`RUBRICAS.md`](RUBRICAS.md) | Instrucciones y rúbricas del profesor.                                                     |
| `src/`                                                             | Código de la demo y del análisis.                                                          |

## Resultados (resumen)

Promedio sobre las metas alcanzables desde la entrada (`analisis2.py`; detalle en [`docs/ANALISIS.md`](docs/ANALISIS.md)):

|          | Costo | Nodos explorados | Tiempo (ms) |
| -------- | ----- | ---------------- | ----------- |
| Dijkstra | 40.76 | 1304.67          | 2.117       |
| A*       | 40.76 | 334.71           | 1.430       |

A* encuentra el mismo costo y explora un 74.3 % menos nodos. En algunos casos (como la meta `COCINA`) el costo de calcular h hace que A* tarde más.

## Estructura del código

```
src/
├── grafo.py              # clase Grafo (lista de adyacencia)
├── mapa_restaurante.py   # plano, costos y construcción del grafo
├── dijkstra.py           # Dijkstra con min-heap
├── a_estrella.py         # A* con heurística Manhattan
├── interfaz.py           # visualización (pygame)
├── analisis.py           # comparación en una meta
└── analisis2.py          # promedios sobre todas las metas
```

## Referencias

Ver [`BIBLIOGRAFIA.md`](BIBLIOGRAFIA.md).
