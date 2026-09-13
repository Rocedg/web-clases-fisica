# T1 — Background editorial: Movimiento rectilíneo

Versión 0.2 para revisión docente · Web Clases Rocedg · 8 de septiembre de 2026

## 1. Función de este documento

Este documento acompaña al PDF original y dirige la creación de una lección propia: especifica selección de contenido, profundidad, orden, ejemplos y diagramas. Está redactado como instrucciones para Codex. No es la lección final ni una orden de cambiar la aplicación.

Fuente revisada: `T1-Movimiento-rectilíneo(1).pdf`, 15 páginas. Las referencias siguientes usan la página del archivo, empezando en 1, porque la numeración impresa se reinicia entre bloques. El documento contiene material identificado como IES La Magdalena, Avilés, y anotaciones manuscritas.

Referencia de estilo disponible: las instrucciones de refinamiento de T0 compartidas en esta conversación. El archivo específico «T0 background», el PDF final de T0 y la imagen de referencia no se han adjuntado a esta revisión. Esta propuesta no presupone haberlos inspeccionado. Cuando estén disponibles, ajustar los criterios comunes sin eliminar las decisiones físicas específicas de T1.

## 2. Qué queremos enseñar

Título propuesto: **T1 — Movimiento rectilíneo: describir, representar y predecir**.

Subtítulo: **Posición, velocidad y aceleración para entender movimientos en una dimensión.**

La pregunta conductora es: «¿Cómo paso de lo que hace un objeto a un dibujo, una gráfica y una ecuación que permitan predecir dónde estará?».

Al terminar, el estudiante debe poder:

- Elegir origen, sentido positivo y comienzo del tiempo.
- Distinguir posición, desplazamiento y distancia recorrida.
- Interpretar velocidad y aceleración con signo.
- Reconocer cuándo usar MRU o MRUA y cuándo sus hipótesis dejan de valer.
- Relacionar gráficas x(t), v(t) y a(t) mediante pendientes y áreas.
- Resolver un encuentro sencillo, un frenado y un lanzamiento vertical.
- Explicar y comprobar un resultado, no solo sustituir números.

Se asumen las unidades, vectores básicos y nociones de derivada e integral de T0. Recordarlas en contexto, sin repetir capítulos completos. La descripción vectorial general de trayectorias curvas se desarrollará en T2.

## 3. Selección del original

| Páginas originales | Material | Decisión editorial |
| --- | --- | --- |
| 1–2 | Posición, desplazamiento, MRU y gráficas | Conservar y reescribir con coordenada x y signos inequívocos. Sustituir la introducción vectorial extensa por un eje recto. |
| 3–5 | Ecuaciones particulares, lectura de gráficas, paso por el origen y encuentro | Conservar las habilidades. Seleccionar ejemplos representativos; evitar repetir cinco veces el mismo procedimiento. |
| 6–7, inicio | Aproximación a la velocidad instantánea | Condensar en una explicación con secante y tangente. Recalcular la tabla si se reutiliza. |
| 7–8 | Desplazamiento y velocidad en una curva | Trasladar el desarrollo a T2. En T1 basta una frase de transición. |
| 9 | Aceleración y distintas trayectorias con aceleración constante | Conservar definición y casos rectilíneos. Trasladar los lanzamientos horizontal y oblicuo a T2. |
| 10–11 | MRUA, ecuaciones, signos y frenado | Núcleo obligatorio. Corregir la ecuación particular del ejemplo de la página 11. |
| 12–13 | Tabla de posiciones, lanzamiento vertical y gráfica v(t) | Conservar caída/tiro vertical y lectura gráfica. La tabla puede ser una comprobación breve. |
| 14–15 | Catálogo de gráficas | Seleccionar casos contrastantes. Sustituir el mosaico de miniaturas por gráficos grandes y relacionados. |

Las anotaciones sobre derivar e integrar en las páginas 2 y 10 orientan el tratamiento: hacer visible la conexión matemática, usando integrales definidas con condiciones iniciales. No copiar literalmente una anotación si es ambigua.

## 4. Contenido obligatorio y convenciones

### A. Sistema de referencia y magnitudes

Usar x para la posición sobre el eje, Δx = x_f − x_i para el desplazamiento y d para la distancia recorrida, siempre no negativa. La posición puede ser negativa; la distancia al origen es |x|. Evitar «espacio» como término indistinto para las tres cosas.

