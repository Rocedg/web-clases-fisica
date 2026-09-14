# T6 — Momento lineal, impulso y choques: background editorial

## Fuente, alcance y criterio

Fuente revisada: **T6-Momento-lineal.pdf**, 10 páginas físicas, IES La Magdalena. Pp. 1–3: momento, impulso y conservación; pp. 4–6: choques con restitución; pp. 7–10 repiten la introducción y amplían fórmulas y tablas.

Objetivo: elegir el sistema y el intervalo de interacción, conservar momento cuando corresponde y añadir la condición física necesaria para determinar el choque. Fusionar las dos secciones de colisiones. Evitar un catálogo de fórmulas por combinación de masas.

## Índice de la lección

**Bloque 1 — Momento lineal e impulso**
- 1.1. Cantidad de movimiento y fuerza.
- 1.2. Impulso: área bajo F(t).

**Bloque 2 — Conservación en un sistema**
- 2.1. Fuerzas internas e impulso externo.
- 2.2. Separaciones y cuerpos que quedan unidos.

**Bloque 3 — Resolver e interpretar choques**
- 3.1. Choques elásticos, inelásticos y restitución.
- 3.2. Ecuaciones con signo y comprobación energética.
- 3.3. Comparar masas y condiciones del choque.

No crear otro bloque de ampliación o de casos especiales. La comparación final cabe en una tabla breve dentro de 3.3.

## Desarrollo conceptual que debe quedar escrito

p⃗ = mv⃗ es vectorial; unidades kg·m/s. Para masa constante Δp⃗ = mΔv⃗. ΣF⃗ = dp⃗/dt e I⃗ = ∫ΣF⃗ dt = Δp⃗. Para fuerza constante, I⃗ = ΣF⃗ Δt; para fuerza variable puede usarse su media en el intervalo. No confundir fuerza instantánea con Δp/Δt, que es media. N·s equivale a kg·m/s.

El momento total P⃗ = Σp⃗ depende del sistema elegido. ΔP⃗ = I⃗_ext. Se conserva si el impulso externo es cero; durante choques breves puede aproximarse como constante cuando el impulso externo es despreciable en la escala relevante. La presencia de fuerzas internas no demuestra por sí sola que las externas sean nulas. Elegir velocidades inmediatamente antes y después, no varios segundos después de que el rozamiento haya actuado.

En 1D fijar +x a la derecha, u1 y u2 antes, v1 y v2 después. Distinguir rapidez y velocidad con signo. Conservación: m1u1 + m2u2 = m1v1 + m2v2. Esta sola ecuación no determina dos velocidades desconocidas.

Para un choque frontal con cuerpo 1 inicialmente a la izquierda y acercándose al 2, u1 > u2: e = (v2−v1)/(u1−u2). La separación posterior requiere v2 ≥ v1. Introducir e como condición empírica en la dirección del impacto. Para los modelos pasivos aquí tratados: e = 1, elástico; 0 < e < 1, inelástico; e = 0, perfectamente inelástico en la dirección considerada. No llamar «inelástico» únicamente al caso e = 0 ni afirmar que todo choque conserva K.

En el ejemplo de plastilina los cuerpos quedan unidos por el enunciado. e = 0 significa igual velocidad inmediatamente después en 1D, pero no demuestra por sí solo adhesión permanente para cualquier contacto. La energía total se conserva incluyendo deformación, energía interna y sonido; K puede disminuir. No usar e² como fracción universal de K total conservada en cualquier referencia.

## Ejemplos seleccionados y resultados de control

### A. Mismo impulso, distinta fuerza — ejemplo propio guiado

Pelota de 0,200 kg con u = −10,0 m/s que termina con v = +5,00 m/s. Fuerza horizontal neta durante contacto. Δp = m(v−u) = +3,00 N·s. Si Δt = 0,0200 s, F_med = +150 N; si Δt = 0,100 s, +30,0 N.

Dibujar dos pulsos triangulares F(t), ambos con área 3,00 N·s: bases 0,0200 y 0,100 s; alturas 300 y 60,0 N, respectivamente. Aclarar diferencia entre máximo y media. Interpretar: prolongar el contacto reduce la fuerza media para el mismo cambio de momento; no implica una reducción del impulso. Variación: detenerla sin rebote requiere +2,00 N·s.

Conservar el ejemplo original F = 5 N sobre 3 kg durante 3 s desde reposo solo como comprobación en una línea: I = 15 N·s y v = 5 m/s. No dedicarle una página.

### B. Plastilina y bloque — guiado adaptado, p. 3

Plastilina de 0,250 kg a +10,0 m/s contra bloque de 0,500 kg en reposo. Quedan unidos sobre mesa horizontal. Despreciar impulso externo horizontal durante el choque.

P_i = 2,50 kg·m/s; v = 2,50/0,750 = +3,33 m/s. K_i = 12,5 J; K_f = 4,17 J; disminución de K = 8,33 J. No imponer K_i = K_f.

Variación propia por etapas: después del choque deslizan sobre mesa con μ_k = 0,20, g = 10 m/s². La aceleración posterior es −2,00 m/s² y recorren 2,78 m hasta parar. El momento se conserva aproximadamente durante el impacto, pero no durante todo el frenado. Este caso conecta con T4 y T5 sin repetir su teoría.

### C. Separación desde reposo y referencia de la velocidad — adaptación de p. 3

