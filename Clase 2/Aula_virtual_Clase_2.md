# Clase 2 — Las particularidades del dato espacial

**Sistemas de Información Geográfica**
Especialización en Ciencias Sociales Computacionales

---

## Presentación

### Antes de empezar: qué vimos la clase pasada

En el primer encuentro instalamos dos ideas que hoy se ponen a trabajar.

La primera vino del mapa de John Snow: un patrón espacial muestra **dónde** ocurren las
cosas juntas, pero no explica por qué. La asociación espacial y la explicación causal son
cosas distintas, y confundirlas es el error más caro que se puede cometer con datos
territoriales.

La segunda apareció al final, casi como un efecto secundario. Calculamos escuelas por
provincia de dos maneras —conteo absoluto y tasa por habitante— y obtuvimos **dos mapas
que decían cosas opuestas**. Ninguno mentía: respondían preguntas diferentes.

### El tema de hoy

Esa segunda idea tenía una trampa que dejamos sin abrir: usamos la provincia como unidad
de análisis sin justificarlo en ningún momento. La usamos porque los datos venían así.

Hoy vamos a ver que esa decisión, que suele tomarse por conveniencia, **puede cambiar el
resultado de un análisis**. Y no de manera menor: vamos a comprobar que el máximo de un
indicador cae un 41 % con solo correr una grilla media celda, sin modificar ni un dato.

La pregunta que organiza la clase es:

> **¿Cambia la respuesta si cambio la grilla?**

Los datos espaciales tienen un conjunto de propiedades que los vuelven distintos de una
tabla común y que rompen supuestos que la estadística da por sentados. Hoy las recorremos
una por una, y sobre todo **las medimos**: ninguna se queda en la definición.

### Contenidos de esta clase

- La primera ley de la geografía y su amenaza al supuesto de independencia.
- Escala de análisis: por qué la longitud de una ruta depende de cómo se la mide.
- El problema de la unidad de área modificable, separado en sus dos componentes:
  efecto de agregación y efecto de zonificación.
- Efecto de borde.
- Localización representada: cuándo un centroide representa mal a su área.
- Falacia ecológica.

### Actividades

1. **Actividad integradora.** Localización del foco de concentración escolar de una
   provincia con tres grillas distintas, y medición de cuánto se mueve.
2. **Actividad con inteligencia artificial.** Un ejercicio sobre el límite entre lo que se
   puede deducir y lo que solo se puede medir.
3. **Tarea para la próxima clase.** Se detalla al final.

---

## Desarrollo

Los contenidos se trabajan en dos materiales, en este orden:

**1. Presentación `Presentación Clase 2.pdf`, diapositivas 1 a 16.**
Expone los componentes de la información geográfica, su organización en capas y las siete
particularidades del dato espacial. Se ve en el encuentro sincrónico.

> **Nota:** las diapositivas sobre formatos de archivo (Shapefile, GeoPackage, GeoJSON,
> WKT) se vieron en la Clase 1, junto con la práctica de carga de datos.

**2. Notebook `Clase_2.ipynb` (Google Colab).**
Retoma cada particularidad de la presentación y la mide con datos reales: las escuelas
primarias del Ministerio de Educación, las provincias del IGN y la traza de la Ruta
Nacional 40. Cada bloque indica a qué diapositiva corresponde.

Como en la clase anterior, conviene abrirla y ejecutar la primera celda antes de que
empiece el encuentro.

---

## Cierre

### Qué trabajamos hoy

La clase tuvo un solo argumento, sostenido con seis mediciones distintas: **las decisiones
metodológicas que parecen técnicas y neutrales tienen consecuencias sustantivas**, y casi
nunca se declaran.

Empezamos comprobando que la primera ley de la geografía se cumple en nuestros datos: las
provincias vecinas se parecen un 38 % más entre sí que dos provincias cualesquiera. Eso
significa que 24 provincias no son 24 observaciones independientes, y que aplicarles
estadística convencional exagera cuánta información tenemos.

Después vimos que la Ruta 40 mide 5.166 km o 4.152 km según el nivel de detalle con que se
la represente. No hay un valor verdadero esperando ser descubierto: **la escala es parte de
la definición de la medición**.

El núcleo de la clase fue el problema de la unidad de área modificable, que separamos en
sus dos componentes. Con celdas de idéntica superficie, correr la grilla media celda hizo
caer el máximo de escuelas de 283 a 167. Con celdas cada vez más grandes, la variabilidad
del indicador se redujo a la mitad. La conclusión práctica es incómoda: **agregar oculta
desigualdad**, y un mapa por provincia siempre se verá más homogéneo que el mismo
fenómeno por radio censal.

Cerramos con tres problemas más. El efecto de borde, que subestima un 9 % los valores de
las unidades cercanas al límite de la zona de estudio, y que con un radio de análisis de
20 km llega a contaminar al 43 % de las observaciones. La localización representada, donde
vimos que el centroide geométrico de Buenos Aires está a 186 km de donde realmente vive la
gente. Y la falacia ecológica, con una correlación que pasa de 0,21 entre escuelas a 0,76
entre provincias: el gráfico agregado es el que uno publicaría, y es el que induce al
error.

### La idea para llevarse

Ninguno de estos problemas tiene una solución puramente técnica. No existe la grilla
correcta ni la escala verdadera. Existe la unidad **adecuada al fenómeno que se estudia**,
y la obligación de declarar cuál se eligió y por qué. Un análisis territorial serio no es
el que evita estos problemas, sino el que los explicita.

### Tarea para la Clase 3

Retomá la pregunta territorial que escribiste para hoy y agregale un párrafo que responda:

1. **Qué unidad territorial** vas a usar y por qué esa, y no una más chica o más grande.
2. **Qué límite** tiene tu zona de estudio y si hay efecto de borde. Si lo hay, cómo pensás
   tratarlo.
3. **Qué afirmación NO vas a poder hacer** con datos agregados a esa unidad.

**Extensión:** media carilla.
**Formato:** archivo de texto o mensaje en el foro.
**Entrega:** antes del próximo encuentro.

El punto 3 es el que más nos interesa: reconocer por adelantado los límites de lo que los
datos van a permitir afirmar.

### Material de la clase

| Material | Descripción |
|---|---|
| `Presentación Clase 2.pdf` | Diapositivas 1 a 16 |
| `Clase_2.ipynb` | Notebook práctica, para abrir en Google Colab |
| `Clase_2_opcional.ipynb` | Ampliación: desagregación dasimétrica y zonificaciones irregulares |

### Bibliografía

- Olaya, V. *Sistemas de Información Geográfica*, capítulo 9.
- Openshaw, S. (1984). *The Modifiable Areal Unit Problem*. Geo Books.
- Robinson, W. S. (1950). "Ecological Correlations and the Behavior of Individuals".
  *American Sociological Review*, 15(3).
- Tobler, W. (1970). "A Computer Movie Simulating Urban Growth in the Detroit Region".
  *Economic Geography*, 46.
