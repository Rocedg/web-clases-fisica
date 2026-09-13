# T4 — Rozamiento, curvas y fuerzas elásticas: background editorial

## Fuente y decisión de alcance

Fuente revisada: **T4-Fuerzas-centrales.pdf**, 13 páginas físicas, IES La Magdalena. El nombre del archivo NO describe todo su contenido: pp. 1–7 tratan rozamiento, curva plana y peralte; pp. 8–10, medida de g con péndulo; pp. 11–13, muelle real. La anotación de la primera página pide profundizar en fuerzas comunes.

Título editorial recomendado: **T4 — Rozamiento y aplicaciones de las fuerzas**; subtítulo «Deslizamiento, curvas y elasticidad». Conservar el identificador T4 y las rutas del proyecto. No renombrar automáticamente slugs o archivos publicados. Si el catálogo exige «Fuerzas centrales», comunicar la discrepancia y usar el subtítulo para aclarar el contenido; no inventar un capítulo de gravitación, órbitas o leyes de Kepler a partir del nombre.

## Índice de la lección

**Bloque 1 — Rozamiento: antes y después de deslizar**
- 1.1. Rozamiento estático y cinético.
- 1.2. Superficies horizontales y planos inclinados.

**Bloque 2 — Tomar una curva**
- 2.1. Curva plana: adherencia y resultante radial.
- 2.2. Peralte: normal inclinada y velocidad de diseño.

**Bloque 3 — Elasticidad y comprobación experimental**
- 3.1. Ley de Hooke y equilibrio de un muelle.
- 3.2. Péndulo y muelle: qué informa una gráfica.

Las dos prácticas son ampliaciones breves dentro de 3.2, no bloques separados. Conservar aquí su objetivo, ecuación, datos útiles y advertencias; no reproducir seis páginas de procedimientos repetidos. El MD retiene los datos para una futura ficha experimental si se solicita.

## Desarrollo conceptual

El rozamiento se opone al deslizamiento relativo o a su tendencia en el contacto, no necesariamente a la velocidad del centro de masas. Para contacto seco ideal: |f_s| ≤ μ_s N; solo en el umbral |f_s| = μ_s N. En deslizamiento, |f_k| = μ_k N en el modelo adoptado. Calcular N y la fuerza necesaria antes de decidir el régimen. Los coeficientes son aproximaciones dependientes del contacto, no constantes universales de cada material.

En una curva plana, N es vertical y el rozamiento estático proporciona la componente radial. No inclinar la normal porque el motorista incline su cuerpo. La reacción total del suelo es N⃗ + f⃗. En peralte, N sí se inclina porque la calzada está inclinada. v_d = √(Rg tanθ) es la velocidad compatible sin rozamiento para R y θ dados, no una «velocidad máxima sin rozamiento».

Introducir Hooke en una dimensión: F_el = −kx, con x deformación respecto a la longitud natural, k en N/m. En equilibrio vertical kΔL = mg. Para oscilaciones alrededor del equilibrio, usar ξ respecto a ese equilibrio: fuerza neta = −kξ. No identificar sin aclaración ξ con la deformación total del muelle vertical. Validez en régimen elástico lineal.

## Ejemplos seleccionados y controles

### A. Una fuerza creciente no siempre mueve el bloque — guiado adaptado, p. 3

m = 0,250 kg, μ_s = 0,50, μ_k = 0,42, mesa horizontal, g = 10 m/s². Desde reposo, comparar F = 1,00 N y F = 2,00 N hacia la derecha.

N = 2,50 N; f_s,max = 1,25 N. Con 1,00 N permanece en reposo y f_s = 1,00 N, no 1,25 N. Con 2,00 N supera el umbral; f_k = 1,05 N y a = (2−1,05)/0,250 = 3,80 m/s². Si esa F actúa durante 3,00 s desde el inicio del deslizamiento, v = 11,4 m/s. Si entonces se reduce a 1,05 N, mantiene esa velocidad mientras siga deslizando.

Variación: retirar la fuerza tras esos 3 s → a = −4,20 m/s² hasta detenerse; tarda otros 2,71 s y recorre 15,5 m. Una vez detenido, no prolongar esa aceleración para hacerlo volver hacia atrás.

### B. ¿Se mueve en la rampa? — guiado adaptado, pp. 4–5

m = 0,300 kg, μ_s = 0,40, μ_k = 0,30. Primero θ = 15°; luego θ = 30°. En ambos casos parte del reposo.

A 15°: mg sinθ = 0,776 N y f_s,max = 1,16 N → queda quieto, f_s = 0,776 N. Umbral θ_c = arctan0,40 = 21,8°. A 30°: componente cuesta abajo 1,50 N, umbral estático 1,04 N → desliza. a = g(sin30°−0,30 cos30°) = 2,40 m/s² cuesta abajo.

Variación conceptual: si se lanza cuesta arriba a 30°, el rozamiento apunta cuesta abajo durante la subida; al parar se comprueba de nuevo el equilibrio estático. No usar la fórmula del descenso durante la subida. El caso θ = θ_c es equilibrio límite en el modelo ideal, no garantía universal de que cualquier vibración cause deslizamiento.

### C. Curva plana y calzada peraltada — comparación guiada adaptada, pp. 6–7

R = 30,0 m, g = 10 m/s². En curva plana sin derrape ni fuerzas aerodinámicas: N = mg, f_s = mv²/R y f_s ≤ μ_s mg. Con μ_s = 0,80, v_max = √(μ_s gR) = 15,5 m/s = 55,8 km/h. Si μ_s baja a 0,50, v_max = 12,2 m/s = 44,1 km/h. Son resultados de un modelo didáctico, no velocidades recomendadas para conducción.

