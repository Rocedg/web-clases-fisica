# T2 — Background editorial: Movimiento en el plano

Versión 0.2 para revisión docente · Web Clases Rocedg · 8 de septiembre de 2026

## 1. Función de este documento

Este documento acompaña al PDF original y dirige la creación de una lección propia. Especifica contenido, exclusiones, profundidad, orden, ejemplos, correcciones y diagramas para Codex. No es la lección final ni una orden de cambiar la aplicación.

Fuente revisada: `T2-Movimiento-en-el-plano.pdf`, 19 páginas. Las referencias usan el número de página del archivo, empezando en 1; la numeración impresa se reinicia. El material identifica al IES La Magdalena, Avilés, e incluye anotaciones manuscritas.

El «T0 background» exacto no está disponible en esta revisión. La continuidad visual y didáctica se basa provisionalmente en las instrucciones de T0 compartidas en esta conversación, no en una inspección de su PDF final. Ajustar los criterios comunes cuando se aporte esa referencia.

## 2. Intención de la lección

Título propuesto: **T2 — Movimiento en el plano: componer movimientos y entender las curvas**.

Subtítulo: **Tiros y movimiento circular a partir de vectores, componentes y tiempo.**

Idea conductora: «Para describir un movimiento en dos dimensiones, estudiamos cómo cambian sus componentes y cómo cambia la dirección de la velocidad».

Al terminar, el estudiante debe poder:

- Pasar de posición y velocidad vectoriales a sus componentes y viceversa.
- Entender que los movimientos horizontal y vertical comparten el mismo tiempo.
- Resolver un tiro horizontal y un lanzamiento oblicuo con condiciones iniciales claras.
- Distinguir trayectoria y gráficas temporales.
- Entender que puede existir aceleración aunque la rapidez sea constante.
- Relacionar radio, ángulo, velocidad angular, rapidez, periodo y frecuencia.
- Distinguir MCU y MCUA y descomponer la aceleración en tangencial y normal.

Se asumen vectores y trigonometría de T0, y MRU, MRUA, signos y lectura gráfica de T1. Reutilizar estos conocimientos sin volver a impartirlos completos.

## 3. Decisión de alcance y mapa de la fuente

Mantener movimiento circular dentro de T2, porque ocupa siete páginas del original y forma parte sustancial de su contenido. Organizar una sola lección con dos bloques identificables: **A. Composición y tiros** y **B. Movimiento circular**. No eliminar MCUA ni trasladarlo silenciosamente a un nuevo tema.

| Páginas originales | Material | Decisión editorial |
| --- | --- | --- |
| 1 y 7 | Composición de movimientos y nadador | Unificar en una explicación con dibujo, componentes y una única versión vectorial. |
| 1–2 y 8–9 | Tiro horizontal y ejemplo desde 20 m | Unificar teoría y ejemplo. No repetir la solución por cambiar de notación. |
| 3–4 y 9–10 | Tiro oblicuo y saltador | Unificar. Conservar descomposición, máximo, alcance y velocidad en un instante. |
| 5–6 y 11–12 | Lanzamiento desde 12 m, cambio de origen y doble paso por una altura | Conservar como caso que muestra los límites de las fórmulas de igual altura. Simplificar cuentas repetidas. |
| 13 | Aceleraciones tangencial y normal; MCU | Núcleo conceptual obligatorio, con terminología más precisa. |
| 14–15 | Magnitudes angulares y comparación entre radios | Conservar con diagramas grandes y condiciones de comparación explícitas. |
| 16–17 | Ejemplos de MCU | Seleccionar uno completo y una comparación breve; no reproducir todos. |
| 18–19 | MCUA y frenado angular | Conservar una introducción y un ejemplo; corregir erratas y revisar la anotación final. |

La parte por componentes y la parte vectorial no son dos temas diferentes: son dos maneras de escribir el mismo movimiento. Esta unificación es la principal reducción de redundancia.

## 4. Bloque A: contenido obligatorio

### A1. Posición, desplazamiento y velocidad

