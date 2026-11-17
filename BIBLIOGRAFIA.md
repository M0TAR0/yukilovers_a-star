# Bibliografía y referencias

## Fuente primaria

- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. _IEEE Transactions on Systems Science and Cybernetics, 4_(2), 100–107. https://doi.org/10.1109/TSSC.1968.300136
  Es el artículo que introdujo A* (1968) y demuestra su optimalidad. Sirve como fuente primaria para la sección histórica.

## Documentación y notas de curso (inglés)

1. Patel, A. J. (s. f.). _Introduction to the A\* algorithm_. Red Blob Games. https://www.redblobgames.com/pathfinding/a-star/introduction.html
   Introducción al algoritmo; habla de la problemática que resuelve frente a Dijkstra o Greedy y tiene visualizadores interactivos paso a paso.

2. Patel, A. J. (s. f.). _Implementation of A\*_. Red Blob Games. https://www.redblobgames.com/pathfinding/a-star/implementation.html
   Pseudocódigo y código en varios lenguajes; muestra el uso de estructuras de datos vistas en el curso.

3. Patel, A. J. (2026). _Amit's A\* pages_. Stanford University. http://theory.stanford.edu/~amitp/GameProgramming/index.html
   Índice con información sobre otros métodos de búsqueda de caminos, aplicaciones de A* e información técnica adicional. _(Nota del PDF: no se había leído; útil para posibles preguntas.)_

4. University of Illinois Urbana-Champaign. (s. f.). _A\* search_ [Notas de clase, CS 440, otoño 2024]. https://courses.grainger.illinois.edu/cs440/fa2024/lectures/astar.html
   A* es esencialmente UCS (Dijkstra) priorizando por f = g + h. Define qué hace "razonable" a una heurística, la relación entre admisibilidad y subestimar el costo, y la dominancia.

5. Poupart, P. (2026). _Lecture 3: Informed search techniques_ [Diapositivas, CS 486/686]. University of Waterloo. https://cs.uwaterloo.ca/~ppoupart/teaching/cs486-winter26/slides/cs486-lecture3-annotated.pdf
   Definiciones formales de heurística admisible y consistente, condición para que A* sea óptimo y completo, y propiedades de complejidad.

6. University of Toronto. (2020). _Heuristic search (Part 2)_ [Notas de clase, CSC384]. https://www.teach.cs.toronto.edu/~csc384h/winter/Lectures/csc384w20-Lecture03-Heuristic-Search-part2-4pp.pdf
   Demuestra por qué una heurística admisible hace óptimo a A*, y compara heurísticas (fichas mal colocadas contra distancia Manhattan).

7. Cornell University. (2017). _Informed search_ [Notas de clase, CS 4700]. https://www.cs.cornell.edu/courses/cs4700/2017fa/lectures/pdf/CS4700-04-Search_informed_v2.pdf
   Ejemplo que contrasta Dijkstra (A* con h(n) = 0) contra A* en la ruta de Hannover a Múnich; útil para la comparación pedida.

## Fuentes en español

1. Learn Graph Theory. (2024, 31 de agosto). _Algoritmo A\*_. https://learngraphtheory.org/articles/es/a-star-search-algorithm.html
   Muy clara; explica g(n), h(n) y f(n) y muestra el paso a paso con listas, actualizaciones y aplicaciones.

2. CIBERED. (2026, 5 de febrero). _¿Qué es el algoritmo A\*?_ | Conceptos programación. https://cibered.com/programacion/conceptos/que-es-el-algoritmo-a/
   Información clara y resumida, organizada por puntos; explica la heurística y muestra código en Python.

3. Instituto Tecnológico de Nuevo Laredo. (s. f.). _Algoritmo A\*_ [Apunte académico]. Tecnológico Nacional de México. https://nlaredo.tecnm.mx/takeyas/Apuntes/Inteligencia%20Artificial/Apuntes/tareas_alumnos/A-Star/A-Star(2005-II-B).pdf
   PDF de doce páginas, más formal, que explica el funcionamiento del algoritmo. _(Nota del PDF: no se había leído.)_

## Otros recursos

- DataCamp. _El Algoritmo A\*: Guía completa_. https://www.datacamp.com/es/tutorial/a-star-algorithm
- (Video, sin título en el PDF) https://youtu.be/X-5JMScsZ14
- Medium (SMU CS). _A\* search algorithm_. https://medium.com/smucs/a-search-algorithm-e22721d38b87
- Llama Elitista (canal de YouTube). _¿Por qué este Algoritmo está en tantos Videojuegos? — A\* Explicado_. https://www.youtube.com/watch?v=hQa9JTtq4Ok
  Es el origen del esquema de colores y de la idea de la demo paso a paso (ver `docs/DEMO.md` §7).
- cb3ndev. _Visualizador-Algoritmo-A-Estrella_ (GitHub). https://github.com/cb3ndev/Visualizador-Algoritmo-A-Estrella
  Código y animación con obstáculos.

## Herramientas

- Pygame (pygame-ce). https://pyga.me — usado para la visualización (`src/interfaz.py`).
- Python `heapq` (min-heap). https://docs.python.org/3/library/heapq.html — usado en `dijkstra.py` y `a_estrella.py`.

## Uso de IA

- Para la implementación de la demostración se hizo uso de Claude, el promt se incluye en la documentación y se empleó con el fin de ahorrar tiempo.
- Chat de muestra con Claude (conversación usada para la demostración): https://claude.ai/chat/e0e957c9-04e3-4425-996a-401fd1fca5f6
- La documentación de `README.md`, `docs/` y `BIBLIOGRAFIA.md` se organizó con ayuda de Claude Code a partir de los documentos del equipo (`INSTRUCTIONS.md` §6 permite usar IA verificando lo obtenido).
- Claude Code ayudó a **transcribir al repositorio** (en archivos `.md`) la información de `Predocumentación.pdf` y de la presentación: leyó los PDF, copió el texto casi sin cambios a `docs/TEORIA.md` y demás documentos. Se realizó una revisión sobre la información introducida.
