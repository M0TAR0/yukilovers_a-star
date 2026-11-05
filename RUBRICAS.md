# Rúbricas de Evaluación: Exposición Final

**Curso:** Estructuras de Datos y Algoritmos II (EDA2) · **Profesor:** Daniel Vargas
**Tema asignado:** A\* (camino más corto con heurística)
**Puntaje total:** **10 puntos**

---

## 1. Distribución General

| Modalidad  | Criterio                      | Puntos | Peso      |
| ---------- | ----------------------------- | ------ | --------- |
| Por equipo | Contexto y teoría             | 3      | 30 %      |
| Por equipo | Demo y análisis de resultados | 3      | 30 %      |
| Por equipo | Conclusiones del tema         | 1      | 10 %      |
| Por equipo | Reporte (repositorio)         | 1      | 10 %      |
| Individual | Comunicación                  | 2      | 20 %      |
|            | **Total**                     | **10** | **100 %** |

- **Calificación por equipo:** 8 puntos, igual para todos los integrantes.
- **Calificación individual:** 2 puntos, según la intervención de cada integrante.

---

## 2. Criterios por Equipo (8 pts)

### 2.1 Contexto y teoría (3 pts)

**Evalúa:** investigación, comprensión y explicación del tema.

| Nivel        | Puntos | Descriptor                                                                                                                                                         |
| ------------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Excelente    | 3      | Explica con precisión f(n) = g(n) + h(n), admisibilidad, relación con Dijkstra, BFS y min-heap. Muestra investigación propia y va más allá del material del curso. |
| Bueno        | 2      | Explica correctamente los conceptos principales con imprecisiones menores o poca profundidad en admisibilidad o complejidad.                                       |
| Suficiente   | 1      | Definición superficial; los conceptos se enuncian sin justificarse.                                                                                                |
| Insuficiente | 0      | Teoría ausente, incorrecta o copiada sin comprensión.                                                                                                              |

**Checklist:**

- [ ] Definición del problema de camino más corto.
- [ ] Función f(n) = g(n) + h(n) y significado de cada término.
- [ ] Heurística admisible (y consistente) con ejemplos.
- [ ] Heurísticas comunes: Manhattan, Euclidiana, Chebyshev.
- [ ] Relación con Dijkstra (h = 0), BFS y priority queue.
- [ ] Complejidad temporal y espacial.
- [ ] Aplicaciones reales (videojuegos, robótica, mapas).

### 2.2 Demo y análisis de resultados (3 pts)

**Evalúa:** que la demo funcione y que los resultados se interpreten correctamente.

| Nivel        | Puntos | Descriptor                                                                                                                                                                                      |
| ------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Excelente    | 3      | Demo funcional y reproducible. Compara A\* contra Dijkstra en cuadrícula con obstáculos (nodos explorados y tiempo), con varios escenarios, e interpreta los resultados con argumentos sólidos. |
| Bueno        | 2      | Demo funcional con comparación básica; análisis correcto pero limitado.                                                                                                                         |
| Suficiente   | 1      | Demo funciona parcialmente o sin comparación; resultados descritos sin interpretación.                                                                                                          |
| Insuficiente | 0      | La demo no funciona o no hay análisis.                                                                                                                                                          |

**Checklist:**

- [ ] Implementación en Python correcta y ejecutable.
- [ ] Visualización del camino y de los nodos explorados.
- [ ] Comparación A\* vs. Dijkstra (nodos explorados y tiempo).
- [ ] Más de un escenario (densidad de obstáculos, tamaño, distancia).
- [ ] Tablas o gráficas de resultados.
- [ ] Interpretación: por qué los resultados son los observados.

### 2.3 Conclusiones del tema (1 pt)

**Evalúa:** cuándo conviene usar el algoritmo.

| Nivel    | Puntos | Descriptor                                                                                                 |
| -------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| Completo | 1      | Conclusiones sustentadas en los resultados; indica cuándo conviene y cuándo no usar A\*, con limitaciones. |
| Parcial  | 0.5    | Conclusiones generales sin respaldo en los resultados.                                                     |
| Ausente  | 0      | Sin conclusiones o irrelevantes.                                                                           |

### 2.4 Reporte (1 pt)

**Evalúa:** repositorio completo y documentado.

| Nivel    | Puntos | Descriptor                                                                                         |
| -------- | ------ | -------------------------------------------------------------------------------------------------- |
| Completo | 1      | Repositorio público con todos los elementos requeridos, README claro e instrucciones de ejecución. |
| Parcial  | 0.5    | Falta algún elemento o la documentación es insuficiente.                                           |
| Ausente  | 0      | Repositorio no público, inaccesible o sin contenido requerido.                                     |

**Elementos obligatorios:**

- [ ] Repositorio **público** en GitHub.
- [ ] Nombres y números de cuenta de los integrantes.
- [ ] Contexto y teoría.
- [ ] Demo.
- [ ] Análisis de resultados.
- [ ] Conclusiones.
- [ ] Referencias.

---

## 3. Criterio Individual (2 pts)

### 3.1 Comunicación (2 pts)

**Evalúa:** claridad, presencia y manejo de preguntas durante la intervención de cada integrante.

| Dimensión           | Excelente (2)                                                                      | Regular (1)                                     | Deficiente (0)                             |
| ------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------ |
| Claridad            | Explica con sus propias palabras, estructura lógica, vocabulario técnico correcto. | Se entiende, pero con saltos o lectura parcial. | Lee las diapositivas; explicación confusa. |
| Presencia           | Voz audible, contacto con la audiencia, dominio del escenario.                     | Presencia irregular.                            | Poca proyección, sin contacto visual.      |
| Manejo de preguntas | Responde con seguridad y precisión; admite lo que no sabe.                         | Responde parcialmente.                          | No responde o evade.                       |

---

## 4. Penalizaciones

| Falta                               | Efecto                                                            |
| ----------------------------------- | ----------------------------------------------------------------- |
| Exceder los 30 minutos              | Descuento en el criterio afectado (contexto, demo o conclusiones) |
| Leer los slides                     | Descuento en Comunicación                                         |
| Participación nula de un integrante | 0 en Comunicación individual                                      |
| Repositorio privado o inaccesible   | 0 en Reporte                                                      |
| Demo no funcional                   | Máximo 1 pt en Demo y análisis                                    |
| Sin referencias                     | Descuento en Reporte                                              |

> Las penalizaciones son lineamientos de control interno del equipo; el profesor determina la aplicación final.

---

## 5. Resumen de Calificación

| Componente                    | Máximo | Obtenido |
| ----------------------------- | ------ | -------- |
| Contexto y teoría             | 3      |          |
| Demo y análisis de resultados | 3      |          |
| Conclusiones                  | 1      |          |
| Reporte                       | 1      |          |
| Comunicación (individual)     | 2      |          |
| **Total**                     | **10** |          |
