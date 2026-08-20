# Sistemas de Información Geográfica

**Especialización en Ciencias Sociales Computacionales**
Universidad Nacional Guillermo Brown · Docente: Renzo Polo

Materiales del seminario: notebooks ejecutables, presentaciones y los datos preparados
para cada clase. Todo con herramientas de código abierto.

---

## Cómo cursar

Las notebooks se abren en **Google Colab**, sin instalar nada en tu computadora.

| Clase | Tema | Notebook |
|---|---|---|
| 1 | ¿Por qué el "dónde" importa? | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%201/Clase_1.ipynb) |
| 2 | Las particularidades del dato espacial | *próximamente* |
| 3 | Sistemas de referencia y proyecciones | *próximamente* |
| 4 | Adquisición de datos: IDE, geoservicios y datos abiertos | *próximamente* |
| 5 | Cartografía temática | *próximamente* |
| 6 | Geoprocesamiento | *próximamente* |
| 7 | Autocorrelación espacial | *próximamente* |
| 8 | Inferencia espacial | *próximamente* |

Cada clase incluye:

- una **presentación** con la parte conceptual;
- una **notebook** con la práctica, que referencia las diapositivas correspondientes.

La consigna, el cierre y la tarea de cada clase se publican en el aula virtual de la
Especialización.

---

## Los datos

Los datasets están en `datos/`, en formato **GeoPackage**, ya curados: nombres de columna
legibles, codificación UTF-8 y sistema de referencia declarado.

No hace falta descargarlos a mano. Las notebooks usan la función `cargar()` del módulo
`sig_utils.py`, que los baja una sola vez y los guarda en caché:

```python
from sig_utils import cargar
provincias = cargar("provincias")
```

| Dataset | Contenido | Fuente |
|---|---|---|
| `paises` | 177 países del mundo | Natural Earth 110m |
| `provincias` | 24 jurisdicciones argentinas con población y hogares | IGN / INDEC Censo 2022 |
| `ruta40` | Traza de la Ruta Nacional 40 | IGN |
| `escuelas` | 22.753 escuelas primarias georreferenciadas | Ministerio de Educación |

Para ver el catálogo completo:

```python
from sig_utils import CATALOGO
for nombre, info in CATALOGO.items():
    print(f"{nombre}: {info['descripcion']}")
```

---

## Usar los materiales en tu computadora

No es necesario, pero es posible:

```bash
git clone https://github.com/renzoepolo/sig-ciencias-sociales.git
cd sig-ciencias-sociales
pip install geopandas==1.0.1 mapclassify==2.8.1 folium==0.17.0 matplotlib==3.9.2
jupyter lab
```

---

## Licencia y atribución

Los materiales de este repositorio —notebooks, presentaciones y textos— se publican bajo
[**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/deed.es). Podés usarlos,
adaptarlos y redistribuirlos citando la fuente y manteniendo la misma licencia.

Los **datos** conservan la licencia de sus organismos de origen:

- **Natural Earth** — dominio público.
- **Instituto Geográfico Nacional (IGN)** — datos abiertos, atribución requerida.
- **INDEC**, Censo Nacional de Población, Hogares y Viviendas 2022 — uso público.
- **Ministerio de Educación de la Nación**, padrón de establecimientos educativos.

Los archivos de `datos/` son versiones derivadas: se recortaron columnas, se
normalizaron nombres y se convirtió el formato. Las geometrías y los valores no fueron
alterados.

Si usás estos materiales en una clase o publicación, una cita es suficiente:

> Polo, R. (2026). *Sistemas de Información Geográfica*. Especialización en Ciencias
> Sociales Computacionales, Universidad Nacional Guillermo Brown.
> https://github.com/renzoepolo/sig-ciencias-sociales
