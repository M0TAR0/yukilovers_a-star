# Contexto y teoría de A*

---

## ¿Cómo surge?

- **Año:** 1968
- **Lugar:** Laboratorio en Stanford Research Institute
- **Autores:** Peter Hart, Nils Nilsson y Bertram Raphael

Fuente primaria: Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). _A formal basis for the heuristic determination of minimum cost paths._ IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107. https://doi.org/10.1109/TSSC.1968.300136 (ver [`../BIBLIOGRAFIA.md`](../BIBLIOGRAFIA.md)).

## ¿Qué es?

Es un algoritmo de búsqueda informada, lo que significa que aprovecha una función heurística para guiar su búsqueda hacia el objetivo.

Encuentra el camino más corto entre un nodo inicial y un nodo objetivo evitando obstáculos y buscando reducir el costo del recorrido.

## Función de evaluación

$$f(n) = g(n) + h(n)$$

- **f(n):** costo total estimado del camino que pasa por el nodo n.
- **g(n):** costo real desde el inicio hasta el nodo n.
- **h(n):** costo estimado desde el nodo n hasta la meta.

## ¿Qué es una heurística?

Es una estimación del costo que falta para llegar desde un nodo hasta el objetivo.

## Propiedades de la heurística

**Heurística admisible:** nunca sobreestima el costo mínimo real que falta para llegar a la meta.

$$h(n) \leq \text{costo mínimo real restante}$$

**Heurística consistente:** cumple la condición de que la estimación actual no sea mayor que el costo de avanzar a un nodo vecino más la estimación desde ese vecino.

## Idea principal

1. Se establece el nodo inicial y la meta.
2. Se calculan los valores g(n), h(n) y f(n).
3. Se selecciona el nodo con menor f(n).
4. Se revisan sus nodos vecinos.
5. Se actualizan los costos cuando se encuentra una ruta mejor.
6. El proceso continúa hasta llegar a la meta o determinar que no existe una ruta.

## Grafo de ejemplo

Aristas (pesos de la diapositiva): S–A = 2, S–B = 1, A–B = 2, A–C = 2, B–C = 2, A–G = 7, C–G = 3, B–G = 8.

```
            A           7
        2
                2
S           2       C       3   G
                2
    1                   8
            B
```

## Funcionamiento de A* (pseudocódigo)

```
a_estrella(cuadricula, inicio, meta)
  lista_abierta ← cola_prioridad()
  lista_abierta.insertar(inicio, 0)
  lista_cerrada ← conjunto_vacio()
  vino_de ← mapa_vacio()

  costo_g ← mapa(por_defecto = ∞)
  costo_g[inicio] ← 0

  while lista_abierta no esté vacía
    actual ← lista_abierta.extraer_minimo()       // O(log V)

    if actual == meta
       return reconstruir_camino(vino_de, actual)

    lista_cerrada.agregar(actual)

    for each (vecino, costo) in vecinos(cuadricula, actual)
      if vecino in lista_cerrada
         continue

      g_tentativo ← costo_g[actual] + costo

      if g_tentativo < costo_g[vecino]
         vino_de[vecino] ← actual
         costo_g[vecino] ← g_tentativo
         costo_f ← g_tentativo + heuristica(vecino, meta)
         lista_abierta.insertar(vecino, costo_f)

  return NO_ENCONTRADO

reconstruir_camino(vino_de, actual)
  camino ← [actual]
  while actual in vino_de
    actual ← vino_de[actual]
    agregar actual al inicio de camino
  return camino
```

---

# Material ampliado (de `Predocumentación.pdf`)

> Texto copiado de la predocumentación; complementa las diapositivas de arriba.

## ¿Qué es una heurística? (ampliado)

No representa necesariamente la distancia exacta, sino una aproximación que ayuda a orientar la búsqueda. Su función es guiar al algoritmo hacia las rutas que parecen más prometedoras.

## ¿Cómo surge A*? (ampliado)

A* surge por ahí de los años 1968, 10 años después que el algoritmo de Dijkstra que diseñó su algoritmo en 1956 pero lo publicó en 1959, consiste en la búsqueda que explora cada camino hasta encontrar el de menor distancia, el algoritmo en sí funciona muy bien pero al explorar cada camino lo vuelve lento y no tan óptimo. En los años 1968 fue cuando en un laboratorio, en el Stanford Research Institute, un grupo de investigadores buscaban crear lo que hoy en día es considerado como el primer robot móvil que fuera capaz de razonar los caminos que visitaba (Shakey), pero aquí entró la limitación de Dijkstra ya que era un algoritmo bastante pesado y que tardaba en soltar un resultado, lo que no era óptimo para un robot, por lo que los investigadores: Peter Hart, Nils Nilsson y Bertram Raphael, desarrollaron el algoritmo de A* que en lugar de hacer una búsqueda amplia ignoraban ciertos caminos y exploraban algunos en concreto con ayuda de la heurística haciendo una fusión entre Dijkstra y la heurística creando la función f(n)=g(n)+h(n).