Introducir r⃗(t) = x(t)î + y(t)ĵ, v⃗(t) = v_x(t)î + v_y(t)ĵ y a⃗(t) = a_x(t)î + a_y(t)ĵ. La derivación y la integración actúan por componentes. Mostrar v⃗ = dr⃗/dt y a⃗ = dv⃗/dt; un recordatorio breve de la integral definida por componentes basta.

Trasladar aquí la explicación de T1 sobre una trayectoria curva: desplazamiento como cuerda entre puntos, distancia como longitud recorrida y velocidad instantánea tangente en el sentido del movimiento. No afirmar que r⃗ y v⃗ son siempre paralelos.

### A2. Composición: cruzar un río

Identificar los marcos de referencia: velocidad del nadador respecto al agua + velocidad del agua respecto a la orilla = velocidad del nadador respecto a la orilla. Dibujar las flechas y después escribir las componentes.

Para este dibujo en planta elegir x a favor de la corriente e y hacia la orilla opuesta; esos ejes no representan altura. Explicar que ambos desplazamientos ocurren durante el mismo intervalo temporal.

Usar el ejemplo del original, página 7: ancho 10 m, corriente 2,0 m/s y velocidad transversal respecto al agua 0,8 m/s. Se obtiene t = 12,5 s y deriva 25 m. No usar el módulo de la velocidad resultante para dividir directamente el ancho del río. Dejar la compensación de corriente y la optimización de trayectorias fuera del núcleo.

### A3. Modelo común de los tiros

Declarar las hipótesis: objeto puntual, sin rozamiento del aire, gravedad constante y suelo de referencia especificado. En estos diagramas, x positiva hacia la derecha e y positiva hacia arriba; g > 0 es el módulo y a⃗ = −gĵ.

Con Δt = t − t₀:

- x = x₀ + v₀xΔt; v_x = v₀x; a_x = 0.
- y = y₀ + v₀yΔt − ½gΔt²; v_y = v₀y − gΔt; a_y = −g.
- r⃗ = r⃗₀ + v⃗₀Δt + ½a⃗Δt²; v⃗ = v⃗₀ + a⃗Δt.

Presentar una tabla compacta de componentes y una sola expresión vectorial equivalente, sin resolver de nuevo el problema entero. Usar t₀ = 0 en los ejemplos.

Mantener g = 10 m/s² como aproximación didáctica declarada en los ejemplos heredados, coherente con T1. Mencionar g ≈ 9,8 m/s² sin mezclar ambos valores dentro de una solución.

### A4. Tiro horizontal

Mostrar v₀y = 0, v_x constante y v_y cada vez más negativa. La velocidad es tangente a la trayectoria y la aceleración siempre vertical hacia abajo.

Conservar el ejemplo desde 20 m a 15 m/s: con g = 10 m/s², t_impacto = 2 s, alcance horizontal 30 m, v⃗_impacto = (15î − 20ĵ) m/s y rapidez 25 m/s. La dirección es aproximadamente 53,1° por debajo de la horizontal.

Dar el método: imponer y = y_suelo → resolver el tiempo válido → calcular x → calcular componentes, módulo y dirección de la velocidad. No llamar «distancia recorrida» al alcance horizontal.

### A5. Tiro oblicuo

Definir θ desde +x: v₀x = v₀ cos θ y v₀y = v₀ sin θ. Reservar α para aceleración angular en el bloque circular.

En el máximo de un tiro oblicuo ascendente, v_y = 0; v_x permanece y la aceleración no desaparece. Para un lanzamiento y aterrizaje a la misma altura, y con las hipótesis del modelo:

- t_vuelo = 2v₀ sin θ/g.
- Alcance horizontal R_h = v₀² sin(2θ)/g.
- Elevación máxima respecto al lanzamiento Δh = v₀² sin²θ/(2g).

Estas fórmulas son consecuencias, no el punto de partida. Indicar que las dos primeras no se aplican sin cambios a alturas distintas. Reservar R para el radio circular y R_h para el alcance, o usar otra notación inequívoca.

Como nota breve, y(x) puede obtenerse eliminando t cuando v₀x ≠ 0. Priorizar su interpretación parabólica sobre el álgebra extensa.

