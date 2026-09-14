# T5 — Energía y trabajo: background editorial

## Fuente, alcance y criterio

Fuente revisada: **T5-Energía-y-trabajo.pdf**, 15 páginas físicas, IES La Magdalena. Pp. 1–6: energía cinética, trabajo y potencia; pp. 7–11: potencial gravitatoria y disipación; pp. 12–15: energía elástica, MAS y caminos alternativos. Las anotaciones añaden la integral del trabajo y el producto escalar: integrarlos correctamente sin repetir el capítulo matemático de T0.

Objetivo: elegir el sistema, identificar intercambios y resolver cambios de rapidez o altura mediante un balance. Mantener trabajo variable e interpretación gráfica, no reducir la lección a W = Fd y «energía inicial = final».

## Índice de la lección

**Bloque 1 — Trabajo, energía cinética y potencia**
- 1.1. Trabajo: producto escalar y área bajo F(x).
- 1.2. Teorema de la energía cinética.
- 1.3. Potencia y ritmo de transferencia.

**Bloque 2 — Energía potencial y conservación**
- 2.1. Gravedad y fuerzas conservativas.
- 2.2. Muelles y energía elástica.

**Bloque 3 — Balances con y sin disipación**
- 3.1. Elegir el sistema y contabilizar transferencias.
- 3.2. Comparar recorridos y combinar etapas.

No añadir bloques independientes de fórmulas, ejercicios o errores frecuentes. Distribuir ejemplos junto a la idea que aplican.

## Desarrollo conceptual que debe quedar escrito

La energía es una magnitud escalar; el trabajo es una forma de transferir energía mediante fuerzas, no una sustancia almacenada en un cuerpo. Para una partícula de masa constante K = mv²/2. En el modelo de partícula, W_total = ΔK. No afirmar que toda fuerza individual cambia necesariamente la rapidez: una fuerza perpendicular al movimiento puede cambiar solo la dirección.

Para fuerza constante W = F⃗·Δr⃗ = FΔr cosθ; para un tramo rectilíneo sin inversión Δr coincide en módulo con la distancia recorrida. En general W = ∫ F⃗·dr⃗. En una dimensión W = ∫[xi,xf] Fx(x) dx: el área es con signo y los ejes son posición y fuerza, no tiempo. Derivación corta: F_x = ma_x y a_x = v·dv/dx permiten integrar F_x dx = mv dv en un tramo donde esta parametrización es válida; basta mostrar la relación con ΔK sin extender el cálculo.

Potencia media P_med = W/Δt e instantánea P = F⃗·v⃗ para una fuerza. Distinguir potencia de entrada y potencia útil; si se usa rendimiento η, P_útil = ηP_entrada. J es energía, W es potencia y kWh es energía; 1 kWh = 3,6 MJ.

Para una fuerza conservativa, W_cons = −ΔU y el trabajo entre dos puntos no depende del camino. U_g = mgh en campo aproximadamente uniforme, con cero elegido; U_el = kx²/2 para muelle ideal, con x respecto a longitud natural. La potencial corresponde a una interacción del sistema. La energía potencial puede tener signo según el cero; solo las diferencias intervienen en el balance.

E_mec = K+U. En los modelos aquí tratados, Δ(K+U) = W_otras, contando solo los trabajos no incorporados mediante potencial. No sumar el trabajo del peso y también −ΔU_g en el mismo balance. Un trabajo conservativo negativo no implica por sí solo que K disminuya si hay otras fuerzas haciendo trabajo.

Al disiparse energía mecánica no desaparece energía total: aumenta energía interna y puede transferirse al entorno. Evitar llamar al calor una energía «contenida» en el cuerpo; calor es transferencia asociada a diferencia de temperatura. En el modelo de bloque sobre superficie fija, el rozamiento cinético constante tiene W_f = −f_k d. No generalizar «todo rozamiento siempre hace trabajo negativo» a cintas móviles o rodadura.

## Ejemplos seleccionados y resultados de control

