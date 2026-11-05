# Instrucciones: Exposición Final

**Curso:** Estructuras de Datos y Algoritmos II (EDA2), semestre 2027-1
**Profesor:** Daniel Vargas Sánchez
**Tema del equipo:** **A\*** (camino más corto con heurística)
**Duración máxima:** **30 minutos**

---

## 1. Objetivo General

Investigar por cuenta propia, trabajar en equipo, aplicar lo aprendido y comunicarlo frente al salón de clases.

---

## 2. Contenido Obligatorio

La exposición debe incluir:

| #   | Sección                    | Descripción                                  |
| --- | -------------------------- | -------------------------------------------- |
| 1   | **Contexto y teoría**      | Fundamentos del tema y relación con el curso |
| 2   | **Demo**                   | Implementación funcional                     |
| 3   | **Análisis de resultados** | Mediciones e interpretación                  |
| 4   | **Conclusiones**           | Cuándo conviene usar el algoritmo            |
| 5   | **Referencias**            | Documentación oficial y bibliografía         |

---

## 3. Tema Asignado: A\*

| Campo                   | Detalle                                                                                                   |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **Concepto**            | Búsqueda de camino más corto con heurística                                                               |
| **Objetivo**            | Mostrar cómo A\* extiende Dijkstra con una estimación de la distancia a la meta para explorar menos nodos |
| **Se relaciona con**    | Dijkstra, priority queue (min-heap) y BFS                                                                 |
| **Lenguaje de la demo** | Python                                                                                                    |

### 3.1 Qué se debe cubrir

- La función **f(n) = g(n) + h(n)** y qué representa cada término:
  - **g(n):** costo real desde el origen hasta n.
  - **h(n):** estimación del costo de n a la meta.
  - **f(n):** costo total estimado del camino que pasa por n.
- Qué significa que una heurística sea **admisible**.
- **Comparación con Dijkstra** en una cuadrícula con obstáculos, midiendo:
  - Nodos explorados.
  - Tiempo de ejecución.
- **Demo en Python.**

### 3.2 Puntos adicionales recomendados

| Aspecto            | Contenido sugerido                                                                   |
| ------------------ | ------------------------------------------------------------------------------------ |
| Heurísticas        | Manhattan, Euclidiana, Chebyshev; cuándo usar cada una                               |
| Consistencia       | Diferencia entre heurística admisible y consistente                                  |
| Casos límite       | h = 0 (equivale a Dijkstra); h sobreestimada (pierde optimalidad)                    |
| Estructuras        | Open set con min-heap, closed set, diccionario de predecesores                       |
| Desempate          | Criterios de desempate cuando f(n) es igual                                          |
| Complejidad        | Tiempo y espacio en el peor caso; dependencia de la calidad de h                     |
| Escenarios         | Variación de densidad de obstáculos, tamaño de la cuadrícula y distancia origen-meta |
| Casos sin solución | Comportamiento cuando la meta es inalcanzable                                        |
| Variantes          | Weighted A\*, IDA\*, Bidirectional A\*, Jump Point Search                            |
| Aplicaciones       | Videojuegos, robótica, navegación GPS, planificación de rutas                        |
| Limitaciones       | Consumo de memoria; rendimiento con heurísticas pobres                               |

---

## 4. Entregables

**Repositorio público en GitHub** que incluya:

- [x] **Nombres y números de cuenta** de los integrantes.
- [ ] **Contexto y teoría.**
- [ ] **Demo** (código ejecutable).
- [ ] **Análisis de resultados.**
- [ ] **Conclusiones.**
- [ ] **Referencias.**

### 4.2 Requisitos del repositorio

| Requisito        | Detalle                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| Visibilidad      | **Público**                                                            |
| README           | Integrantes con número de cuenta, descripción, instalación y ejecución |
| Reproducibilidad | La demo corre con instrucciones documentadas                           |
| Dependencias     | Versiones declaradas en `requirements.txt`                             |
| Commits          | Historial con contribuciones de todos los integrantes                  |
| Referencias      | Formato consistente (autor, título, año, enlace)                       |

---

## 5. Estructura de la Presentación

| Bloque                        | Tiempo          | Contenido                                                          |
| ----------------------------- | --------------- | ------------------------------------------------------------------ |
| Contexto y teoría             | ~5 min          | Problema, f(n) = g(n) + h(n), admisibilidad, relación con Dijkstra |
| Demo y análisis de resultados | 10–15 min       | Ejecución, comparación con Dijkstra, interpretación                |
| Conclusiones                  | ~5 min          | Cuándo conviene A\*, limitaciones                                  |
| Preguntas                     | ~5 min          | Sesión de preguntas y respuestas                                   |
| **Total**                     | **máx. 30 min** |                                                                    |

