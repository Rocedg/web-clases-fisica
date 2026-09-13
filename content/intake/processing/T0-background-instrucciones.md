# T0 — Background e instrucciones para crear la lección PDF

## Objetivo del documento

Crear la primera versión de la lección PDF:

**T0 — Herramientas para empezar Física**

El objetivo no es copiar el PDF antiguo, sino transformarlo en una lección moderna, visual y coherente con la interfaz de **Web Clases Rocedg**.

Debe servir como molde para futuras lecciones: limpia, rápida de leer, con diagramas claros, fórmulas destacadas y buena integración visual cuando se vea embebida dentro de la web.

---

## Restricción de tiempo

No dedicar mucho tiempo a seleccionar frase por frase.

Regla práctica:

- máximo 20 minutos por PDF para decidir estructura y contenido;
- el PDF antiguo manda el contenido base;
- estas instrucciones mandan el enfoque;
- la plantilla visual manda el diseño.

No perseguir perfección en la primera versión. Esta lección es un piloto.

---

## Estructura simple de archivos

Evitar muchas carpetas por ahora.

Usar algo simple:

```text
content/
├── intake/
│   ├── T0-original.pdf
│   ├── T0-instrucciones.md
│   ├── T1-original.pdf
│   └── T1-instrucciones.md
│
├── latex/
│   ├── T0-introduccion.tex
│   └── T1-movimiento-rectilineo.tex

static/
└── lessons/
    ├── T0-introduccion.pdf
    ├── T0-resumen.pdf
    ├── T1-movimiento-rectilineo.pdf
    └── T1-resumen.pdf
```

No crear una carpeta por cada lección todavía.

---

## Fuente base

Usar como material de entrada:

```text
content/intake/T0-original.pdf
```

El PDF contiene:

- magnitudes, medida, unidades y análisis dimensional;
- vectores: escalares/vectoriales, módulo, dirección, sentido, igualdad, suma, resta, componentes y vectores unitarios;
- cifras significativas;
- cálculo de errores;
- producto escalar y producto vectorial en apuntes manuscritos;
- trigonometría básica;
- derivadas e integrales en apuntes manuscritos.

---

## Título nuevo

```text
T0 — Herramientas para empezar Física
```

Subtítulo sugerido:

```text
Magnitudes, unidades, vectores, errores y herramientas matemáticas básicas.
```

---

## Estilo visual

La lección debe parecer parte de la web, no un PDF antiguo pegado dentro de un visor.

Usar una estética tipo:

- fondo blanco;
- azul principal de Web Clases Rocedg;
- texto navy/azul muy oscuro;
- cajas suaves con bordes finos;
- verde para ideas correctas o relaciones útiles;
- amarillo suave para advertencias o errores típicos;
- fórmulas centradas y bien separadas;
- diagramas redibujados, no capturas feas del PDF antiguo;
- páginas limpias pero con contenido suficiente;
- evitar páginas demasiado vacías;
- evitar saturación visual.

Debe verse bien:

- embebido dentro de la web;
- descargado como PDF normal;
- con zoom dentro del visor.

---

## Estructura propuesta de la lección

### Página 1 — Medir, magnitudes y unidades

Debe caber todo en una página.

Incluir:

- qué es una magnitud;
- qué significa medir;
- qué es una unidad;
- resultado físico = número + unidad;
- Sistema Internacional de forma compacta;
- idea básica de análisis dimensional.

No separar el Sistema Internacional en una página distinta.

#### Diagramas sugeridos para página 1

1. **Mesa medida con unidades repetidas**
   - Redibujar la idea del bolígrafo/unidad sobre una mesa.
   - Mostrar que medir es contar cuántas veces cabe la unidad en la magnitud.
   - Etiquetas:
     - magnitud: longitud de la mesa;
     - unidad elegida: bolígrafo;
     - resultado: 7 bolígrafos.

2. **Tarjeta “Número + unidad”**
   - Visual simple:
     ```text
     medida física = valor numérico + unidad
     ```
   - Ejemplos rápidos:
     ```text
     3,2 m
     5,0 s
     12 N
     ```

3. **Mini tabla del Sistema Internacional**
   - Longitud — m
   - Masa — kg
   - Tiempo — s
   - Corriente — A
   - Temperatura — K
   - Cantidad de sustancia — mol
   - Intensidad luminosa — cd

4. **Mini escalera dimensional**
   - Mostrar cómo de magnitudes fundamentales salen derivadas:
     ```text
     L, T → velocidad [v] = L T⁻¹
     L, T → aceleración [a] = L T⁻²
     M, L, T → fuerza [F] = M L T⁻²
     ```