### A. Empujar hacia abajo o tirar hacia arriba — guiado adaptado, pp. 4–5

m = 1,00 kg, v0 = 3,00 m/s hacia la derecha, desplazamiento horizontal d = 6,00 m, F = 8,00 N a 30° por debajo de la horizontal, μ_k = 0,30 y g = 10 m/s². Pedir trabajo de cada fuerza y rapidez final; primero predecir el efecto de la componente vertical.

N = mg + F sin30° = 14,0 N; f_k = 4,20 N. W_F = Fd cos30° = 41,569 J; W_f = −25,2 J; W_N = W_P = 0. K_i = 4,50 J; K_f = 20,869 J; v_f = 6,46 m/s. No tratar F como completamente horizontal.

Variación: misma fuerza a 30° por encima. N = 6,00 N > 0, f_k = 1,80 N, W_f = −10,8 J, K_f = 35,269 J y v_f = 8,40 m/s. La proyección horizontal de F y su trabajo son iguales, pero cambia la normal y con ella la disipación. Esta comparación sustituye varios ejercicios rutinarios de fuerza constante.

### B. Fuerza variable: más recorrido, menos energía — ejemplo propio guiado

Bloque de 2,00 kg inicialmente en reposo en x = 0 sobre mesa lisa. Fuerza horizontal neta F_x(x) = 6 N − (2 N/m)x, aplicada hasta x = 4,00 m. Preguntar dónde es máxima la rapidez y cuál es al final.

W(0→x) = (6 N)x − (1 N/m)x². En x = 3,00 m la fuerza cambia de signo: W = 9,00 J y v_max = 3,00 m/s. De 3 a 4 m, W = −1,00 J. En 4 m, K = 8,00 J y v = 2,83 m/s. Dibujo: recta F(x), corte en 3 m, áreas +9 J y −1 J. El bloque sigue avanzando tras x = 3 m, aunque frena.

Variación: si la fuerza continúa, el siguiente reposo ocurre en x = 6,00 m; se ha devuelto el trabajo acumulado, pero se ha recorrido distancia no nula. No deducir tiempo usando solo la igualdad energética.

### C. Lanzamiento vertical visto con energía — microejemplo adaptado, p. 9

m = 0,500 kg, v0 = +12,0 m/s desde h = 0; sin aire, g = 10 m/s². K0 = 36,0 J. A h = 5,00 m: U = 25,0 J, K = 11,0 J, rapidez = 6,63 m/s; vy puede ser +6,63 o −6,63 m/s según la etapa. h_max = 7,20 m. Al volver al nivel inicial la rapidez es 12,0 m/s y la velocidad es −12,0 m/s.

Variación: elegir el cero de U dos metros más abajo suma 10,0 J a U y a E_mec en todos los estados, sin alterar h_max ni velocidades.

### D. Caída con resistencia idealizada — comparación adaptada, pp. 10–11

Objeto de 1,00 kg desde reposo a 10,0 m. Comparar sin aire y con fuerza resistente idealizada constante de 2,00 N hacia arriba durante el descenso; g = 10 m/s². A h = 4,00 m ha descendido 6 m: U = 40,0 J; K = 60,0 J sin resistencia y 48,0 J con ella. Al suelo: K = 100 J y v = 14,1 m/s sin resistencia; K = 80,0 J y v = 12,6 m/s con resistencia. Los 20,0 J restantes corresponden a disipación, no a energía destruida.

Indicar que la fuerza resistente constante es una simplificación pedagógica, no una ley general del arrastre del aire. No desarrollar velocidad terminal aquí.

### E. Muelle que lanza hacia una rampa — guiado adaptado, p. 14

Bloque de 0,500 kg inicialmente en reposo contra un muelle horizontal comprimido 0,200 m; k = 100 N/m. No está unido al muelle: lo abandona en su longitud natural y llega a una rampa lisa mediante una transición suave. Todo sin rozamiento, g = 10 m/s². Pedir rapidez al abandonar el muelle y altura máxima respecto al nivel inicial.