Mostrar un recorrido de ida y vuelta: empezar en x = 2 m, ir a 8 m y terminar en 5 m. Resultado: Δx = 3 m y d = 9 m. El ejemplo es una propuesta nueva, no una transcripción del original.

### B. Velocidad y aceleración

Definir v_media = Δx/Δt; distinguirla de rapidez media = d/Δt. Introducir v(t) = dx/dt y a(t) = dv/dt mediante interpretación gráfica. No llamar velocidad instantánea al cociente de un intervalo finito salvo que la velocidad sea constante.

Explicar que v < 0 indica sentido, no «ir lento». Para v ≠ 0, si v y a tienen el mismo signo aumenta la rapidez; si tienen signos opuestos disminuye. En un instante con v = 0, estudiar lo que ocurre antes y después. No identificar automáticamente a < 0 con frenado.

### C. MRU y MRUA

Para Δt = t − t₀:

- MRU: a = 0; v constante; x = x₀ + vΔt.
- MRUA: a constante; v = v₀ + aΔt; x = x₀ + v₀Δt + ½aΔt².
- Como fórmula derivada útil, v² = v₀² + 2a(x − x₀), solo con a constante. Advertir que al obtener v a partir de v² hace falta determinar su signo físicamente.

En los ejemplos tomar t₀ = 0 salvo necesidad explícita. No presentar aceleración constante como garantía general de trayectoria recta: en este tema el movimiento está restringido a una dimensión.

### D. Gráficas y cálculo

Incluir un conjunto coherente de gráficas apiladas con el mismo eje temporal:

- Pendiente de x(t): velocidad.
- Pendiente de v(t): aceleración.
- Área con signo bajo v(t): desplazamiento.
- Área con signo bajo a(t): cambio de velocidad.
- Distancia recorrida: suma de las áreas en valor absoluto bajo v(t), separando los intervalos de signo.

Mostrar x(t_f) = x(0) + ∫₀ᵗᶠ v(t)dt y v(t_f) = v(0) + ∫₀ᵗᶠ a(t)dt. Obtener brevemente las ecuaciones del MRUA a partir de estas relaciones; evitar un capítulo nuevo de cálculo.

### E. Caída libre y lanzamiento vertical

Declarar el modelo: objeto puntual, sin resistencia del aire, gravedad uniforme cerca de la superficie. Usar y positiva hacia arriba, g > 0 como módulo y a_y = −g. No alternar g como módulo positivo y como componente negativa.

Para la primera versión se propone g = 10 m/s² en los ejemplos, indicado como aproximación didáctica para conservar cuentas sencillas del original; mencionar g ≈ 9,8 m/s² como aproximación habitual. Si se cambia la convención, recalcular todos los resultados.

En el punto más alto, v_y = 0 y a_y = −g: no desaparece la aceleración. Distinguir altura sobre el suelo de elevación respecto del lanzamiento. Detener el modelo al llegar al suelo si no se modela el impacto.

## 5. Recorrido de lectura propuesto

Objetivo orientativo: 10 páginas; admitir 10–12 si los diagramas o ejemplos lo requieren. No heredar automáticamente las nueve páginas de T0.

| Página orientativa | Pregunta y contenido | Visual principal |
| --- | --- | --- |
| 1 | ¿Qué describe la cinemática? Propósito, aprendizajes e índice; conexión T0 → T1 → T2 | Recorrido dibujo → gráfica → ecuación |
| 2 | ¿Dónde está y cuánto se ha movido? Origen, signo, x, Δx y d | Eje grande con ida y vuelta |
| 3 | ¿Cómo cambia la posición? Velocidad media e instantánea | Secante y tangente sobre x(t) |
| 4 | ¿Qué ocurre con velocidad constante? MRU, ecuación y lectura de pendientes | x(t) y v(t) del mismo movimiento |
| 5 | ¿Cuándo se encuentran? Método y ejemplo de dos móviles | Eje común y cruce de dos gráficas x(t) |
| 6 | ¿Acelerar siempre significa ir más rápido? Aceleración y signos | Flechas v/a y gráfica que cruza v = 0 |
| 7 | ¿Cómo se calcula un MRUA? Ecuaciones, condiciones y ejemplo de frenado | Secuencia de posiciones y bloque de cálculo |
| 8 | ¿Qué cuentan pendientes y áreas? Conexión x, v, a y cálculo definido | Tres gráficas apiladas, áreas sombreadas |
| 9 | ¿Qué pasa al lanzar hacia arriba? Caída y tiro vertical | Ascenso, punto más alto y descenso |
| 10 | ¿Cómo abordo un problema? Método, síntesis y comprobaciones | Tabla MRU/MRUA y tres preguntas breves con respuesta |

