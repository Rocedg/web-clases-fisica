# Rocedg Física Bach

Plataforma web sencilla para organizar apuntes, ejercicios, exámenes e información PAU de Física de Bachillerato.

El proyecto mantiene una arquitectura deliberadamente ligera: Flask en Python, plantillas HTML con Jinja, CSS estático y datos en JSON. No usa base de datos ni frameworks frontend, así que sigue siendo fácil de desplegar en Render y de ampliar poco a poco.

## Qué es Flask y para qué sirve

Flask es un microframework de Python para crear aplicaciones web. En este proyecto se encarga de:

- Definir las rutas de la web, por ejemplo `/`, `/topics`, `/homework` o `/exams`.
- Renderizar las plantillas HTML de `templates/`.
- Leer datos desde archivos JSON de `data/`.
- Gestionar sesiones simples para proteger secciones de estudio.
- Servir archivos estáticos como CSS y PDFs desde `static/`.

La ventaja de Flask aquí es que permite mantener el proyecto pequeño, claro y compatible con Render sin introducir una base de datos o un frontend más complejo antes de tiempo.

## Estructura del proyecto

```text
.
├── app.py
├── data/
│   ├── exams.json
│   ├── quizzes.json
│   ├── summaries.json
│   └── topics.json
├── static/
│   ├── css/
│   │   ├── components.css
│   │   ├── layout.css
│   │   ├── pages.css
│   │   ├── responsive.css
│   │   ├── style.css
│   │   └── tokens.css
│   └── pdfs/
├── templates/
│   ├── base.html
│   ├── components/
│   │   └── _macros.html
│   ├── errors/
│   ├── home.html
│   ├── login.html
│   └── user/
├── tests/
│   └── test_app_smoke.py
├── requirements.txt
├── run-local.ps1
├── setup-local.ps1
├── start-web.bat
└── README.md
```

## Cómo ejecutar en local

El entorno anterior `venv/` apuntaba a una instalación antigua de Python, así que se creó un entorno nuevo `.venv/` ignorado por Git.

## Forma rápida en Windows

Hay tres formas sencillas de arrancar la web en Windows.

Opción A: doble clic

```text
start-web.bat
```

Opción B: desde PowerShell

```powershell
.\run-local.ps1
```

Opción C: primera configuración

```powershell
.\setup-local.ps1
```

La web se abre en:

```text
http://127.0.0.1:5000
```

La terminal debe quedarse abierta mientras pruebas la web. Para parar el servidor local, pulsa `CTRL+C`.

Si PowerShell bloquea scripts por la política de ejecución de Windows, usa `start-web.bat` con doble clic.

En Windows PowerShell:

```powershell
py -m venv .venv
$env:PYTHONIOENCODING = "utf-8"
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Después abre:

```text
http://127.0.0.1:5000
```

Nota: `PYTHONIOENCODING=utf-8` ayuda a evitar errores de consola porque la ruta del proyecto contiene emojis.

En este equipo concreto, `ensurepip` no pudo escribir en la carpeta temporal de Windows. Para evitar tocar instalaciones globales, se uso esta alternativa:

```powershell
py -m pip install -r requirements.txt --target .venv\Lib\site-packages
```

El resultado es el mismo para el proyecto: Flask y sus dependencias quedan disponibles dentro de `.venv`.

## Usuarios de prueba

```text
Usuario: Guest
Contraseña: studentpass
```

```text
Usuario: Paul
Contraseña: fisica2026
```

## Cambios del rediseño

### Estructura Flask

- Se mantuvo `app.py` como punto de entrada compatible con Render.
- Se añadieron cargadores JSON reutilizables para temas, quizzes, exámenes y resúmenes.
- Se movieron exámenes y resúmenes a `data/exams.json` y `data/summaries.json`.
- Se añadió `asset_url()` para convertir rutas `static/...` en URLs correctas desde templates.
- Se centralizó la navegación principal en `NAV_ITEMS`.

### Interfaz

- La home ahora funciona como panel de estudio.
- La navegación principal muestra Apuntes, Ejercicios, Exámenes y PAU de forma directa.
- Se conservó la paleta existente: azul principal `#84b6f4`, fondo claro y beige para segundo curso.
- Se eliminaron referencias a imágenes inexistentes en `static/img/`.
- Las páginas comparten tarjetas, cabeceras y acciones visuales coherentes.

### Templates

- `templates/base.html` define la estructura global, navegación y footer.
- `templates/components/_macros.html` contiene macros reutilizables para cabeceras y tarjetas PDF.
- `templates/user/topics.html` y `templates/user/homework.html` se simplificaron.
- `templates/user/exams.html` ahora se alimenta desde JSON.
- `templates/user/miscellaneous.html` se reorganizó como página clara de información PAU.
- Login y errores usan el mismo lenguaje visual que el resto de la web.

### CSS

El CSS se separó para que sea más fácil crecer:

- `tokens.css`: colores, sombras, radios y variables.
- `layout.css`: estructura global, navegación y footer.
- `components.css`: tarjetas, botones, badges, formularios y componentes reutilizables.
- `pages.css`: estilos específicos de páginas.
- `responsive.css`: ajustes móviles.
- `style.css`: archivo principal que importa los demás.

## Validaciones realizadas

Se revisó lo siguiente:

- Sintaxis de Python con `ast.parse`.
- JSON válido en `data/`.
- Sintaxis Jinja de todos los templates.
- Rutas `url_for(...)` usadas en templates.
- Referencias entre templates.
- Imports CSS.
- Enlaces `static/...` definidos en JSON.
- Render básico con Flask test client para rutas públicas y protegidas.

## Comandos de validación

Comandos útiles:

```powershell
$env:PYTHONIOENCODING = "utf-8"
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -B -c "from app import app; print(app.url_map)"
.\.venv\Scripts\python.exe -B -c "from app import app; c=app.test_client(); print(c.get('/').status_code)"
```

## Despliegue en Render

El proyecto sigue usando `requirements.txt`, Flask y Gunicorn, así que mantiene compatibilidad con Render.

Un comando típico de arranque en Render sería:

```text
gunicorn app:app
```

Para producción conviene definir una variable de entorno:

```text
SECRET_KEY=<valor-seguro>
```

Si no se define, `app.py` usa una clave de desarrollo para poder trabajar en local.

## Próximos pasos recomendados

- Mover usuarios hardcodeados a variables de entorno o un sistema más seguro.
- Crear JSON para más recursos si crece la biblioteca.
- Añadir seguimiento de progreso cuando decidas introducir persistencia.
- Revisar si `/exams` debe requerir login igual que apuntes, ejercicios e información PAU.