### A6. Alturas distintas, raíces y gráficas

Adaptar el lanzamiento desde 12 m con v₀ = 15 m/s y θ = 30° (páginas 5–6 y 11–12). Mostrar que cambiar el origen cambia y₀ y la coordenada del suelo, pero no el tiempo de impacto. Distinguir la altura máxima sobre el suelo de la elevación sobre el lanzamiento.

Usar la condición y = y_objetivo y discutir las raíces según el intervalo físico. Puede haber dos tiempos positivos para una misma altura, uno de subida y otro de bajada. Eso no significa que el objeto choque dos veces con un mismo balcón: las posiciones horizontales son distintas y habría que comprobar también x.

Integrar la intención de la anotación de la página 4 con gráficos claros: trayectoria y(x), posición horizontal x(t), posición vertical y(t) y velocidades v_x(t), v_y(t). No confundir una curva en el plano espacial con una gráfica de una magnitud frente al tiempo. Preferir paneles grandes y apilados a un esquema 3D difícil de leer.

## 5. Bloque B: contenido obligatorio

### B1. Cambiar dirección también es acelerar

Mostrar velocidades tangentes de igual módulo en dos puntos de una circunferencia y su diferencia vectorial. En MCU la rapidez es constante, pero la velocidad vectorial cambia.

Introducir a⃗ = a_t u⃗_t + a_n u⃗_n: u⃗_t sigue el movimiento; u⃗_n apunta hacia el centro en la circunferencia. Usando u = |v⃗| como rapidez: a_t = du/dt y a_n = u²/R. La componente tangencial puede ser negativa; a_n es un módulo no negativo. En MCU, a_t = 0.

### B2. Magnitudes angulares y MCU

Definir φ, Δφ, ω, R, periodo T y frecuencia f. Explicar el radián con longitud de arco/R y practicar una conversión de rpm a rad/s.

- Δφ = ωΔt y φ = φ₀ + ωΔt para ω constante.
- Longitud de arco recorrido = R|Δφ| si no cambia el sentido; distinguirla del desplazamiento angular con signo.
- Rapidez u = R|ω|.
- T = 1/f; |ω| = 2πf = 2π/T.
- a_n = u²/R = ω²R, hacia el centro.

Puede usarse ω > 0 en los ejemplos introductorios, pero declarar el sentido positivo. Si se escribe v_t = Rω, explicar que v_t es una componente con signo, no el módulo.

Comparar dos puntos con el mismo ω y radios diferentes: u y a_n aumentan con R; la dirección gira al mismo ritmo angular. Comparar después dos trayectorias con la misma rapidez: a_n aumenta al disminuir R. Indicar siempre qué permanece fijo.

### B3. MCUA

Mantener el radio fijo y α constante:

- ω = ω₀ + αΔt.
- φ = φ₀ + ω₀Δt + ½αΔt².
- Componente tangencial según el sentido angular positivo: a_φ = Rα; su módulo es R|α|.
- a_n = ω²R y |a⃗| = √[(Rα)² + (ω²R)²].

La aceleración angular constante no implica un vector aceleración total constante. El movimiento sigue siendo circular: aumentar la rapidez no aumenta por sí solo el radio.

Conservar un frenado angular: ω₀ = 12 rad/s y α = −2,6 rad/s². Detención a aproximadamente 4,62 s; ángulo hasta detenerse ≈ 27,69 rad, unas 4,41 vueltas. Si el objeto permanece parado después, cerrar ahí el tramo de aceleración constante.

## 6. Recorrido y diagramas propuestos

Objetivo orientativo: 13 páginas, con margen de 12–15. No comprimir ambos bloques para imitar las nueve páginas de T0.