---

### Página 2 — Vectores I: definición y formas de escribirlos

Aquí empieza la parte gráfica importante.

Incluir:

- escalar vs vector;
- módulo;
- dirección;
- sentido;
- igualdad de vectores;
- multiplicación por escalar;
- formas equivalentes de escribir un vector.

Explicar explícitamente que un vector puede representarse como:

```text
1. una flecha geométrica;
2. un par o terna de componentes;
3. una matriz columna;
4. combinación de vectores unitarios i, j, k.
```

Ejemplo:

```text
v = (4, 3)

v = [4]
    [3]

v = 4 i + 3 j
```

#### Diagramas sugeridos para página 2

1. **Anatomía de un vector**
   - Flecha grande con:
     - módulo;
     - dirección;
     - sentido.

2. **Escalar vs vector**
   - Dos tarjetas:
     - temperatura: 25 °C → escalar;
     - velocidad: 25 m/s hacia la derecha → vector.

3. **Multiplicación por escalar**
   - Dibujar `v`, `2v`, `0,5v`, `-v`.
   - Resaltar:
     - mismo sentido si el escalar es positivo;
     - sentido contrario si el escalar es negativo.

4. **Mismo vector, cuatro escrituras**
   - Una sola figura que conecte:
     - flecha;
     - coordenadas;
     - matriz columna;
     - expresión `v = vx i + vy j`.

---

### Página 3 — Vectores II: suma y resta

Incluir:

- suma por regla del paralelogramo;
- suma punta-cola;
- resta como suma del opuesto;
- resta uniendo extremos;
- suma/resta por componentes;
- suma/resta usando vectores unitarios.

Fórmulas a destacar:

```text
A + B = (Ax + Bx, Ay + By)
A - B = (Ax - Bx, Ay - By)
```

Y también:

```text
A = Ax i + Ay j
B = Bx i + By j

A + B = (Ax + Bx)i + (Ay + By)j
```

#### Diagramas sugeridos para página 3

1. **Suma por paralelogramo**
   - Dos vectores desde el mismo origen.
   - Paralelas punteadas.
   - Diagonal como resultante.

2. **Suma punta-cola**
   - Vector A seguido de vector B.
   - Resultante desde el inicio de A hasta el final de B.
   - Comparar con el paralelogramo.

3. **Resta como suma del opuesto**
   - Mostrar `A - B = A + (-B)`.
   - Dibujar `B` y `-B`.

4. **Suma por componentes en una cuadrícula**
   - Usar componentes x/y.
   - Mostrar que sumar vectores equivale a sumar coordenadas.

---

### Página 4 — Vectores III: componentes y geometría básica

Incluir:

- descomposición en componentes x/y;
- relación con trigonometría;
- seno, coseno y tangente en triángulo rectángulo;
- módulo de un vector;
- ángulo de un vector;
- extensión a 3D con i, j, k.

Fórmulas clave:

```text
vx = v cos(α)
vy = v sen(α)

|v| = √(vx² + vy²)

tan(α) = vy / vx
```

Para 3D:

```text
v = vx i + vy j + vz k

|v| = √(vx² + vy² + vz²)
```

#### Diagramas sugeridos para página 4

1. **Descomposición del vector en x/y**
   - Vector inclinado.
   - Proyección horizontal `vx`.
   - Proyección vertical `vy`.
   - Ángulo `α` respecto al eje x.

2. **Triángulo trigonométrico mínimo**
   - Hipotenusa `v`.
   - Cateto adyacente `vx`.
   - Cateto opuesto `vy`.
   - Fórmulas al lado.

3. **Sistema 3D con i, j, k**
   - Ejes x, y, z.
   - Vector con tres componentes.
   - No hacerlo demasiado complejo.

---

### Página 5 — Producto escalar y producto vectorial

Incluir como ficha de referencia.

No desarrollarlo en exceso, pero sí dejarlo claro porque aparecerá en física.

Producto escalar:

```text
u · v = |u| |v| cos(α)
```

Ideas:

- mide cuánto apunta un vector en la dirección del otro;
- sirve para proyecciones;
- si son perpendiculares, el producto escalar es cero;
- si son paralelos, es máximo en valor absoluto.

Producto vectorial:

```text
u × v
```

Ideas:

- da un vector perpendicular al plano formado por ambos vectores;
- su módulo es el área del paralelogramo;
- usa la regla de la mano derecha;
- si los vectores son paralelos, el producto vectorial es cero;
- si son perpendiculares, su módulo es máximo.

Fórmula de módulo:

