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
| 2 | Las particularidades del dato espacial | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%202/Clase_2.ipynb) |
| 3 | ¿De dónde saco los datos? | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%203/Clase_3.ipynb) |
| 4 | Sistemas de referencia y proyecciones | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%204/Clase_4.ipynb) |
| 5 | Cartografía temática: ¿dónde está la pobreza? | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%205/Clase_5.ipynb) |
| 6 | Análisis espacial: construir variables territoriales | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%206/Clase_6.ipynb) |
| 7 | Accesibilidad y cambio de unidad de análisis | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%207/Clase_7.ipynb) |
| 8 | Autocorrelación espacial: ¿el patrón es azar? | [Abrir en Colab](https://colab.research.google.com/github/renzoepolo/sig-ciencias-sociales/blob/main/Clase%208/Clase_8.ipynb) |

Cada clase incluye:

- una **presentación** con la parte conceptual;
- una **notebook** con la práctica, que referencia las diapositivas correspondientes.

La consigna, el cierre y la tarea de cada clase se publican en el aula virtual de la
Especialización.

El seminario se aprueba con un trabajo final: una notebook propia, sobre una pregunta
territorial elegida por cada estudiante. La consigna y la rúbrica están en
[`TRABAJO_FINAL.md`](TRABAJO_FINAL.md).

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
| `departamentos_nbi` | 527 departamentos con indicadores de hogares del Censo 2022 | INDEC |
| `osm_barrios` / `osm_amenities` | Recoleta y Villa Lugano, y sus 1.770 equipamientos | OpenStreetMap |
| `ign_salud` | 8.311 establecimientos de salud del país | IGN, geoservicio WFS |
| `salud_barrios` | Los 13 efectores de salud que caen en esos dos barrios | IGN |
| `caba_radios_2022` | 3.554 radios censales de CABA con población, hogares y NBI | BA Data — Censo 2022 |
| `caba_isocronas` / `caba_rutas_ors` | Isocronas de caminata y rutas por calle, congeladas | OpenRouteService |

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