| Página orientativa | Contenido | Visual principal |
| --- | --- | --- |
| 1 | Propósito, requisitos e índice con dos bloques | Recorrido de composición, tiro y giro |
| 2 | Vectores en una curva y composición | Trayectoria con desplazamiento y tangente; nadador |
| 3 | Modelo común por componentes | Lanzamiento con ejes y tabla x/y |
| 4 | Tiro horizontal y ejemplo | Trayectoria grande y velocidad de impacto |
| 5 | Tiro oblicuo, máximo y alcance | Parábola con velocidades y gravedad en tres instantes |
| 6 | Lanzamiento desde altura y cambio de origen | Mismo movimiento con dos referencias verticales |
| 7 | Gráficas y dos pasos por una altura | Gráficas temporales y trayectoria con instantes comunes |
| 8 | Aceleración tangencial y normal | Descomposición en un punto de la curva |
| 9 | Radianes, ω, T y f | Radio, arco y ángulo; ejemplo de conversión |
| 10 | MCU y comparación entre radios | Flechas tangentes/normales y dos comparaciones explícitas |
| 11 | Ejemplo guiado de MCU | Disco con dos radios y cantidades calculadas |
| 12 | MCUA y frenado | Circunferencia de radio fijo y gráfica ω(t) |
| 13 | Método y síntesis | Tabla tiros/MCU/MCUA y comprobaciones con respuesta |

Si hay exceso de densidad, separar composición y vectores o MCUA y su ejemplo. Conservar diagramas legibles antes que un número rígido de páginas.

## 7. Ejemplos, contexto y exclusiones

Resolver una sola vez cada tipo: río, tiro horizontal, oblicuo, alturas distintas, MCU y frenado angular. El lanzamiento oblicuo puede usar el saltador del original, pero recalculando con las componentes sin redondear hasta el final. El caso de alturas distintas puede centrarse en condiciones y resultados para no repetir todo el álgebra.

Para MCU, adaptar el ejemplo del disco de la página 16 o usar un microejemplo nuevo declarado como tal: R = 0,20 m y f = 2 Hz → T = 0,5 s, ω = 4π rad/s, u = 0,8π m/s y a_n = 3,2π² m/s².

Tarjetas «Dato» propuestas, breves y sin saturar:

- «En el modelo sin aire, lanzar horizontalmente no cambia el tiempo de caída respecto a soltar desde la misma altura y con velocidad vertical inicial nula.»
- «Los movimientos horizontal y vertical comparten reloj.»
- «Dar una vuelta devuelve al punto inicial: desplazamiento cero, distancia recorrida 2πR.»
- «Dos puntos de un disco rígido giran con la misma velocidad angular, aunque sus rapidez y aceleración centrípeta sean distintas.»

Excluir resistencia del aire, Coriolis, marcos giratorios, fuerza centrífuga, dinámica circular, energía, momentos de inercia, órbitas y ecuaciones diferenciales avanzadas. Se puede mencionar que las fuerzas explicarán después la aceleración, sin abrir ese tema. No crear un banco de ejercicios ni atribuir frecuencias PAU.

## 8. Correcciones obligatorias de la fuente

- Páginas 3 y 10: unificar el tiempo del ejemplo del saltador; aparece una discrepancia 1,05/1,10 s en la versión por componentes. Recalcular con trigonometría sin redondeo prematuro; explicar posibles diferencias con los resultados impresos.
- Página 11: corregir el término 17,5t que aparece en la expresión vectorial con origen en el lanzamiento; debe ser 7,5t − 5t² en la componente vertical para ese ejemplo.
- Páginas 6 y 12: presentar el «balcón» como una altura de referencia si no se da su posición horizontal. Dos cruces de una altura no prueban dos pasos por un punto fijo.
- Página 13: sustituir «velocidad constante» en MCU por «rapidez constante». Aceleración tangencial instantánea se define con derivada; el cociente finito corresponde a un promedio.
- Página 15: a igual ω, el punto exterior no cambia la dirección a mayor ritmo angular. Su aceleración normal es mayor porque también lo es su rapidez.
- Páginas 16–17: revisar unidades en las cadenas de cálculo; no conservar factores de metro en magnitudes angulares ni omitirlos en rapidez.
- Página 18: corregir «circular y uniforme» en el ejemplo con aceleración tangencial distinta de cero. Diferenciar velocidad angular inicial en rad/s de rapidez en m/s.
- Página 19: conservar el signo negativo de α en el frenado. La anotación manuscrita de una espiral con radio creciente no describe MCUA de radio fijo: no incorporarla como explicación de ese movimiento.