Si se separa una página densa, conservar este orden. La síntesis no sustituye las explicaciones anteriores.

## 6. Ejemplos que debe desarrollar Codex

Cada ejemplo seguirá: esquema → datos con signo y unidades → modelo → condición del suceso → cálculo → interpretación → comprobación.

1. **MRU breve:** adaptar el ejemplo x₀ = −12 m, v = 5 m/s de la página 5. Paso por el origen a los 2,4 s. Relacionar el resultado con el cruce de x(t) por cero.
2. **Encuentro:** adaptar la página 5: x_A = −10 − 3t y x_B = 30 − 7t, en SI. Se encuentran a los 10 s en x = −40 m. Decir «misma posición al mismo tiempo», no «misma distancia al origen».
3. **MRUA y cambio de sentido:** adaptar la página 11: x₀ = 100 m, v₀ = 20 m/s y a = −5 m/s². Debe resultar x = 100 + 20t − 2,5t²; se detiene instantáneamente a los 4 s en x = 140 m. Si se conserva a después, invierte el sentido. Diferenciar esto de un vehículo que frena y permanece parado: en ese caso cambia el modelo tras la parada.
4. **Tiro vertical:** adaptar las páginas 12–13, v₀ = 15 m/s y g = 10 m/s². Tiempo hasta el máximo: 1,5 s; elevación: 11,25 m. Comparar v(0,8 s) = 7 m/s y v(2,3 s) = −8 m/s. Interpretar ambos signos.

La ida y vuelta y las áreas pueden ser microejemplos nuevos. No reproducir toda la colección de ejercicios. Las preguntas de comprobación se incluyen dentro de la lección, sin crear archivos del sistema de ejercicios.

## 7. Correcciones de la fuente y exclusiones

- Páginas 1, 10 y 11: corregir la confusión entre coordenada con signo, distancia al origen y distancia recorrida. En una dimensión usamos componentes escalares con signo; no afirmar que la distancia es un vector.
- Página 11: aparece un factor a adicional en la ecuación particular de posición. Usar el término −2,5t², sin volver a multiplicar por a.
- Páginas 6–7: recalcular desde x(t) antes de redondear la aproximación a la velocidad. No reproducir cocientes inconsistentes por cifras intermedias truncadas.
- Páginas 13–15: una pendiente negativa de v(t) indica a negativa; solo es frenado donde v sea positiva. x₀ es posición inicial, no «desplazamiento inicial».
- No incluir desarrollos de tiros en dos dimensiones, aceleración normal/tangencial, MCU, fuerzas, energía ni resistencia del aire.
- No convertir el límite de la derivada en una demostración formal extensa.
- No copiar cabeceras, logos, capturas ni toda la redacción original. Redactar material propio y mantener una nota de procedencia del material utilizado.

## 8. Estilo y tarjetas contextuales

Aplicar la dirección de T0: flujo vertical de una columna, diagramas grandes redibujados en TikZ/PGFPlots, tarjetas anchas, acentos azules y párrafos breves. Si está disponible en el repositorio, consultar `docs/design/ui-redesign-reference/Image 22.jpeg` como inspiración visual y reutilizar los componentes de T0 que funcionen.

Alternar explicación, visual, fórmula y aplicación. Los gráficos deben llevar magnitudes, unidades, origen y escalas coherentes; aclarar cuándo son cualitativos. No depender solo del color para distinguir curvas.

Propuestas de «Dato», máximo uno o dos breves por página y sin obligación de incluirlos siempre:

- «Cambiar el origen cambia las coordenadas, pero no el encuentro entre dos móviles.»
- «El velocímetro muestra rapidez; el signo de la velocidad depende del eje elegido.»
- «Un objeto puede tener velocidad nula en un instante y seguir teniendo aceleración.»

Evitar relleno, afirmaciones sobre frecuencia de preguntas PAU, largas historias y repetición de fórmulas sin explicación.

## 9. Instrucción de uso y aceptación