```text
|u × v| = |u| |v| sen(α)
```

#### Diagramas sugeridos para página 5

1. **Producto escalar como proyección**
   - Dos vectores con ángulo α.
   - Proyección de uno sobre el otro.
   - Etiqueta: `|u| cos(α)`.

2. **Producto vectorial como perpendicular**
   - Dos vectores en un plano.
   - Vector resultado saliendo perpendicular al plano.

3. **Regla de la mano derecha**
   - Dibujo simple de mano o flechas curvas.
   - Alternativa si no se quiere dibujar mano: arco de giro de `u` hacia `v` y vector perpendicular `u × v`.

4. **Área del paralelogramo**
   - Paralelogramo formado por `u` y `v`.
   - Área asociada a `|u × v|`.

---

### Página 6 — Cifras significativas

Incluir:

- qué son cifras significativas;
- ceros a la izquierda;
- ceros a la derecha;
- notación científica;
- suma/resta;
- multiplicación/división;
- redondeo.

Caja importante:

```text
No tiene sentido dar más cifras que las permitidas por la incertidumbre de la medida.
```

Aquí no hace falta mucho diagrama. Mejor usar ejemplos limpios y tarjetas.

---

### Página 7 — Errores e incertidumbre

Incluir:

- error absoluto;
- error relativo;
- resultado como `x ± Δx`;
- incertidumbre del aparato;
- medidas repetidas solo como introducción.

Fórmulas:

```text
Ea = Vmedido - Vverdadero

Er = |Ea| / Vverdadero · 100

x ± Δx
```

Caja de error típico:

```text
La precisión de la medida no puede ser mayor que la del error.
```

No alargar demasiado esta página.

---

### Página 8 — Derivadas e integrales para física

Incluir:

- derivada como pendiente instantánea;
- secante que se convierte en tangente;
- integral definida como área bajo la curva;
- integrar normalmente desde `t = 0` hasta `t = t_final` en problemas físicos introductorios;
- integral indefinida solo como nota secundaria.

Priorizar integrales definidas.

Fórmulas:

```text
f'(a) = lim(Δa → 0) [f(a + Δa) - f(a)] / Δa

∫[0, tf] f(t) dt
```

#### Diagramas sugeridos para página 8

1. **Derivada como pendiente**
   - Curva.
   - Dos puntos cercanos.
   - Recta secante.
   - Recta tangente en el límite.
   - Etiqueta: pendiente instantánea.

2. **Integral definida como área**
   - Curva `f(t)`.
   - Eje temporal.
   - Área sombreada entre `t = 0` y `t = tf`.

---

## Prioridad de diagramas

La prioridad gráfica es:

1. Página 1: medida, unidad y análisis dimensional.
2. Páginas 2–4: vectores, representaciones, suma/resta y componentes.
3. Página 5: producto escalar/vectorial con proyección, perpendicularidad y mano derecha.
4. Página 8: derivada e integral con gráficos.
5. Páginas 6–7: menos dibujo, más ejemplos claros.

---

## Decisiones de contenido

Mantener:

- conceptos físicos y matemáticos importantes;
- enfoque de signos, unidades y dimensiones;
- ejemplos representativos;
- uso de diagramas para explicar vectores;
- producto escalar/vectorial como referencia inicial;
- derivadas e integrales desde interpretación gráfica.

Modificar:

- diseño antiguo;
- cajas densas;
- diagramas demasiado toscos;
- orden demasiado fragmentado;
- exceso de texto corrido.

Añadir:

- diagramas redibujados;
- tarjetas de idea clave;
- errores típicos;
- mini formularios;
- transiciones más suaves con la web;
- lenguaje visual consistente.

Evitar:

- demasiadas carpetas;
- demasiada selección manual;
- páginas extremadamente largas;
- copiar capturas del PDF antiguo como solución final;
- hacer una teoría matemática demasiado avanzada;
- dedicar demasiado espacio a integrales indefinidas.

---

## Resultado esperado

Generar:

```text
content/latex/T0-introduccion.tex
static/lessons/T0-introduccion.pdf
static/lessons/T0-resumen.pdf
```

El PDF final debe estar listo para:

- mostrarse en la Biblioteca de teoría;
- abrirse embebido dentro de la web;
- descargarse;
- registrarse como recurso abierto/descargado en el backend de actividad.

---

## Nota importante

Este T0 es una lección de herramientas. No debe sentirse como una unidad aislada demasiado pesada, sino como una base útil para entender después:

- cinemática;
- fuerzas;
- campos;
- electromagnetismo;
- óptica;
- física moderna.