Sustituir el monopatín de 3 kg por dos patinadores de 60,0 y 40,0 kg inicialmente juntos y en reposo sobre hielo ideal. Tras empujarse, el de 60 kg lleva +2,00 m/s respecto al suelo. El otro: v2 = −(60·2)/40 = −3,00 m/s. Impulsos individuales +120 y −120 N·s; momento total cero, pero K_f = 300 J, procedente de energía interna de los patinadores.

Variación: si «2,00 m/s» fuera la velocidad relativa entre ambos después de separarse, plantear v1−v2 = 2 y 60v1+40v2 = 0 → v1 = +0,800 m/s, v2 = −1,20 m/s. Sirve para exigir que se lea respecto a qué se mide la velocidad.

El resultado −20 m/s del monopatín original solo corresponde a +1 m/s del patinador respecto al suelo y al modelo ideal especificado; no reproducirlo sin explicitar la referencia.

### D. Masas distintas y restitución — guiado adaptado, p. 6

m1 = 0,500 kg, u1 = +4,00 m/s; m2 = 0,300 kg, u2 = −6,00 m/s; e = 0,40. Choque frontal con impulso externo despreciable.

0,500v1 + 0,300v2 = 0,200; v2−v1 = 0,40[4−(−6)] = 4,00 m/s. Solución: v1 = −1,25 m/s, v2 = +2,75 m/s. Control: P_f = −0,625 + 0,825 = 0,200 kg·m/s. K_i = 9,40 J; K_f = 1,525 J (1,53 J a tres cifras); pérdida = 7,875 J (7,88 J).

Predicción inicial: no basta la masa mayor para decidir el sentido final. Interpretación: ambos invierten el sentido; se separan a rapidez relativa 4 m/s. Variación: si quedan unidos (e = 0), v = +0,250 m/s y K_f = 0,0250 J. No calcular por separado masas con «conservación de su momento» individual.

### E. El mismo choque con diferente restitución — tabla breve adaptada, pp. 8–10

m1 = m2 = 1,00 kg, u1 = +10,0 m/s, u2 = +6,00 m/s. El cuerpo 1 está detrás y alcanza al 2. En los tres casos P = 16,0 kg·m/s y K_i = 68,0 J.

| e | v1 (m/s) | v2 (m/s) | K_f (J) | Pérdida de K (J) |
|---|---:|---:|---:|---:|
| 0 | 8,00 | 8,00 | 64,0 | 4,00 |
| 0,50 | 7,00 | 9,00 | 65,0 | 3,00 |
| 1 | 6,00 | 10,0 | 68,0 | 0 |

Preguntar qué permanece igual y qué cambia. Para masas iguales y choque elástico intercambian velocidades; no generalizar a masas distintas. Con m1 = 1,00 kg, m2 = 4,00 kg y las mismas velocidades iniciales, e = 1 da v1 = 3,60 m/s y v2 = 7,60 m/s; no se intercambian.

### Prueba tú — detectar una solución imposible (propuesta propia)

«Dos masas de 1,00 kg llegan con u1 = +4,00 m/s y u2 = 0. Se propone v1 = −1,00 m/s y v2 = +5,00 m/s para un choque pasivo. ¿Conservar momento basta para aceptar la solución? Calcula P, K y e». Respuesta: P = 4,00 kg·m/s antes y después, pero K pasa de 8,00 a 13,0 J y e = 1,50. No corresponde al modelo pasivo sin liberación de energía interna; haría falta otra fuente energética. No decir que e > 1 es imposible en toda situación física.

## Fórmulas generales: reserva editorial

Priorizar resolver las dos ecuaciones. Si se incluye una fórmula de consulta, una sola pareja basta:

v1 = [m1u1+m2u2−m2 e(u1−u2)]/(m1+m2).
v2 = [m1u1+m2u2+m1 e(u1−u2)]/(m1+m2).

No repetir derivaciones para e = 0, e = 1, masas iguales y masas en proporción k: la tabla y los casos anteriores cubren la comparación. No introducir choques 2D, centro de masas o cohetes como nuevos bloques.

## Diagramas y correcciones del original

- Paneles antes/después con identidad y color de cada cuerpo estables. Las flechas salen de velocidades con signo; longitud proporcional al módulo dentro de cada panel o con escala común declarada. Mostrar la posición que permite el choque, no dos cuerpos que ya se separan antes de impactar.
- Durante contacto, par de fuerzas sobre cuerpos diferentes, mismo módulo y sentidos opuestos. No dibujar el impulso como si fuese una fuerza de valor constante no especificado.
- P. 6, ejemplo de alcance: las etiquetas gráficas intercambian los resultados 5,60 y 7,40 m/s. Para u1 = 8, u2 = 5, masas iguales y e = 0,60, corresponden v1 = 5,60 y v2 = 7,40. Mantener identidades.
- P. 6, masas distintas: el texto menciona 0,60 aunque los datos y las ecuaciones usan 0,40. Usar e = 0,40 de forma consistente.
- Pp. 4 y 7: conservar una sola explicación del impulso externo despreciable. La brevedad del choque no garantiza por sí sola que dicho impulso sea despreciable.
- Evitar llamar «velocidad» al módulo sin aclararlo y «pérdida de energía» a una desaparición de energía total.

## Referencias y procedencia

B, D y E adaptan datos del PDF; C modifica masas y contexto para hacer explícita la referencia; A y «Prueba tú» son propios. El criterio energético se coordina con T5 y con [OpenStax, teorema trabajo–energía](https://openstax.org/books/university-physics-volume-1/pages/7-3-work-energy-theorem). Las ecuaciones de restitución y los casos de 1D se han recalculado desde el material adjunto; no se atribuyen a una consulta externa distinta.

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