Usa este background junto al original para elaborar la lección T1. Localiza las fuentes y convenciones reales del proyecto antes de elegir rutas. No supongas que la rama piloto de T0 es la rama autorizada para T1.

Este documento fija el encargo editorial. No autoriza cambios de aplicación, base de datos, seguimiento o banco de ejercicios; tampoco ordena commit, push o merge. El prompt de ejecución debe concretar rama y archivos de salida.

La lección será aceptable cuando incluya todo el núcleo anterior, no duplique T2, distinga correctamente signos y distancias, muestre pendientes y áreas con un ejemplo coherente y haya sido compilada y revisada visualmente página a página. Comprobar cálculos de forma independiente; no copiar resultados por confianza en la fuente. Informar de cambios de alcance y limitaciones reales.

## 10. Selección definitiva de ejemplos y profundidad

Esta ampliación concreta qué ejemplos incorporar: no dejar su presencia como un «si cabe». Los ejemplos de la sección 6 se mantienen, con la siguiente distribución. Las nuevas propuestas son de elaboración propia; las referencias externas de la sección 12 aportan enfoques didácticos, no enunciados para copiar.

| Ejemplo | Prioridad y tratamiento | Qué aporta |
| --- | --- | --- |
| Ida y vuelta 2 → 8 → 5 m | Obligatorio, microejemplo en página 2 | Separar posición, desplazamiento y distancia antes de calcular velocidades. |
| MRU desde x₀ = −12 m | Obligatorio, solución breve | Traducir signos y comprobar el paso por el origen. |
| Encuentro de los dos móviles del original | Obligatorio, ejemplo guiado | Una ecuación por objeto, mismo reloj y condición x_A = x_B. |
| MRUA x₀ = 100 m, v₀ = 20 m/s, a = −5 m/s² | Obligatorio, ejemplo guiado | Diferenciar parada instantánea, inversión de sentido y fin de un modelo. |
| Lanzamiento vertical a 15 m/s | Obligatorio, ejemplo guiado | Conectar signos, punto más alto y aceleración persistente. |
| Reacción y frenado | Incorporar como extensión del bloque MRUA | Encadenar dos modelos y evaluar cómo influye la rapidez. |
| Gráfica con áreas de signos opuestos | Obligatorio en la página de gráficas | Obtener desplazamiento y distancia de una misma representación. |
| Tabla x = 10 + 3t² del original, página 12 | Reserva, comprobación breve | Inferir un modelo a partir de datos; evitar otra solución larga. |

No apilar los ejemplos al final: colocarlos junto al concepto que ponen a prueba. Si falta espacio, ampliar una o dos páginas antes que reducir los dibujos. El ejemplo breve de MRU y la tabla no necesitan ocupar páginas completas.

## 11. Ejemplos adicionales listos para desarrollar

### T1-A. Antes de frenar, el móvil sigue avanzando

**Enunciado propio.** Un móvil circula a 72 km/h. Desde que aparece la señal hasta que comienza a frenar transcurren 0,8 s; durante ese intervalo mantiene la velocidad. Después tiene aceleración constante de −5 m/s² hasta detenerse. ¿Qué distancia recorre desde la señal? ¿Qué cambiaría si su velocidad inicial fuera el doble, manteniendo las otras condiciones?

**Antes de calcular:** pedir que distinga el intervalo de reacción del de frenado. Pregunta: «¿Se puede usar una sola aceleración constante desde el comienzo?».

**Solución que debe aparecer:** 72 km/h = 20 m/s. Reacción: d_r = 20 · 0,8 = 16 m. Frenado: duración 4 s y distancia d_f = 20²/(2 · 5) = 40 m. Total 56 m; tiempo total 4,8 s. Tras la parada termina el tramo con a = −5 m/s².

**Visual:** v(t) horizontal de 0 a 0,8 s y descendente hasta cero a los 4,8 s; sombrear rectángulo y triángulo. Dar x = 0 al inicio para conectar área y posición final.

**Variación:** a 40 m/s, reacción 32 m y frenado 160 m: total 192 m. Se duplica la distancia de reacción y se cuadruplica la de frenado, pero el total no se cuadruplica exactamente. Estas cifras corresponden al modelo propuesto, no a una predicción real de seguridad vial.

**Aprendizaje:** elegir el modelo por tramos, convertir unidades y distinguir dependencia lineal y cuadrática. No añadir leyes de rozamiento.

### T1-B. Desplazamiento cero no significa no haberse movido

