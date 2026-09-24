# Trabajo final

**Sistemas de Información Geográfica**
Especialización en Ciencias Sociales Computacionales — Universidad Nacional Guillermo Brown

---

## La consigna, en una línea

Elegí una **pregunta territorial** vinculada a tu investigación o a un tema que te interese, y
respondela construyendo variables territoriales a partir de **datos abiertos**.

## El formato

Una **notebook de Google Colab autocontenida**, individual, que **corra de principio a fin en
un entorno limpio**. No hay informe aparte: el texto va en celdas de markdown intercaladas con
el código, como las notebooks del curso.

"Autocontenida" quiere decir que otra persona puede abrirla, apretar *Ejecutar todo* y obtener
los mismos resultados. En la práctica: nada de rutas de tu computadora, nada de archivos que
haya que subir a mano. Los datos se bajan desde su URL o se leen de un repositorio o una
carpeta de Drive compartida.

**Extensión sugerida:** entre 40 y 80 celdas. No se evalúa el largo.

---

## Qué tiene que tener

### 1. Pregunta y unidad de análisis

La pregunta va escrita, al principio, y empieza por **"¿Dónde…?"** o **"¿Qué diferencia hay
entre…?"**. Tiene que ser una pregunta que el territorio pueda contestar.

Declarás la **unidad de análisis** —radio censal, fracción, departamento, barrio, localidad,
provincia— y por qué elegiste ésa. Si la elegiste porque es la única para la que hay datos,
decilo: es una razón legítima y conviene que quede escrita.

### 2. Ficha de datos

**Al menos dos fuentes abiertas distintas.** Algunas posibles:

