# T3 — Leyes de Newton: background editorial

## Fuente, alcance y criterio

Fuente revisada: **T3-Leyes-de-Newton.pdf**, 10 páginas físicas, IES La Magdalena. Incluye diagramas de fuerzas, leyes de Newton, planos sin rozamiento, dinámica circular, péndulo cónico y masas enlazadas. Las referencias de página de este documento son las del archivo adjunto, no una futura paginación.

Objetivo: pasar de identificar interacciones a plantear ecuaciones de movimiento. El rozamiento se presenta como interacción, pero su cálculo detallado pertenece a T4. Conserva aquí la introducción a la dinámica circular y el péndulo cónico que ya están en el original; T4 aplicará esas ideas a curvas y peraltes.

## Índice de la lección

**Bloque 1 — De las interacciones a las leyes**
- 1.1. Fuerzas y diagramas de cuerpo libre.
- 1.2. Inercia, resultante y aceleración.
- 1.3. Acción y reacción: dos cuerpos distintos.

**Bloque 2 — Resolver movimientos con fuerzas**
- 2.1. Ejes, componentes y planos inclinados.
- 2.2. Cuerdas, poleas y masas enlazadas.

**Bloque 3 — Fuerzas que cambian la dirección**
- 3.1. Resultante radial y tangencial.
- 3.2. Péndulo cónico.

No añadir un cuarto bloque de método o resumen: integrar el método en el primer ejemplo y cerrar con una comprobación breve.

## Desarrollo conceptual que debe quedar escrito

En un diagrama de cuerpo libre se aísla un objeto y se dibujan las fuerzas que otros cuerpos ejercen sobre él. Identificar agente y receptor: Tierra sobre bloque, mesa sobre bloque, cuerda sobre bloque. Velocidad y aceleración pueden aparecer en un esquema cinemático separado, pero no son fuerzas. La resultante es la suma, no otra fuerza que añadir.

En un sistema de referencia inercial, resultante cero significa velocidad vectorial constante, que puede ser nula. Para masa constante, ΣF⃗ = ma⃗, con 1 N = 1 kg·m/s². Una fuerza aislada no determina por sí sola la aceleración si otras la compensan. Introducir la primera ley como caracterización del marco inercial, no únicamente como una sustitución algebraica en la segunda.

Las fuerzas F⃗(A sobre B) y F⃗(B sobre A) actúan sobre objetos diferentes. Peso y normal de un mismo bloque no son un par de acción y reacción. Para el sistema conjunto pueden cancelarse las fuerzas internas, pero no se borran del diagrama de cada cuerpo.

La normal es perpendicular a la superficie y se calcula con la ecuación correspondiente: no siempre es mg. La tensión apunta a lo largo de la cuerda tirando del objeto. Una cuerda ideal tensa e inextensible y una polea ideal permiten usar la misma tensión y relacionar aceleraciones; declarar estas hipótesis.

Elegir ejes útiles, no necesariamente un eje «siempre paralelo a la velocidad». En círculo: ΣF_radial = mv²/R hacia el centro y ΣF_tangencial = m·dv/dt para el módulo de la velocidad. «Centrípeta» describe la resultante radial, no una interacción adicional. No confundir la normal de contacto N con la componente normal de la aceleración a_n.

## Ejemplos seleccionados y resultados de control

### A. ¿Hace falta fuerza para mantener la velocidad? — microejemplo adaptado, p. 5

Bloque de 0,250 kg sobre mesa lisa. F1 = 3,00 N a la derecha y F2 = 1,00 N a la izquierda. Preguntar dirección y valor de la aceleración; después qué F1 mantiene una velocidad de +1,00 m/s que el bloque ya tiene.

ΣFx = 3 − 1 = 2 N; a = +8,00 m/s². Para mantenerla, F1 = 1,00 N. Esto mantiene la velocidad existente, no hace aparecer instantáneamente una velocidad de 1 m/s desde reposo. Variación: si inicialmente va a la izquierda, la misma resultante positiva primero reduce su rapidez.

### B. Subir y bajar el mismo plano — ejemplo guiado adaptado, pp. 6–7