---

## 6. Lineamientos de la Presentación

| Lineamiento               | Indicación                                                                     |
| ------------------------- | ------------------------------------------------------------------------------ |
| **No leer los slides**    | Explicar las ideas con palabras propias                                        |
| **Cuidar el tiempo**      | 30 minutos máximo                                                              |
| **Ensayar**               | Al menos un ensayo completo en equipo                                          |
| **Preparar presentación** | Organiza ideas y estructura                                                    |
| **Participación**         | Todos los integrantes exponen; la comunicación se evalúa individualmente       |
| **Fuentes**               | Consultar documentación oficial y bibliografía; no confiar ciegamente en la IA |
| **Uso de IA**             | Permitido (ChatGPT, Claude, Copilot) para profundizar, verificando lo obtenido |

---

## 7. Recomendaciones de Calidad

### 7.1 Teoría

- Usar un ejemplo pequeño resuelto paso a paso (cuadrícula de 5×5) con valores g, h y f.
- Incluir una demostración intuitiva de por qué una heurística admisible garantiza optimalidad.
- Presentar diagramas del open set y closed set en cada iteración.

### 7.2 Demo

- Visualizar la cuadrícula, los obstáculos, los nodos explorados y el camino final.
- Ejecutar A\* y Dijkstra sobre **las mismas** instancias.
- Fijar semillas aleatorias para que los resultados sean reproducibles.
- Repetir mediciones de tiempo y reportar el promedio.
- Tener una **grabación o capturas de respaldo** por si falla la ejecución en vivo.
- Verificar que el código corra en un entorno limpio antes de la exposición.

### 7.3 Análisis

- Presentar resultados en **tablas y gráficas** con ejes y unidades rotulados.
- Explicar **por qué** ocurren los resultados, no solo describirlos.
- Cubrir al menos un caso donde A\* ofrezca poca ventaja sobre Dijkstra.

### 7.4 Conclusiones

- Basar cada conclusión en los datos medidos.
- Indicar cuándo usar A\* y cuándo otra alternativa.
- Mencionar limitaciones y posible trabajo futuro.

### 7.5 Comunicación

- Distribuir las secciones de forma equitativa.
- Preparar respuestas a preguntas probables (admisibilidad, consistencia, complejidad, h = 0, heurística sobreestimada).
- Mantener contacto visual y ritmo pausado.
- Reconocer lo que no se sabe en lugar de improvisar.

---

## 8. Cronograma de Preparación

| Etapa | Actividad                                                      |
| ----- | -------------------------------------------------------------- |
| 1     | Investigación y lectura de fuentes                             |
| 2     | Implementación de A\* y Dijkstra                               |
| 3     | Diseño de experimentos y recolección de datos                  |
| 4     | Redacción del análisis y las conclusiones                      |
| 5     | Documentación del repositorio                                  |
| 6     | Elaboración de la presentación                                 |
| 7     | Ensayo general cronometrado                                    |
| 8     | Revisión final del repositorio (público, completo, ejecutable) |

---

## 9. Lista de Verificación Final

- [x] El repositorio es público y accesible.
- [x] Integrantes con número de cuenta en el README.
- [ ] Teoría de A\* completa (f, g, h, admisibilidad).
- [ ] Demo funcional y reproducible.
- [ ] Comparación A\* vs. Dijkstra (nodos explorados y tiempo).
- [ ] Análisis interpretado, con tablas o gráficas.
- [ ] Conclusiones basadas en resultados.
- [ ] Referencias incluidas.
- [ ] Exposición ensayada, dentro de 30 minutos.
- [ ] Todos los integrantes participan.
- [ ] Respaldo de la demo preparado.

---

## 10. Criterios de Evaluación (Resumen)

| Criterio                      | Puntos | Modalidad  |
| ----------------------------- | ------ | ---------- |
| Contexto y teoría             | 3      | Equipo     |
| Demo y análisis de resultados | 3      | Equipo     |
| Conclusiones del tema         | 1      | Equipo     |
| Reporte (repositorio)         | 1      | Equipo     |
| Comunicación                  | 2      | Individual |
| **Total**                     | **10** |            |

Detalle completo en [`RUBRICAS.md`](./RUBRICAS.md).