| Fuente | Qué tiene |
|---|---|
| [poblaciones.org](https://poblaciones.org) | Censos 2010 y 2022 por departamento y por radio, con geometría |
| [datos.gob.ar](https://datos.gob.ar) | Portal nacional de datos abiertos |
| [IGN](https://www.ign.gob.ar/nuestrasactividades/geografia/datosargentina) | Capas base del país: límites, red vial, hidrografía, equipamiento. Geoservicios WMS y WFS |
| [INDEC](https://www.indec.gob.ar) | Censo, EPH, cartografía censal |
| IDE provinciales y municipales | Parcelas, usos del suelo, equipamiento urbano, obras |
| [OpenStreetMap](https://www.openstreetmap.org) | Equipamiento, red vial, usos del suelo — vía OSMnx |
| Portales locales (p. ej. [BA Data](https://data.buenosaires.gob.ar)) | Datos de la jurisdicción |

De **cada** fuente informás: organismo, fecha o período, cobertura territorial, unidad de
análisis, CRS declarado, licencia y **limitaciones conocidas**.

Esa última columna es la que más se saltea y la que más importa. Si usás OSM, la limitación
conocida es la que medimos en la Clase 6.

### 3. Preparación

Carga de los datos, unión por clave o espacial, declaración y reproyección del sistema de
coordenadas, limpieza de lo que haga falta.

Con **al menos una comprobación explícita** de que cada operación salió bien: cantidad de
filas, registros sin coincidencia, nulos en la geometría, rango de los valores. Las celdas ✅
de las notebooks del curso son el modelo.

### 4. Al menos dos variables territoriales construidas

Con las técnicas del curso. Por ejemplo:

- conteo o agregación de una capa dentro de las unidades de otra (`sjoin` + `groupby`);
- porcentaje de superficie cubierta por un área de influencia (`buffer` + `intersection`);
- distancia al equipamiento más cercano (`sjoin_nearest`);
- densidad por km² o tasa sobre población;
- cambio de unidad de análisis, por pertenencia o por ponderación de área;
- un índice compuesto a partir de variables normalizadas;
- la categoría de conglomerado de un análisis LISA.

**La unidad de medida va en el nombre de la columna:** `distancia_m`, `densidad_por_km2`,
`cobertura_500m_perc`.

### 5. Un análisis

Al menos uno, y elegido porque responde tu pregunta —no porque lo vimos en clase:

- comparación de conteo / porcentaje / densidad sobre la misma variable;
- comparación de criterios de clasificación y su efecto sobre la lectura;
- autocorrelación espacial: I de Moran y LISA, con su interpretación;
- comparación entre dos unidades territoriales o entre dos momentos.

### 6. Cartografía

**Al menos dos mapas terminados** —título, leyenda con nombre, fuente, método de clasificación
declarado— y **al menos un gráfico no cartográfico**: histograma, barras, dispersión. No todo
lo que se sabe de un territorio se ve mejor en un mapa.

### 7. Limitaciones y qué no se puede afirmar

Una sección propia, al final, que discuta lo que corresponda de lo que vimos:

- **MAUP**: ¿el resultado cambiaría con otra división territorial?
- **Falacia ecológica**: ¿estás afirmando algo sobre personas a partir de datos de áreas?
- **Sesgos de la fuente**: ¿el dato falta al azar, o falta donde falta por una razón?
- **Efecto de borde**: ¿lo que pasa fuera de tu zona de estudio afecta el resultado?
- **Asociación y causa**: lo que encontraste, ¿es un patrón o una explicación?

Es la sección más corta y la que más pesa. Un trabajo que encuentra poco pero sabe qué no
puede concluir está mejor que uno que concluye de más.

### 8. Uso de IA

Si usaste un asistente, lo declarás con el formato del curso: **el prompt, la salida sin
editar, la verificación contra los datos y el veredicto**. Si no lo usaste, también se declara.

Usar IA no resta. Usarla sin verificar, sí.

---

## Entrega

- **Enlace** a la notebook: Colab compartido con permiso de lectura, o un repositorio.
- **Por el aula virtual.**
- **Individual.**
- **Fecha:** la que se anuncie en el aula.

---

## Rúbrica

| Criterio | Puntos |
|---|---|
| Pregunta territorial clara y unidad de análisis justificada | 10 |
| Fuentes abiertas: dos o más, con ficha completa y limitaciones declaradas | 15 |
| Preparación correcta: CRS declarado y reproyectado, uniones verificadas | 15 |
| Dos o más variables territoriales bien construidas, con la unidad en el nombre | 25 |
| Análisis pertinente e **interpretado**, no sólo ejecutado | 15 |
| Cartografía: dos mapas terminados y un gráfico | 10 |
| Limitaciones y honestidad sobre lo que el análisis no permite afirmar | 10 |

**Se aprueba con 60 puntos**, con dos condiciones:

1. **La notebook corre completa.** Una notebook que se cuelga en la celda 12 no se puede
   evaluar.
2. **La sección de limitaciones existe.** Un trabajo técnicamente impecable que afirme una
   relación causal sin diseño que la sostenga no aprueba ese criterio, y son diez puntos.

---

## Tres ejemplos de pregunta

No son consignas: son la forma que tiene que tener una pregunta que se puede responder.

> **¿Qué localidades de mi provincia quedan a más de 30 minutos de un hospital con
> internación?** — Unidad: localidad. Fuentes: IGN (localidades y red vial) + padrón
> provincial de establecimientos. Variables: distancia por red, tiempo de viaje.

> **¿Dónde se concentran los hogares sin cloaca, y esa concentración coincide con la de los
> hogares sin agua de red?** — Unidad: departamento o radio. Fuente: Censo 2022 vía
> poblaciones.org. Variables: porcentajes, conglomerados LISA.

> **¿Los barrios populares de mi municipio tienen menos equipamiento educativo por habitante
> que el resto?** — Unidad: barrio o radio. Fuentes: RENABAP + padrón educativo + censo.
> Variables: escuelas por cada 1.000 habitantes en edad escolar, distancia a la escuela más
> cercana.

---

## Consultas

En la Clase 7 dedicamos el comienzo a revisar las preguntas elegidas. Traé la tuya, aunque
esté a medio formular: es el momento más barato para cambiarla.