Plano liso a 20°, lanzamiento hacia arriba a 2,60 m/s desde s = 0. Eje positivo hacia arriba del plano, g = 10 m/s². Pedir tiempo hasta parar, distancia sobre el plano y ganancia de altura.

N = mg cos20°; a_s = −g sin20° = −3,4202 m/s². v = v0 + a_s t; s = v0 t + a_s t²/2. Condición v = 0: t = 0,760 s; s = 0,988 m; h = s sin20° = 0,338 m. Al volver al origen v = −2,60 m/s y t = 1,52 s, si el plano continúa y no hay obstáculos.

Predicción: la aceleración apunta cuesta abajo incluso mientras sube. En el punto superior v = 0, pero a no es cero. Variación: duplicar masa no cambia a ni h bajo estas hipótesis.

Como comprobación breve del ejemplo de descenso original: plano a 30°, salida desde reposo y recorrido de 0,600 m → a = 5,00 m/s², t = 0,490 s, v = 2,45 m/s. No calcular v desde un tiempo prematuramente redondeado a 0,50 s.

### C. Dos masas, dos diagramas — ejemplo guiado adaptado, p. 10

m1 = 0,100 kg sobre mesa lisa y m2 = 0,200 kg colgante. Cuerda y polea ideales. Positivo: m1 hacia la polea y m2 hacia abajo. Parten del reposo.

T = m1 a; m2g − T = m2 a. Por tanto a = m2g/(m1+m2) = 6,67 m/s² y T = 0,667 N. Normal de la mesa N = 1,00 N. Interpretar por qué T < m2g. El modelo vale hasta que una masa toca un tope o la cuerda deja de estar tensa.

Variación con respuesta: si ambas masas son 0,100 kg, a = 5,00 m/s² y T = 0,500 N. No confundir este sistema con dos masas colgantes de una máquina de Atwood.

### D. Péndulo cónico — ejemplo guiado del original, con datos propios

Esfera de 0,200 kg, cuerda de 1,00 m y ángulo de 30° respecto a la vertical; giro horizontal uniforme sin resistencia del aire. Preguntar radio, tensión y rapidez.

R = L sinθ = 0,500 m; T cosθ = mg; T sinθ = mv²/R. T = 2,31 N y v = √(Rg tanθ) = 1,70 m/s. Mostrar que el radio de la órbita no es la longitud de la cuerda. Variación: duplicar masa duplica tensión, pero no la rapidez para L y θ fijos.

### Prueba tú — detectar un diagrama incorrecto (propuesta propia)

«En un bloque en reposo sobre una mesa se dibujan peso, normal y una tercera fuerza llamada resultante. Además, se afirma que peso y normal son acción y reacción. Corrige las dos afirmaciones y nombra el receptor de cada reacción». Respuesta: la resultante es cero y no se añade; reacción al peso: fuerza gravitatoria del bloque sobre Tierra; reacción a la normal: fuerza del bloque sobre mesa.

## Diagramas y correcciones del original

- Dibujar un objeto y su diagrama aislado; componentes discontinuas o más finas, sin sumar simultáneamente vector original y componentes como fuerzas independientes.
- En el plano, peso vertical, N perpendicular y eje s paralelo. Mostrar subida y bajada sin invertir arbitrariamente el eje.
- En el péndulo cónico, distinguir vista lateral y órbita horizontal. Velocidad tangente; resultante horizontal radial; tensión hacia el punto de suspensión.
- P. 1: sustituir «si se ejerce una fuerza modifica su velocidad» por resultante no nula. No presentar la gravedad como la única interacción a distancia que existe.
- P. 5: corregir las apariciones de «velocidad de 1 m/s²» a 1 m/s.
- P. 9: decir rapidez constante, no velocidad vectorial constante.
- P. 10: las tensiones dibujadas sobre las dos masas no son vectores opuestos en el espacio: una es horizontal y otra vertical. Se eliminan al sumar las ecuaciones escalares asociadas al movimiento compatible; no afirmar que los dos vectores se cancelan directamente sobre el sistema de solo las masas. La polea y su soporte redirigen la cuerda.

## Referencias y procedencia

