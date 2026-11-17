# Análisis de resultados

## 1. Configuración

- Plano: 55 filas × 76 columnas, 3014 celdas transitables, 181 metas posibles.
- Inicio fijo: la celda de `ENTRADA` (`50,34`).
- Mismo grafo, mismo inicio y misma meta para ambos algoritmos.
- Métricas: costo del camino, nodos explorados (= tamaño del conjunto cerrado al terminar) y tiempo (`time.perf_counter`).

## 2. Resultado en una meta: `MESA_01` (`analisis.py`)

| Métrica                 | Dijkstra | A*   |
| ----------------------- | -------- | ---- |
| Costo del camino óptimo | 74       | 74   |
| Nodos explorados        | 2802     | 971  |
| Tiempo (ms)             | 6.83     | 5.97 |

Costo y nodos son reproducibles. Los tiempos son los de la computadora del equipo (diapositiva "Ejemplo de prueba"); en otra computadora cambiarán, pero A* sale más rápido.

Complejidad (diapositiva): Temporal O[(V+A) log V] · Espacial O(V + A).

## 3. Promedios sobre todas las metas alcanzables (`analisis2.py`)

|          | Costo | Nodos   | Tiempo (ms)   |
| -------- | ----- | ------- | ------------- |
| Dijkstra | 40.76 | 1304.67 | 6.83 (equipo) |
| A\*      | 40.76 | 334.71  | 5.97 (equipo) |

**A\* explora un 74.3 % menos nodos que Dijkstra** (1 − 334.71 / 1304.67 = 0.743).

Datos extra de la misma corrida:

| Dato                                      | Valor                                                                                     |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- |
| Metas totales                             | 181                                                                                       |
| Metas alcanzables desde la entrada        | 156                                                                                       |
| Metas **inalcanzables**                   | 25 (por ejemplo `MESA_36`, `MESA_43`, `COMENSAL_77`, `SALIDA_EMERGENCIA_04`, `MESERO_08`) |
| Metas con el mismo costo en A* y Dijkstra | 156 de 156                                                                                |
| Metas donde A* exploró menos nodos        | 155 de 156 (la excepción es `ENTRADA`, que es el propio inicio: 2 vs 2)                   |
| Metas donde A* fue más lento en tiempo    | 7 de 156                                                                                  |

Las 25 metas inalcanzables son lugares del plano que quedan cerrados por paredes. Los dos algoritmos revisan todo lo que sí pueden alcanzar y se detienen cuando la lista abierta queda vacía. `analisis2.py` las salta (`if camino is None: continue`).

## 4. El caso donde A* ayuda poco: `COCINA`

| Métrica                            | Dijkstra | A*   |
| ---------------------------------- | -------- | ---- |
| Costo del camino                   | 60       | 60   |
| Nodos explorados                   | 2341     | 1073 |
| Tiempo (ms), diapositivas (equipo) | 6.3      | 51   |

Misma tendencia al medirlo yo: 3.74 ms contra 33.50 ms (promedio de 20 corridas). A* explora **menos** nodos y aun así tarda **mucho más**.

## 5. Resumen de interpretación

| Observación                  | Explicación                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| Mismo costo en ambos         | Camino óptimo (Dijkstra) / óptimo si h es admisible (A*).                             |
| A* explora menos nodos       | Dijkstra se expande en todas direcciones, como una onda; A* se orienta hacia la meta. |
| A* a veces tarda igual o más | Calcular h agrega un costo por nodo (`COCINA`).                                       |