(En la predocumentación el robot aparece escrito "Sharky"; el nombre correcto es **Shakey**.)

## La función f(n) = g(n) + h(n) (ampliado)

- **g(n):** costo real acumulado desde el nodo origen hasta n.
- **h(n):** estimación heurística del costo de n a la meta.
- **f(n):** costo total estimado del camino que pasa por n. A* siempre expande el nodo con menor f(n).

Por ejemplo, si ya recorrimos una distancia de 20 unidades y estimamos que faltan 10 para llegar a la meta, nuestro costo estimado total es 30.

A* utiliza este valor para comparar los nodos y decidir cuál debe explorar primero. La fórmula es la parte central de A*. El algoritmo suma lo que ya costó llegar al nodo y lo que calcula que falta para llegar a la meta. Así puede comparar las diferentes opciones.

## ¿Cómo funciona?

1. Se crean una lista abierta (cola de prioridad ordenada por f) y una lista cerrada. El nodo inicial entra a la abierta con g = 0.
2. Se saca de la abierta el nodo con menor f(n).
3. Si es la meta, se reconstruye el camino siguiendo a los padres y termina.
4. Si no, se pasa a la cerrada y se generan sus vecinos. Para cada vecino se calcula g = g(n) + costo de moverse, y h y f.
5. Si el vecino es nuevo, o se encontró un g menor que el que tenía, se actualiza su padre y su f y se agrega o reordena en la abierta.
6. Se repite desde el paso 2. Si la abierta se vacía sin llegar a la meta, no hay camino.

## ¿Qué significa que una heurística sea admisible?

Sea h\*(n) el costo real mínimo de n a la meta. Una heurística es **admisible** si h(n) ≤ h\*(n) para todo n: nunca sobreestima el costo y es "optimista". Por definición h(meta) = 0.

**Por qué importa:** si h es admisible, A* encuentra la solución óptima. Si sobreestimara, podría descartar el camino bueno.

## Consistencia (monotonía)

**h(n) ≤ c(n, n') + h(n')** para todo nodo n y vecino n'. Toda heurística consistente es admisible, pero no al revés. En búsqueda sobre grafos se suele pedir consistencia para no reabrir nodos.

## Dominancia

Entre dos heurísticas admisibles, la de valores mayores (más cercana al costo real) expande menos nodos.

## Casos extremos

- Con **h = 0**, A* se convierte en Dijkstra.
- Con **h perfecta**, solo expande el camino óptimo.

## Ejemplo resuelto

Costos de las aristas: S–A = 2, S–B = 1, A–B = 2, A–C = 2, B–C = 2, A–G = 7, C–G = 3, B–G = 8.

El camino óptimo de S a G es S → B → C → G, con costo 1 + 2 + 3 = 6.

El costo real mínimo desde cada nodo hasta G, llamado h\*(n):

| Nodo | h(n) (estimación) | h\*(n) (costo real mínimo) | ¿h(n) ≤ h\*(n)? |
| ---- | ----------------- | -------------------------- | --------------- |
| S    | 6                 | 6                          | Sí              |
| A    | 4                 | 5                          | Sí              |
| B    | 5                 | 5                          | Sí              |
| C    | 3                 | 3                          | Sí              |
| G    | 0                 | 0                          | Sí              |

**Admisible:** h nunca sobreestima el costo real, así que A* encuentra el camino óptimo.

**Consistente:** h(n) ≤ c(n, n') + h(n') en cada arista. Algunos ejemplos pueden ser:

- S → B: 6 ≤ 1 + 5 = 6 ✓
- S → A: 6 ≤ 2 + 4 = 6 ✓
- A → C: 4 ≤ 2 + 3 = 5 ✓
- B → C: 5 ≤ 2 + 3 = 5 ✓
- C → G: 3 ≤ 3 + 0 = 3 ✓

También se cumple en el sentido contrario y en las demás aristas. Por eso, una vez que A* saca un nodo de la lista abierta, ya encontró su mejor costo y no necesita reabrirlo.

**Contraejemplo 1: heurística NO admisible.** Si h(B) = 9, como h\*(B) = 5, se sobreestima. A* descarta B por parecer muy caro y devuelve S → A → C → G con costo 7, que no es óptimo (el óptimo es 6).