**Enunciado propio.** Un carrito tiene v(t) = 4 − 2t, en SI, durante 0 ≤ t ≤ 4 s y parte de x₀ = 0. Determina cuándo cambia de sentido, dónde termina y qué distancia recorre.

**Predicción:** mostrar primero la gráfica v(t) sin sombrear y preguntar si vuelve al punto de partida.

**Resultados:** v = 0 en t = 2 s. El área positiva es 4 m y la negativa −4 m: Δx = 0, pero d = 8 m. La posición es x(t) = 4t − t²; alcanza x = 4 m y regresa a x = 0. Velocidad media 0 m/s; rapidez media 2 m/s.

**Visual:** v(t) y x(t) apiladas, mismo eje temporal; marcar t = 2 s en ambas. Usar áreas geométricas y luego escribir la integral definida como segunda lectura de la misma operación.

**Error a discutir:** integrar v entrega desplazamiento; para distancia se separan los intervalos y se suman las áreas en valor absoluto. Este ejemplo desarrolla el contenido de la página 8; no debe duplicarse como un ejercicio extra de otra página.

### T1-C. De una tabla a una ley: reserva del original

Conservar como actividad corta los datos t = 0, 1, 2, 3 s y x = 10, 13, 22, 37 m, con la condición explícita de que parte del reposo. Bajo la hipótesis MRUA se obtiene x₀ = 10 m y a = 6 m/s². Pedir una predicción para t = 4 s: x = 58 m. Advertir que una tabla finita compatible con un modelo no demuestra por sí sola que ese modelo describa cualquier instante futuro.

## 12. Referencias externas y aportación frente a otros recursos

Consulta web realizada el 8 de septiembre de 2026. Se trata de una comparación editorial acotada, no de una auditoría completa de plataformas ni de una afirmación de que carezcan de alguna función.

| Recurso consultado | Qué se observó | Decisión para nuestra lección |
| --- | --- | --- |
| [OpenStax: posición, desplazamiento y velocidad media](https://openstax.org/books/university-physics-volume-1/pages/3-1-position-displacement-and-average-velocity) | Ejemplo desarrollado con estrategia, solución, interpretación y comprobación de comprensión. | Mantener ese recorrido pedagógico en los ejemplos propios; exigir una interpretación final de los signos. |
| [OpenStax: gráficas velocidad-tiempo](https://openstax.org/books/physics/pages/2-4-velocity-vs-time-graphs) | Conecta representaciones, pendientes y áreas, y propone discutir simplificaciones del movimiento. | Añadir T1-B y explicitar dónde termina el modelo de frenado en T1-A. Recalcular todo; no trasladar cifras o frases sin revisión. |
| [Fisicalab: presentación de sus recursos](https://www.fisicalab.com/) | Presenta teoría por niveles, problemas resueltos, interactividades e ilustraciones. La revisión de este sitio se limita a esa presentación. | Hacer que el PDF reúna explicación, ejemplo y comprobación en el mismo punto de lectura; no limitarlo a formularios. |

**Aportación propuesta de Web Clases Rocedg:** continuidad entre temas y una misma notación; un dibujo, una gráfica y una ecuación para el mismo caso; errores frecuentes explicados; una variación pequeña que compruebe si el estudiante entendió el modelo. Es una propuesta editorial, no una superioridad demostrada frente a esos recursos.

**Competencias que debe ejercitar:** interpretar datos, representar una situación, seleccionar hipótesis, justificar signos, calcular, comprobar unidades y comunicar el significado del resultado. No presentar esta lista como alineación normativa con un currículo específico sin una revisión adicional.

## 13. Regla para Codex al incorporar ejemplos de internet

La selección anterior ya contiene ejemplos externos investigados como referencia y propuestas nuevas concretas. Si buscas más, incorpora solo los que cubran una carencia identificada; documenta URL, idea aprovechada y adaptación. Distingue «adaptado del original», «inspirado en una referencia» y «elaboración propia». No copiar páginas ni colecciones enteras, ni atribuir a una fuente los enunciados nuevos.

Cada ejemplo guiado debe incluir una predicción breve, modelo e hipótesis, cálculo legible, resultado con unidades, comprobación y una pregunta de transferencia con respuesta. Las soluciones deben estar dentro del PDF; no depender de una web externa para entender la lección. No añadir herramientas interactivas a la aplicación como parte de este encargo.
