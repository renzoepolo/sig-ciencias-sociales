# Formatos de archivo — material de clase

Los tres archivos de esta carpeta contienen **el mismo dato**: las 24
provincias argentinas con población y hogares del Censo 2022. Lo único que
cambia es el formato.

| Archivo | Formato | Cuántos archivos |
|---|---|---|
| `provincias.gpkg` | GeoPackage | 1 |
| `provincias.geojson` | GeoJSON | 1 |
| `provincias.shp` | Shapefile | **4**: `.shp`, `.shx`, `.dbf`, `.prj` |

## El Shapefile está deliberadamente sin corregir

El `provincias.shp` reproduce los dos defectos que el formato impone y que la
Clase 2 estudia:

1. **Nombres de campo cortados a diez caracteres.** `poblacion_total` quedó
   como `poblacion_` y `poblacion_por_km2` como `poblacio_1`, porque al
   truncarse chocaban entre sí.
2. **Codificación no declarada.** No se escribe el archivo `.cpg`, de modo que
   el contenido está en UTF-8 pero nada lo dice, y "Córdoba" se lee como
   "CÃ³rdoba" salvo que se pase `encoding="utf-8"` a mano.

**No uses estos archivos para analizar nada.** El dato limpio es el de
`datos/provincias_arg.gpkg`.