En curva peraltada a 10° sin rozamiento: N cosθ = mg; N sinθ = mv²/R → v_d = 7,27 m/s = 26,2 km/h. Preguntar qué proporciona la fuerza radial en cada caso. Respuesta: rozamiento estático en plana; componente horizontal de N en peraltada.

Si se ilustra un motorista, en régimen estacionario ideal tanφ = v²/(Rg), con φ respecto a la vertical: a 10,0 m/s y R = 30,0 m, φ = 18,4°. Presentarlo como relación de equilibrio de inclinación opcional, sin desarrollar dinámica de rotación. No tratar φ como una fuente extra de fuerza independiente del rozamiento.

### D. Muelle vertical — microejemplo propio que prepara T5

k = 100 N/m, masa colgada 0,200 kg, g = 10 m/s². Equilibrio: ΔL = mg/k = 0,0200 m = 2,00 cm. Si se baja otros 1,00 cm y se suelta: F_el = 3,00 N hacia arriba, peso = 2,00 N hacia abajo; resultante inicial = 1,00 N hacia arriba y a = 5,00 m/s² hacia arriba. Explicar por qué la deformación total es 3 cm y el desplazamiento respecto al equilibrio solo 1 cm.

### Prueba tú — decide el régimen (propuesta propia)

Bloque de 2,00 kg, mesa horizontal, μ_s = 0,40 y μ_k = 0,30. F = 7,00 N hacia la derecha. «Calcula el rozamiento si parte del reposo y si ya está deslizando a la derecha; justifica el modelo en cada caso». Respuesta: desde reposo f_s = 7,00 N a la izquierda, a = 0; deslizando f_k = 6,00 N a la izquierda, a = +0,500 m/s².

## Prácticas del original: conservar de forma breve y rigurosa

**Péndulo, pp. 8–10.** Para oscilaciones pequeñas, T ≈ 2π√(L/g). Medir L desde suspensión hasta centro de la masa y cronometrar varias oscilaciones. T² frente a L tiene pendiente a = 4π²/g, con unidades s²/m. La pendiente publicada a = 4,015 s²/m da g = 9,83 m/s². Este cálculo usa la pendiente publicada, no afirma haber reproducido su ajuste.

Datos originales: L (m) = [0,600; 0,550; 0,500; 0,450; 0,400; 0,350; 0,300; 0,250; 0,200; 0,150]; T (s) = [1,549; 1,490; 1,417; 1,346; 1,263; 1,190; 1,091; 1,011; 0,888; 0,780]. Si se redibuja el ajuste, recalcular y declarar si se fuerza el intercepto a cero. No presentar 20° como frontera exacta de validez. No identificar diferencia frente a 9,80 con incertidumbre experimental.

**Muelle, pp. 11–13.** Presentar T = 2π√(m/k) como modelo ideal proporcionado para interpretar datos, sin desarrollar un capítulo de MAS. Ajuste publicado T² = (0,0117 s²/g)m + 0,0664 s². Convertir pendiente a 11,7 s²/kg: k = 4π²/11,7 = 3,37 N/m. El intercepto puede señalar física omitida o sesgos; por sí solo no demuestra una causa única. Si se adopta T² = (4π²/k)(m+m_ef), m_ef = b/a = 5,68 g. La relación m_ef ≈ m_muelle/3 requiere el modelo de muelle uniforme y se deja como ampliación, no regla universal ni derivación obligatoria.

Datos originales: m (g) = [25,5; 45,9; 56,4; 76,8; 97,2; 106,8]; T (s) = [0,612; 0,772; 0,850; 0,983; 1,097; 1,150]. Calcular T² desde T: la tabla original contiene 0,0966 donde corresponde aproximadamente 0,966 s². No promediar k calculados con un modelo sesgado y llamar al promedio «valor verdadero».

## Correcciones y diagramas obligatorios

- Pp. 1–2: escribir máximo estático explícitamente y distinguir la oposición al deslizamiento relativo. Tratar las leyes de rozamiento como modelo empírico.
- P. 6: rehacer el dibujo del motorista; la normal de carretera horizontal es vertical. No reutilizar los resultados 27,0 y 24,3 m/s del planteamiento incorrecto.
- P. 7: sustituir «velocidad máxima» por velocidad de diseño sin rozamiento. Con rozamiento puede existir un intervalo; no afirmar que el rozamiento siempre apunta cuesta abajo o aumenta la fuerza radial.
- Pp. 9–13: separar referencia, discrepancia e incertidumbre; no inventar barras de error a partir de diferencias o coeficientes de ajuste.
- Mostrar cuerpo libre del bloque y flechas distintas antes y durante deslizamiento. Para curvas, vista superior de trayectoria y sección transversal de fuerzas claramente rotuladas. Para muelles, longitud natural y equilibrio señalados por separado.

## Referencias y procedencia

A–C adaptan casos del PDF con las correcciones indicadas; D y «Prueba tú» son propios. Datos experimentales y ajustes publicados proceden del adjunto. Contraste conceptual: [OpenStax, rozamiento](https://openstax.org/books/university-physics-volume-1/pages/6-2-friction) y [OpenStax, curvas y fuerza centrípeta](https://openstax.org/books/university-physics-volume-1/pages/6-3-centripetal-force). No presentar las prácticas como experimentos realizados en esta revisión.

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