Las anotaciones sobre derivadas, integrales, proyecciones y direcciones de aceleración sí aportan intención didáctica. Redibujarlas con precisión; no tratarlas como instrucciones infalibles ni transcribir lo ilegible.

## 9. Diseño, uso y aceptación

Seguir la dirección de T0: una columna vertical, tarjetas anchas, acentos azules, explicaciones breves, fórmulas acompañadas de significado y diagramas grandes en TikZ/PGFPlots. Consultar `docs/design/ui-redesign-reference/Image 22.jpeg` cuando esté disponible en el repositorio. No copiar capturas, logos ni páginas del original; mantener una nota de procedencia del material utilizado.

Usar etiquetas además de color. Dibujar v⃗ tangente y g⃗ vertical en los tiros; en MCU, v⃗ tangente y a⃗ radial. No confundir estas dos aceleraciones. Los puntos de las distintas gráficas deben corresponder a los mismos instantes y al mismo ejemplo.

Este background fija el encargo editorial. El prompt de ejecución deberá concretar rama, rutas y política de publicación; no asumir que la rama piloto de T0 sirve para T2. No ordena commit, push ni merge ni autoriza cambios de aplicación, base de datos o sistema de ejercicios.

Aceptar la lección cuando cubra ambos bloques sin duplicar las versiones vectorial y por componentes, declare los límites de cada fórmula, corrija las erratas anteriores, distinga rapidez y velocidad y haya sido compilada y revisada visualmente página a página. Verificar de forma independiente todos los resultados y la coherencia entre dibujos y ecuaciones. Informar de cualquier contenido omitido o limitación pendiente.

## 10. Ejemplos del original que deben mantenerse

Esta selección concreta la sección 7. Los ejemplos se distribuyen por la lección y se resuelven una sola vez, conectando componentes y notación vectorial. Las cifras de control siguientes usan g = 10 m/s²; conservar precisión intermedia y adaptar el redondeo al contexto.

| Ejemplo y páginas del original | Tratamiento | Resultados de control y razón para conservarlo |
| --- | --- | --- |
| Nadador, página 7 | Breve y obligatorio | t = 12,5 s y deriva 25 m. Enseña referencia, suma vectorial y tiempo común. |
| Tiro horizontal desde 20 m, páginas 2 y 8–9 | Guiado y obligatorio | 2 s; 30 m; velocidad (15, −20) m/s; rapidez 25 m/s. Une tiempo, posición y velocidad de impacto. |
| Saltador a 8,5 m/s y 40°, páginas 3–4 y 10 | Guiado, sin duplicar versiones | Sin redondear componentes: v₀x ≈ 6,511 m/s, v₀y ≈ 5,464 m/s; vuelo ≈ 1,093 s; alcance ≈ 7,115 m; elevación ≈ 1,493 m. Enseña máximo, trayectoria y condiciones de igual altura. |
| Lanzamiento desde 12 m, páginas 5–6 y 11–12 | Mantener como extensión guiada | Impacto ≈ 2,471 s; máximo sobre el suelo 14,8125 m; elevación 2,8125 m. A 2 m sobre el lanzamiento: t ≈ 0,347 y 1,153 s. Enseña cambio de origen y selección física de raíces. |
| Disco con dos puntos, página 16 | Mantener la comparación y condensar el cálculo | Con tiempo medio de cinco vueltas 4,2576 s: T = 0,85152 s y ω ≈ 7,379 rad/s. A 10 cm y 3 cm, rapidez ≈ 0,738 y 0,221 m/s. Enseña qué comparten los puntos de un disco. |
| Frenado angular, página 19 | Guiado y obligatorio | ω₀ = 12 rad/s, α = −2,6 rad/s²: parada ≈ 4,615 s y giro ≈ 4,407 vueltas. Une signo, dominio temporal y ángulo acumulado. |