U_el,i = 2,00 J; v_salida = √(2U/m) = 2,83 m/s; h_max = U/(mg) = 0,400 m. Comparar rampas de 30° y 60°: misma altura, distancias sobre tramo inclinado de 0,800 y 0,462 m si la rampa recta empieza al nivel de referencia y se desprecia la longitud de transición. Puede omitirse esta geometría idealizada y preguntar solo por igualdad de altura.

Variación independiente: si antes de una rampa a 30° atraviesa 0,500 m horizontales rugosos con μ_k = 0,20, pierde 0,500 J y llega a h_max = 0,300 m. Comprobar que alcanza la rampa antes de usar el balance final.

Conservar como comparación breve del original, p. 13: masa 0,250 kg unida a muelle horizontal k = 500 N/m, compresión 0,200 m. Sin rozamiento pasa por x = 0 a 8,94 m/s; con μ_k = 0,50, suponiendo iniciado el deslizamiento, disipa 0,250 J en ese recorrido y pasa a 8,83 m/s. No desarrollar otra solución larga equivalente.

### F. Potencia — microejemplo adaptado, pp. 5–6

Elevador que sube 50,0 kg a rapidez constante 0,400 m/s: P_útil = mgv = 200 W. Con η = 0,80, entrada = 250 W. Si sube 4,00 m, tarda 10,0 s y consume 2,50 kJ. Es una propuesta propia que sustituye la comparación inconsistente de bombillas.

Si se conserva el coche del original: 1000 kg de reposo a 100 km/h en 8,00 s → ΔK/Δt = 48,2 kW, potencia media neta dedicada a energía cinética. No llamarla sin matices potencia nominal del motor.

### Prueba tú — elegir el balance (propuesta propia)

«Se eleva a velocidad constante un objeto de 2,00 kg una altura de 3,00 m. Calcula trabajo de la fuerza aplicada, trabajo del peso y cambio de energía cinética. Explica por qué puede aumentar U aunque ΔK sea cero». Con g = 10: +60,0 J, −60,0 J y 0 J. En sistema objeto–Tierra, el trabajo externo aumenta U; no exige aumento de K.

## Diagramas, límites y correcciones del original

- Diagramas energéticos con barras o tabla de estados a una escala común; rotular K, U_g, U_el y energía disipada. No añadir una barra de «trabajo» como energía almacenada final.
- Fuerzas aplicadas y desplazamientos con ángulos inequívocos. F(x) con N y m en los ejes; trayectoria espacial separada de gráficas energéticas.
- Pp. 1–3: sustituir afirmaciones universales sobre fuerza individual y energía cinética por el teorema del trabajo total.
- P. 5: se mezclan bombillas de 60 y 40 W. Si se retiene 100/60 W durante 1 h, entradas de energía 360/216 kJ (0,100/0,0600 kWh). Potencia eléctrica absorbida no equivale a potencia luminosa útil.
- Pp. 7–8: simplificar la explicación de levantar y frenar; distinguir trabajo individual, ΔK y ΔU. Corregir el signo tipográfico del trabajo de gravedad en descenso.
- P. 9: al regresar, misma rapidez y velocidad opuesta.
- P. 12: para oscilador horizontal ideal U = kx²/2, K = k(A²−x²)/2, E = kA²/2. K se anula en ambos extremos ±A, no solo en +A. La velocidad es ±√[k(A²−x²)/m], no siempre la raíz positiva. Integrar como gráfica breve, sin capítulo adicional de MAS.
- P. 15: es el trabajo conservativo o la diferencia de potencial lo que depende de extremos; el valor U de un estado depende del punto y de la elección de cero.

## Referencias y procedencia

A, C, D y E adaptan los originales; B, el elevador y «Prueba tú» son propios. Contraste del teorema y sus condiciones: [OpenStax, trabajo y energía cinética](https://openstax.org/books/university-physics-volume-1/pages/7-3-work-energy-theorem). Los desarrollos y cifras anteriores son cálculos propios sobre los datos especificados.

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