**Contraejemplo 2: admisible pero NO consistente.** Si h(A) = 5 y h(C) = 1, ambas valen menos que su costo real (5 y 3). Pero en la arista A → C: 5 ≤ 2 + 1 = 3 es falso. En este caso A* podría tener que reabrir nodos.

**Relación:** toda heurística consistente es admisible, pero no al revés.

### Valores f con heurística Manhattan

- f(S) = 0 + 6 = 6, f(A) = 2 + 4 = 6, f(B) = 1 + 5 = 6, f(C) = 3 + 3 = 6, f(G) = 6 + 0 = 6.
- Todos empatan en f = 6, así que el orden depende del criterio de desempate. Con desempates favorables, A* expande solo S, B, C y G. Con desempates desfavorables expande los 5 nodos, igual que Dijkstra (S, B, A, C, G).
- Ambos encuentran el mismo camino S → B → C → G con costo 6. En un grafo de 5 nodos la ventaja es mínima. Se nota en mapas grandes, como la cuadrícula con obstáculos de la presentación.

## Heurísticas comunes en cuadrícula

Para un nodo (x, y) y la meta (xg, yg), con dx = |x − xg| y dy = |y − yg|:

- **Manhattan:** dx + dy. Se usa cuando solo se mueve en 4 direcciones (arriba, abajo, izquierda, derecha).
- **Euclidiana:** √(dx² + dy²). Es la distancia en línea recta, para movimiento en cualquier dirección.
- **Chebyshev:** max(dx, dy). Se usa con 8 direcciones (diagonales incluidas) cuando la diagonal cuesta lo mismo que un paso recto.

Coordenadas asumidas para el grafo: S(0,0), B(1,0), A(1,1), C(2,1), G(5,1).

| Nodo | Manhattan | Euclidiana | Chebyshev    | h\* (real) |
| ---- | --------- | ---------- | ------------ | ---------- |
| S    | 5+1=6     | √26 ≈ 5.10 | max(5,1) = 5 | 6          |
| A    | 4+0=4     | 4          | 4            | 5          |
| B    | 4+1=5     | √17 ≈ 4.12 | max(4,1) = 4 | 5          |
| C    | 3+0=3     | 3          | 3            | 3          |
| G    | 0         | 0          | 0            | 0          |

- Las tres son admisibles aquí, porque ninguna supera a h\*. También son consistentes, porque en cada arista la distancia entre sus nodos es menor o igual a su costo.
- Se cumple Manhattan ≥ Euclidiana ≥ Chebyshev. Por dominancia, entre heurísticas admisibles, la de valores mayores expande menos nodos, así que aquí Manhattan es la mejor.
- Ojo: si el movimiento permite diagonales, Manhattan puede sobreestimar y dejar de ser admisible. En ese caso se usa Chebyshev (o Euclidiana).
- Ejemplo: con dx = 4 y dy = 3 salen Manhattan = 7, Euclidiana = 5 y Chebyshev = 4. Es el mismo orden.
- Ejemplos en cuadrícula: distancia Manhattan (movimiento en 4 direcciones), distancia octil o Chebyshev (8 direcciones), distancia euclidiana.

## Comparación con Dijkstra en una cuadrícula con obstáculos

| Aspecto             | Dijkstra                                       | A*                                                             |
| ------------------- | ---------------------------------------------- | -------------------------------------------------------------- |
| Camino              | Óptimo                                         | Óptimo si h es admisible                                       |
| Exploración         | Se expande en todas direcciones, como una onda | Se orienta hacia la meta                                       |
| Nodos explorados    | Muchos                                         | Normalmente muchos menos                                       |
| Prioridad           | g(n)                                           | f(n) = g(n) + h(n)                                             |
| Tiempo de ejecución | Mayor en mapas grandes                         | Menor casi siempre, aunque calcular h agrega un costo por nodo |

## Complejidad

Variables: b = factor de ramificación (vecinos por nodo), d = profundidad de la solución, V = nodos y E = aristas.

- **Tiempo (peor caso):** O(b^d), es decir, exponencial. Con una buena heurística baja mucho en la práctica, porque se expanden menos nodos. Si h = 0, A* se comporta como Dijkstra: O((V + E) log V) con min-heap.
- **Espacio:** O(b^d). Es su mayor desventaja, porque guarda en memoria todos los nodos generados (listas abierta y cerrada). En mapas grandes la memoria se agota antes que el tiempo.
- **Costo por operación:** insertar o sacar de la cola de prioridad cuesta O(log n). Calcular h(n) agrega un costo por cada nodo.
- **Propiedades:** es completo (si existe camino, lo encuentra, con costos positivos) y es óptimo si h es admisible.
- **Comparación:** BFS también es O(b^d) pero ignora los costos, y Dijkstra expande en todas direcciones. A* usa h para expandir menos.