En el saltador, tratar la trayectoria como la de un punto representativo bajo el modelo balístico. No presentar el alcance calculado como descripción completa de la biomecánica de un salto real. En el ejemplo de la ventana, hablar de dos cruces de una altura, salvo que se especifique además la posición horizontal del obstáculo.

## 11. Ejemplos adicionales para enriquecer la lección

Son propuestas de elaboración propia apoyadas en los conceptos revisados en las referencias externas. No son transcripciones de ejercicios de esas páginas.

### T2-A. ¿Llega antes al suelo el objeto que avanza más rápido?

**Incorporación obligatoria como microejemplo** junto al tiro horizontal, sin abrir otra página de cuentas.

Desde una altura de 5 m se suelta una pelota A y se lanza horizontalmente otra B a 6 m/s, simultáneamente. Ambas tienen velocidad vertical inicial nula. Despreciar el aire y usar g = 10 m/s².

**Predicción:** elegir cuál llega primero y justificarlo antes de calcular.

**Solución:** en ambas y = 5 − 5t², de modo que llegan en 1 s. A cae al pie del lanzamiento; B llega 6 m más lejos. La velocidad de B al llegar es (6, −10) m/s y su rapidez √136 ≈ 11,66 m/s; la de A tiene rapidez 10 m/s.

**Dibujo:** posiciones de las dos pelotas en los mismos instantes, unidas por líneas horizontales discontinuas. La coincidencia es vertical y temporal; sus velocidades totales son diferentes.

**Transferencia:** si duplicamos solo la velocidad horizontal de B, el tiempo no cambia y el alcance pasa a 12 m. El resultado depende de las hipótesis declaradas.

### T2-B. Mismo alcance, vuelos distintos

**Incorporar como comparación breve** después del tiro oblicuo. Si la página queda densa, colocarlo en una página adicional de aplicación.

Dos pelotas se lanzan a 20 m/s desde el suelo, una a 30° y otra a 60°. Aterrizan a la misma altura, sin aire y con g = 10 m/s². ¿Alcanzan el mismo punto? ¿Pasan el mismo tiempo en el aire?

**Resultados:** ambas tienen alcance 20√3 ≈ 34,64 m. Para 30°: vuelo 2 s y altura máxima 5 m. Para 60°: vuelo 2√3 ≈ 3,464 s y altura máxima 15 m.

**Dibujo:** dos parábolas a la misma escala, mismo origen y mismo punto de llegada; marcar máximos e instantes de impacto. No dibujar ambas pelotas llegando simultáneamente.

**Aprendizaje:** un mismo alcance no determina una única trayectoria ni un único tiempo. La comparación entre ángulos complementarios solo se conserva bajo las condiciones indicadas. Como extensión verbal, preguntar qué fórmula habría que revisar si el aterrizaje fuera más bajo; no desarrollar una optimización nueva.

### T2-C. Dos pegatinas en el mismo disco

**Integrar en el ejemplo del disco existente**, como versión alternativa con datos sencillos; no añadir dos soluciones completas equivalentes.

Un disco gira a 60 rpm; una pegatina A está a 5 cm del centro y otra B a 15 cm. Comparar periodo, velocidad angular, rapidez y aceleración normal.

**Predicción:** «¿La pegatina exterior da más vueltas en un segundo?».

**Solución:** f = 1 Hz, T = 1 s y ω = 2π rad/s para ambas. Rapidez: u_A = 0,1π ≈ 0,314 m/s; u_B = 0,3π ≈ 0,942 m/s. Aceleración normal: a_A = 0,2π² ≈ 1,974 m/s²; a_B = 0,6π² ≈ 5,922 m/s².

**Dibujo:** disco con dos radios, velocidades tangentes y aceleraciones hacia el centro. Ambas avanzan el mismo ángulo en el mismo intervalo; B recorre tres veces más arco. No afirmar que la dirección de B gira a mayor ritmo angular.

**Transferencia:** al duplicar las rpm se duplica la rapidez, se reduce el periodo a la mitad y se cuadruplica la aceleración normal. Contrastar brevemente con dos trayectorias de igual rapidez: entonces menor radio implica mayor aceleración normal.

