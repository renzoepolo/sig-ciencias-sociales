# Clase 1 — ¿Por qué el "dónde" importa?

**Sistemas de Información Geográfica**
Especialización en Ciencias Sociales Computacionales

---

## Presentación

Les damos la bienvenida a la primera clase de Sistemas de Información Geográfica.

Este seminario parte de una idea sencilla y exigente: a las preguntas que ya hacemos en
ciencias sociales —qué ocurre, por qué ocurre, a quiénes les ocurre— se les puede sumar
una más, que muchas veces cambia la respuesta. **Dónde ocurre.**

Durante ocho encuentros vamos a construir la capacidad de trabajar con datos que tienen
posición: cargarlos, medirlos correctamente, representarlos y analizarlos, siempre con
Python y con herramientas de código abierto. No vamos a usar software con licencia paga,
y no hace falta ninguna formación previa en cartografía.

La clase de hoy se organiza alrededor de una pregunta concreta:

> **¿Las escuelas primarias están donde está la población?**

Es una pregunta que se puede responder con datos públicos argentinos, y que en el camino
nos obliga a aprender casi todo lo básico: qué es un dato geoespacial, cómo se guarda,
cómo se carga en Python y cómo se combinan dos capas de información distintas.

### Contenidos de esta clase

- El origen de los SIG y el caso de John Snow, contado con más cuidado del habitual.
- Qué es un SIG: por qué no es solamente un programa de computadora.
- Cómo se organiza la información geográfica en capas.
- Modelos de datos: vectorial y ráster.
- La biblioteca GeoPandas y el objeto `GeoDataFrame`.
- Formatos de archivo: GeoPackage, GeoJSON, Shapefile y CSV con coordenadas.

### Actividades

1. **Actividad integradora.** Construcción de un indicador de escuelas por habitante a
   nivel provincial, y comparación con el conteo absoluto. Se hace durante la clase, en
   la notebook.
2. **Actividad con inteligencia artificial.** Un ejercicio breve para poner a prueba las
   respuestas de un asistente conversacional sobre datos que no tiene a la vista.
3. **Tarea para la próxima clase.** Se detalla al final de esta página.

---

## Desarrollo

Los contenidos de la clase se trabajan en dos materiales, que se recorren en este orden:

**1. Presentación `Presentación Clase 1.pdf` (25 diapositivas).**
Expone la parte conceptual: qué es un SIG, cómo se organiza la información en capas, la
diferencia entre los modelos vectorial y ráster, y para qué se usan los SIG en la gestión
y la planificación del territorio. Se ve en el encuentro sincrónico.

**2. Notebook `Clase_1.ipynb` (Google Colab).**
Es la parte práctica. Retoma cada concepto de la presentación y lo pone a prueba con
datos reales: el padrón de escuelas primarias del Ministerio de Educación y la capa de
provincias del Instituto Geográfico Nacional. La notebook indica, en cada bloque, a qué
diapositivas corresponde.

No hace falta instalar nada: se abre directamente en Google Colab desde el enlace del
aula. La primera celda prepara el entorno y descarga los datos automáticamente.

> **Importante.** La notebook está pensada para ejecutarse durante el encuentro, no para
> leerse después. Si podés, abrila antes de que empiece la clase y ejecutá la primera
> celda: tarda un minuto o dos en instalar las bibliotecas.

---

## Cierre

### Qué trabajamos hoy

Empezamos por el caso fundacional de la disciplina y lo usamos para instalar la distinción
que va a atravesar todo el seminario. El mapa de John Snow mostró que las muertes por
cólera y una bomba de agua **aparecían juntas en el territorio**. Eso es una asociación
espacial, y es un hallazgo valioso. Pero no alcanzaba para afirmar que el agua causaba la
enfermedad: esa afirmación necesitó trabajo de campo y un mecanismo físico verificable.
**Un patrón espacial señala dónde mirar; no explica por sí solo lo que se encuentra.**

Después vimos que trabajar con datos geoespaciales en Python es menos exótico de lo que
suena. Un `GeoDataFrame` es una tabla común con una columna que guarda figuras en lugar
de números, y todo lo que ya se sabe de pandas sigue valiendo. La misma función,
`read_file()`, abre casi cualquier formato; lo que cambia entre formatos no es cómo se
leen, sino qué garantías ofrecen. El Shapefile, el más difundido, es también el que más
información pierde: corta los nombres de campo a diez caracteres y no siempre declara su
codificación de caracteres. Por eso en este curso guardamos siempre en GeoPackage.

La actividad integradora dejó el resultado más importante del día. Al calcular escuelas
por provincia obtuvimos **dos mapas del mismo dato que cuentan historias opuestas**: el
conteo absoluto ubica las escuelas en el centro del país, y la tasa por habitante las
ubica en el sur y el noroeste. Ninguno de los dos miente. Responden preguntas distintas, y
elegir cuál mostrar es una decisión con consecuencias.

También dejamos dos cosas deliberadamente sin resolver, y conviene tenerlas presentes:

- **Medimos en grados.** Las coordenadas con las que trabajamos no sirven para calcular
  distancias ni superficies. Lo resolvemos en la Clase 3.
- **Usamos la provincia como unidad de análisis** sin haberlo justificado. Dentro de una
  provincia como Buenos Aires conviven realidades incomparables, y promediarlas no
  describe bien a ninguna. Ese es el tema de la próxima clase.

### Tarea para la Clase 2

Elegí **una pregunta territorial de tu propio campo de investigación**. Puede ser del tipo
"¿dónde ocurre X?" o "¿X e Y ocurren en los mismos lugares?".

Escribí entre tres y cuatro oraciones que respondan:

1. Cuál es la pregunta.
2. Qué dos capas de datos necesitarías para responderla.
3. Cuál sería la unidad territorial de análisis —provincia, departamento, radio censal,
   barrio, celda de una grilla— y por qué esa y no otra.

**Formato:** un archivo de texto o un mensaje en el foro de la clase.
**Entrega:** antes del próximo encuentro.

El punto tres es el que más nos interesa. En la Clase 2 vamos a ver que esa decisión, que
suele tomarse por conveniencia o por disponibilidad de datos, puede cambiar por completo
el resultado de un análisis.

### Material de la clase

| Material | Descripción |
|---|---|
| `Presentación Clase 1.pdf` | Diapositivas del encuentro |
| `Clase_1.ipynb` | Notebook práctica, para abrir en Google Colab |
| `Clase_1_opcional.ipynb` | Ampliación: historia de los SIG y el modelo ráster en detalle |

### Bibliografía

- Olaya, V. *Sistemas de Información Geográfica*, capítulos 1 y 2. Disponible en línea.
- Rey, S. J., Franklin, R. S. y Wei, D. (2021). *Geographic Data Science with Python*.
  University of California Press. Capítulo 1.