Los casos A–C y la geometría de D proceden del PDF; los datos de D y el ejercicio de revisión son propuestas propias. Se ha contrastado la interpretación de la resultante radial con [OpenStax, fuerza centrípeta](https://openstax.org/books/university-physics-volume-1/pages/6-3-centripetal-force). No atribuir los datos numéricos propios a esa fuente.

## Pautas compartidas de edición y diseño

Este es un background editorial para Codex, no el índice que debe copiarse íntegro al PDF. Solo los apartados del «Índice de la lección» son entradas del índice del alumno. Las notas de producción, los ejemplos y las comprobaciones no crean bloques adicionales.

- Usa **tres bloques didácticos** en esta propuesta. Dentro de cada uno, aproximadamente 2–5 subapartados según necesidad; no impongas simetría ni crees un apartado por fórmula o ejemplo.
- Índice vertical con títulos breves, páginas reales y enlaces internos cuando sea posible. Deja separación entre entradas y más espacio antes de cada bloque. Sin tercer nivel, sin «recorrido visual» y sin repetir «Apartado» en cada fila.
- Conserva el diseño más reciente de T0–T2. Cabecera despejada; título, subtítulo y versión separados; pie «Página X de Y». Una introducción breve por bloque basta: evita repetir objetivo, qué aprenderás y para qué sirve en cada página.
- Texto principal en una columna. Comparaciones o gráfico con explicación pueden compartir fila, alineados arriba. Integra portada e índice con el comienzo del contenido. Elimina saltos forzados y separadores vacíos.
- **Teoría:** blanco y títulos azules. **Ejemplo resuelto:** fondo verde azulado muy claro, banda lateral y etiqueta. **Prueba tú:** fondo ámbar muy claro, banda y etiqueta. Solución separada visualmente del enunciado. El color no será la única señal; comprobar lectura en gris. No teñir páginas completas para forzar una separación entre teoría y práctica.
- Toda la resolución, incluido su dibujo, pertenece a la tarjeta del ejemplo. Usa planteamiento → modelo y ecuaciones → resultado → interpretación; añade predicción y variación breve sin convertir cada paso en una tarjeta distinta.
- Letra orientativa 10,5–11 pt en A4; etiquetas de gráficos al menos 9 pt. Compacta repetición y huecos, no explicaciones esenciales. No se traslada a estos temas el objetivo anterior de 7–8 páginas entre T0 y T1. Extensión según contenido; no obligues a un bloque por página.
- Redibuja con TikZ/PGFPlots u otro mecanismo vectorial ya usado en el repositorio. No copies capturas del original. Todas las flechas, escalas y curvas deben salir de las mismas componentes o funciones que las cuentas.
- Reutiliza las herramientas matemáticas de T0 y la cinemática de T1–T2 sin volver a impartirlas. Los ejemplos deben exigir elegir modelo, interpretar o comparar, no solo sustituir números.
- En ejemplos mecánicos usa g = 10 m/s² como aproximación didáctica declarada, salvo datos experimentales. Guarda precisión intermedia; los controles numéricos de este MD se presentan normalmente con tres cifras significativas. Indica expresamente la precisión solicitada en las preguntas numéricas y las unidades. Para respuestas escritas, especifica «ecuación y justificación de una o dos frases», no un formato de cadena artificial.

## Uso en el repositorio y entrega de la futura lección

Localiza este background y su PDF por contenido en la estructura de intake existente. Lee las instrucciones del repositorio, comprueba Git y conserva trabajo ajeno. No muevas originales ni los marques como revisados fuera del procedimiento establecido. Usa las rutas de fuentes y PDF ya existentes; si no las hay, sigue las convenciones de T0–T2.

El encargo posterior será crear o refinar la lección, compilarla y renderizar todas sus páginas. Comprueba índices, números, diagramas, signos, unidades y soluciones. Recalcula los controles; informa si corriges este MD. Conserva referencias discretas y distingue adaptaciones del original de propuestas propias. No inventes atribuciones ni afirmaciones sobre exámenes.

No modificar backend, base de datos, catálogo de ejercicios interactivos ni seguimiento de progreso. No hacer commit, push ni merge automáticamente. Entregar PDF y fuente editable, extensión final, contenido agrupado, correcciones y verificaciones realmente ejecutadas. Estas instrucciones no autorizan modificar T0–T2.