### T2-D. La velocidad apunta por donde se sale

**Reserva conceptual de una tarjeta.** Una bolita recorre una guía circular horizontal y sale por una abertura. Preguntar la dirección de su velocidad en el instante de salida: la tangente, no el radio hacia fuera. Si se añade el movimiento posterior, declarar qué aceleraciones actúan; no dibujar una recta indefinida sin especificar el modelo. Esta tarjeta conecta cinemática y una futura lección de fuerzas sin introducir dinámica circular.

## 12. Recursos de internet, comparación y mejoras concretas

Consulta web realizada el 8 de septiembre de 2026. «Competencia» se interpreta aquí como otros recursos de enseñanza. No es una clasificación comercial ni una evaluación exhaustiva.

| Recurso | Evidencia consultada | Qué incorporamos |
| --- | --- | --- |
| [OpenStax: Projectile Motion](https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion) | Sus objetivos incluyen componentes perpendiculares, alcance, vuelo y aterrizaje a distinta altura. | Mantener ambos casos de altura y hacer explícito qué condiciones permiten usar las fórmulas abreviadas. |
| [PhET: Projectile Motion](https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_en.html) | La simulación publica apartados Intro, Vectors, Drag y Lab. Se verificó el recurso publicado; no se realizó una sesión interactiva de prueba. | Proponer una extensión opcional de predicción y contraste. El PDF debe contener por sí mismo todos los resultados y explicaciones. |
| [Fisicalab: recursos educativos](https://www.fisicalab.com/) | Su presentación anuncia teoría, ejercicios resueltos e interactividades. No se verificaron aquí sus ejercicios individuales de MCU. | Combinar en cada bloque intuición, solución y una variación; evitar que teoría y aplicación queden desconectadas. |

**Extensión opcional con PhET, diseñada para esta lección:** antes de usarla, comprobar que la versión disponible permite configurar los parámetros. Desactivar el aire, fijar gravedad y rapidez, predecir el efecto de cambiar solo el ángulo y registrar alcance, altura y tiempo. Comparar ángulos complementarios con salida y llegada a la misma altura. Si la gravedad configurada no es 10 m/s², recalcular las cifras esperadas. No afirmar que la simulación reprodujo nuestros resultados hasta ejecutar la prueba.

La actividad es un enlace opcional de aprendizaje, no un encargo de integrar la simulación en la app. Mantener accesible la conclusión en el PDF para quien estudie sin conexión.

**Aportación propuesta de nuestra lección:** continuidad T0–T1–T2, comparación de casos casi iguales con resultados distintos, hipótesis junto a las fórmulas y correspondencia explícita entre trayectoria, componentes y gráficas temporales. Estas son decisiones de diseño; no afirmar que los otros recursos no las ofrecen.

**Competencias a practicar:** formular predicciones, mantener constantes las variables de una comparación, elegir referencias, leer representaciones, evaluar raíces, comprobar dimensiones y explicar límites del modelo. No atribuir alineación con un currículo normativo concreto sin revisarlo.

## 13. Instrucción adicional para Codex

Incluye los ejemplos obligatorios anteriores y los microejemplos T2-A y T2-B. Para el disco, elige la versión experimental del original o T2-C según el espacio y el nivel; preserva la comparación entre radios. T2-D y PhET son extensiones opcionales.

Cada ejemplo guiado debe mostrar: predicción → dibujo y datos → hipótesis → ecuaciones → condición física → cálculo → interpretación → pequeña variación con respuesta. Si añades otra referencia de internet, registra la URL y qué carencia cubre. No copiar capturas, soluciones largas ni colecciones de problemas. Identificar qué procede del original, qué está adaptado y qué es elaboración propia; no atribuir los ejemplos nuevos a OpenStax, PhET o Fisicalab.

La ampliación debe aportar comprensión, no más sustituciones repetitivas. Admitir una o dos páginas adicionales si son necesarias para mantener diagramas y soluciones legibles. No crear archivos del sistema de ejercicios ni cambiar la lógica de la aplicación.
