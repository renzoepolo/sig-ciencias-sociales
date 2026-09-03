"""
Utilidades comunes del curso de Sistemas de Información Geográfica.
Especialización en Ciencias Sociales Computacionales — UNAB.

Este módulo concentra tres cosas que antes se repetían en cada notebook:

1. `cargar()`      — descarga de datos con caché, desde URLs estables.
2. `chequear_*()`  — comprobaciones explícitas antes de interpretar un resultado.
3. `mapa_*()`      — armado de mapas, para no repetir 30 líneas de estilo por clase.

Uso en Colab (ya incluido en la celda de setup de cada notebook):

    !wget -q -O sig_utils.py {URL_BASE}/sig_utils.py
    from sig_utils import cargar, chequear_crs, mapa_capas, mapa_coropletico
"""

from __future__ import annotations

import os
import pathlib
import urllib.request

__all__ = [
    "URL_BASE",
    "CATALOGO",
    "cargar",
    "ruta_local",
    "chequear_crs",
    "chequear_columnas",
    "resumen",
    "mapa_capas",
    "mapa_coropletico",
    "ESTILOS",
    "CRS_ARGENTINA",
    "grilla",
]

# --------------------------------------------------------------------------
# Configuración
# --------------------------------------------------------------------------

# Repositorio público de datos del curso.
# Se puede sobreescribir con la variable de entorno SIG_URL_BASE, útil para
# probar contra una copia local o una bifurcación del repositorio.
URL_BASE = os.environ.get(
    "SIG_URL_BASE",
    "https://raw.githubusercontent.com/renzoepolo/sig-ciencias-sociales/main/datos",
)

CACHE = pathlib.Path(os.environ.get("SIG_CACHE", "datos/cache"))


# Sistemas de referencia usados a lo largo del curso.
# Las fajas Gauss-Krüger de POSGAR 2007 cubren el territorio continental
# argentino de oeste a este; cada una es válida en una franja de 3° de longitud.
CRS_ARGENTINA = {
    "geograficas": "EPSG:4326",       # WGS 84 — grados. NO sirve para medir.
    "web": "EPSG:3857",               # Web Mercator — solo para mapas base.
    "posgar_faja_1": "EPSG:5343",     # oeste                    (72°O – 69°O)
    "posgar_faja_2": "EPSG:5344",
    "posgar_faja_3": "EPSG:5345",
    "posgar_faja_4": "EPSG:5346",
    "posgar_faja_5": "EPSG:5347",     # Buenos Aires, Pergamino  (60°O – 57°O)
    "posgar_faja_6": "EPSG:5348",
    "posgar_faja_7": "EPSG:5349",     # este
    # Para análisis que abarcan todo el país y no entran en una sola faja.
    # Ojo: EPSG:5340 es POSGAR 2007 GEOGRÁFICO (grados), no sirve para medir.
    "sudamerica_equivalente": "ESRI:102033",  # Albers — conserva superficies
    "sudamerica_equidistante": "ESRI:102032", # cónica — conserva distancias
}


# --------------------------------------------------------------------------
# Catálogo de datos
# --------------------------------------------------------------------------
# Cada entrada declara el CRS de origen, para que ninguna notebook tenga que
# adivinarlo ni asignarlo "porque sabemos que viene de tal lado".

CATALOGO = {
    # Clase 1
    "paises": dict(
        archivo="ne_110m_admin_0_countries.gpkg",
        crs="EPSG:4326",
        fuente="Natural Earth 5.1.1, escala 1:110m",
        descripcion="Países del mundo con población estimada y continente.",
    ),
    "provincias": dict(
        archivo="provincias_arg.gpkg",
        crs="EPSG:4326",
        fuente="IGN — Instituto Geográfico Nacional",
        descripcion="Provincias de Argentina con población del Censo 2022.",
    ),
    "ruta40": dict(
        archivo="ruta_nacional_40.gpkg",
        crs="EPSG:4326",
        fuente="IGN — Red vial nacional",
        descripcion="Traza de la Ruta Nacional 40.",
    ),
    "escuelas": dict(
        archivo="escuelas_primarias.gpkg",
        crs="EPSG:4326",
        fuente="Ministerio de Educación — Padrón de establecimientos",
        descripcion="Escuelas primarias de educación común.",
    ),
    # Clase 2
    "grilla_cuadrados": dict(
        archivo="grilla_cuadrados.gpkg", crs="EPSG:5347",
        fuente="Elaboración propia", descripcion="Grilla regular cuadrada.",
    ),
    "grilla_hexagonos": dict(
        archivo="grilla_hexagonos.gpkg", crs="EPSG:5347",
        fuente="Elaboración propia", descripcion="Grilla regular hexagonal.",
    ),
    # Clase 3 — copias congeladas de las tres fuentes en vivo
    "poblaciones_departamentos": dict(
        archivo="poblaciones_departamentos_2022.csv", crs=None,
        fuente="poblaciones.org — Censo 2022 (copia literal del portal)",
        descripcion="527 departamentos con población, hogares y geometría en WKT. Sin CRS declarado.",
    ),
    "ign_salud": dict(
        archivo="ign_salud.gpkg", crs="EPSG:4326",
        fuente="IGN — WFS, capa de edificios de salud (copia congelada)",
        descripcion="Establecimientos de salud del país, tal como los devuelve el geoservicio.",
    ),
    "osm_amenities": dict(
        archivo="osm_amenities_barrios.gpkg", crs="EPSG:4326",
        fuente="OpenStreetMap vía OSMnx (copia congelada)",
        descripcion="Elementos con etiqueta amenity en Recoleta y Villa Lugano.",
    ),
    "osm_barrios": dict(
        archivo="osm_barrios_limites.gpkg", crs="EPSG:4326",
        fuente="OpenStreetMap vía OSMnx (copia congelada)",
        descripcion="Contorno de los dos barrios consultados.",
    ),
    # Clase 4 — proyecciones
    "continentes": dict(
        archivo="ne_110m_land.gpkg", crs="EPSG:4326",
        fuente="Natural Earth 5.1.1", descripcion="Masas continentales.",
    ),
    "canevas": dict(
        archivo="canevas.gpkg", crs="EPSG:4326",
        fuente="Elaboración propia", descripcion="Red de paralelos y meridianos.",
    ),
    "indicatriz": dict(
        archivo="indicatriz_tissot.gpkg", crs="EPSG:4326",
        fuente="Elaboración propia",
        descripcion="Círculos de Tissot para visualizar deformación.",
    ),
    # Clase 5 y 7
    "departamentos_nbi": dict(
        archivo="indicadores_hogares_departamentos_2022.gpkg", crs="EPSG:4326",
        fuente="INDEC — Censo Nacional de Población, Hogares y Viviendas 2022",
        descripcion="527 departamentos con indicadores de hogares.",
    ),
    "departamentos_nbi_2010_2022": dict(
        archivo="censo_nbi_2010-2022.gpkg", crs="EPSG:4326",
        fuente="INDEC — Censos 2010 y 2022",
        descripcion="NBI por departamento en ambos censos.",
    ),
    # Clase 6 — copias congeladas del WFS de Pergamino
    "pergamino_barrios": dict(
        archivo="pergamino_barrios.gpkg", crs="EPSG:5347",
        fuente="IDE Municipalidad de Pergamino (copia congelada)",
        descripcion="Límites de barrios del partido de Pergamino.",
    ),
    "pergamino_centros_salud": dict(
        archivo="pergamino_centros_salud.gpkg", crs="EPSG:4326",
        fuente="IDE Municipalidad de Pergamino (copia congelada)",
        descripcion="Centros de atención sanitaria, ya geocodificados.",
    ),
    "pergamino_farmacias": dict(
        archivo="pergamino_farmacias.gpkg", crs="EPSG:4326",
        fuente="IDE Municipalidad de Pergamino (copia congelada)",
        descripcion="Farmacias del partido.",
    ),
    "pergamino_rutas_ors": dict(
        archivo="pergamino_rutas_ors.csv", crs=None,
        fuente="OpenRouteService (resultado precalculado)",
        descripcion="Distancia y duración por calle de cada barrio a su centro de salud más cercano.",
    ),
    # Clase 8
    "cordoba_radios": dict(
        archivo="cordoba_censo.gpkg", crs="EPSG:5347",
        fuente="INDEC — Censo 2010, radios censales de Córdoba",
        descripcion="Radios censales con variables socioeconómicas.",
    ),
}


# --------------------------------------------------------------------------
# Carga de datos
# --------------------------------------------------------------------------

def ruta_local(nombre: str) -> pathlib.Path:
    """Devuelve la ruta en caché del dataset, sin descargarlo."""
    if nombre not in CATALOGO:
        disponibles = ", ".join(sorted(CATALOGO))
        raise KeyError(f"'{nombre}' no está en el catálogo. Disponibles: {disponibles}")
    return CACHE / CATALOGO[nombre]["archivo"]


def cargar(nombre: str, mostrar_ficha: bool = True):
    """
    Descarga (una sola vez) y abre un dataset del curso.

    A diferencia de leer un archivo suelto, esto garantiza tres cosas:
    el archivo viene de una URL estable, el CRS queda declarado explícitamente,
    y la segunda ejecución de la celda no vuelve a descargar nada.

    Devuelve un GeoDataFrame, o un DataFrame si el archivo es un CSV sin geometría.
    """
    import geopandas as gpd
    import pandas as pd

    entrada = CATALOGO[nombre] if nombre in CATALOGO else None
    if entrada is None:
        disponibles = ", ".join(sorted(CATALOGO))
        raise KeyError(f"'{nombre}' no está en el catálogo. Disponibles: {disponibles}")

    destino = ruta_local(nombre)
    destino.parent.mkdir(parents=True, exist_ok=True)

    if not destino.exists():
        url = f"{URL_BASE}/{entrada['archivo']}"
        print(f"Descargando {entrada['archivo']} …")
        urllib.request.urlretrieve(url, destino)
    else:
        print(f"Usando copia en caché: {destino}")

    if destino.suffix == ".csv":
        datos = pd.read_csv(destino)
    else:
        datos = gpd.read_file(destino)
        # El CRS del catálogo es la referencia. Si el archivo no lo trae,
        # se asigna; si lo trae distinto, se avisa en lugar de sobreescribir.
        declarado = entrada["crs"]
        if declarado is not None:
            if datos.crs is None:
                datos = datos.set_crs(declarado)
            elif datos.crs.to_string() != declarado:
                print(
                    f"  Atención: el archivo declara {datos.crs.to_string()} "
                    f"y el catálogo esperaba {declarado}."
                )

    if mostrar_ficha:
        print(f"  Fuente: {entrada['fuente']}")
        print(f"  {entrada['descripcion']}")
        print(f"  Filas: {len(datos)}", end="")
        if hasattr(datos, "crs"):
            print(f" | CRS: {datos.crs.to_string() if datos.crs else 'sin definir'}")
        else:
            print()

    return datos


# --------------------------------------------------------------------------
# Comprobaciones
# --------------------------------------------------------------------------

def chequear_crs(gdf, proyectado: bool | None = None, nombre: str = "la capa"):
    """
    Verifica el sistema de referencia antes de una operación que dependa de él.

    `proyectado=True`  exige unidades métricas (para áreas, distancias, buffers).
    `proyectado=False` exige coordenadas geográficas (para Folium, por ejemplo).

    Falla con un mensaje explícito en vez de producir un número sin sentido.
    """
    if gdf.crs is None:
        raise ValueError(
            f"{nombre} no tiene CRS definido. Asignalo con .set_crs() si sabés "
            f"cuál es, o revisá la fuente. Nunca uses .to_crs() sobre una capa "
            f"sin CRS: no hay desde dónde transformar."
        )

    if proyectado is True and not gdf.crs.is_projected:
        raise ValueError(
            f"{nombre} está en {gdf.crs.to_string()}, que es un CRS geográfico "
            f"(grados). Medir áreas o distancias acá da resultados incorrectos. "
            f"Reproyectá primero, por ejemplo a {CRS_ARGENTINA['posgar_faja_5']}."
        )

    if proyectado is False and gdf.crs.is_projected:
        raise ValueError(
            f"{nombre} está proyectada ({gdf.crs.to_string()}) y acá se esperan "
            f"coordenadas geográficas. Usá .to_crs('EPSG:4326')."
        )

    unidad = gdf.crs.axis_info[0].unit_name if gdf.crs.axis_info else "?"
    print(f"✓ {nombre}: {gdf.crs.to_string()} — unidades en {unidad}")
    return True


def chequear_columnas(df, columnas, nombre: str = "la tabla"):
    """Verifica que existan las columnas esperadas, y avisa cuáles faltan."""
    faltantes = [c for c in columnas if c not in df.columns]
    if faltantes:
        raise KeyError(
            f"A {nombre} le faltan las columnas {faltantes}. "
            f"Tiene: {list(df.columns)}"
        )
    print(f"✓ {nombre}: están las {len(columnas)} columnas esperadas")
    return True


def resumen(gdf, columnas=None, nombre: str = "la capa"):
    """Resumen breve para la celda de comprobación: filas, CRS, nulos, rangos."""
    print(f"— {nombre} —")
    print(f"  Filas: {len(gdf)}")
    if hasattr(gdf, "crs"):
        print(f"  CRS: {gdf.crs.to_string() if gdf.crs is not None else 'sin definir'}")
    if hasattr(gdf, "geometry"):
        vacias = int(gdf.geometry.is_empty.sum())
        nulas = int(gdf.geometry.isna().sum())
        print(f"  Geometrías vacías: {vacias} | nulas: {nulas}")
        print(f"  Tipos: {sorted(gdf.geom_type.dropna().unique())}")
    for col in columnas or []:
        if col in gdf.columns:
            serie = gdf[col]
            if serie.dtype.kind in "if":
                print(
                    f"  {col}: {serie.min():.2f} – {serie.max():.2f} "
                    f"(media {serie.mean():.2f}, {serie.isna().sum()} nulos)"
                )
            else:
                print(f"  {col}: {serie.nunique()} valores distintos, {serie.isna().sum()} nulos")


# --------------------------------------------------------------------------
# Mapas
# --------------------------------------------------------------------------

# Estilos con nombre, para no repetir diccionarios de 6 claves en cada celda.
ESTILOS = {
    "contorno": dict(fill=False, color="black", weight=1),
    "area": dict(stroke=True, weight=1, color="orange",
                 fillColor="orange", fillOpacity=0.3),
    "punto_rojo": dict(stroke=True, weight=1, color="red",
                       fillColor="red", fillOpacity=1),
    "punto_negro": dict(stroke=True, weight=1, color="black",
                        fillColor="black", fillOpacity=0.6),
}


def mapa_capas(capas, centro=None, zoom=12, tiles="CartoDB.Positron"):
    """
    Arma un mapa Folium con varias capas y control de capas.

    `capas` es una lista de diccionarios:
        [{"gdf": gdf_barrios, "nombre": "Barrios", "estilo": "contorno",
          "tooltip": ["nombre"]}, ...]

    `estilo` puede ser el nombre de una entrada de ESTILOS o un diccionario.
    Todas las capas se reproyectan a geográficas: Folium trabaja en EPSG:4326.
    """
    import folium

    if not capas:
        raise ValueError("Hace falta al menos una capa.")

    if centro is None:
        primera = capas[0]["gdf"].to_crs("EPSG:4326")
        centroide = primera.union_all().centroid
        centro = [centroide.y, centroide.x]

    mapa = folium.Map(location=centro, zoom_start=zoom, tiles=tiles)

    for capa in capas:
        gdf = capa["gdf"]
        if gdf.crs is None:
            raise ValueError(
                f"La capa '{capa.get('nombre', '?')}' no tiene CRS. "
                f"Folium no puede ubicarla."
            )
        gdf = gdf.to_crs("EPSG:4326")

        estilo = capa.get("estilo", "contorno")
        if isinstance(estilo, str):
            estilo = ESTILOS[estilo]

        kwargs = dict(m=mapa, name=capa.get("nombre", "capa"), style_kwds=estilo)

        if capa.get("tooltip"):
            kwargs["tooltip"] = capa["tooltip"]
            if capa.get("alias"):
                kwargs["tooltip_kwds"] = {"aliases": capa["alias"]}
        else:
            kwargs["tooltip"] = False

        for extra in ("column", "cmap", "scheme", "k", "legend"):
            if extra in capa:
                kwargs[extra] = capa[extra]

        gdf.explore(**kwargs)

    folium.LayerControl().add_to(mapa)
    return mapa


def mapa_coropletico(gdf, columna, titulo=None, cmap="Spectral_r",
                     scheme="FisherJenks", k=7, figsize=(7, 9),
                     leyenda_titulo=None, ax=None):
    """
    Mapa de coropletas con la leyenda ya resuelta fuera del eje.

    Reemplaza el bloque de ocho líneas de reposicionamiento de leyenda que
    aparecía repetido en las clases 5, 7 y 8.
    """
    import matplotlib.pyplot as plt

    creado_aca = ax is None
    if creado_aca:
        _, ax = plt.subplots(figsize=figsize)

    gdf.plot(column=columna, scheme=scheme, k=k, cmap=cmap,
             legend=True, ax=ax, edgecolor="white", linewidth=0.2)

    ax.set_title(titulo or columna)
    ax.set_axis_off()

    leyenda = ax.get_legend()
    if leyenda is not None:
        leyenda.set_bbox_to_anchor((1.02, 1.0))
        leyenda.set_title(leyenda_titulo or columna)
        leyenda._legend_box.align = "left"

    if creado_aca:
        plt.tight_layout()

    return ax


# --------------------------------------------------------------------------
# Grillas regulares
# --------------------------------------------------------------------------

def grilla(zona, lado_km: float, forma: str = "cuadrado",
           desplazamiento: float = 0.0, crs_metrico: str = "ESRI:102033"):
    """
    Genera una grilla regular que cubre `zona`, en celdas de área comparable.

    Sirve para estudiar el problema de la unidad de área modificable (MAUP),
    donde importa poder cambiar UNA cosa por vez:

    - `lado_km` distinto, misma forma  -> efecto de AGREGACIÓN (escala)
    - misma área, `forma` distinta     -> efecto de ZONIFICACIÓN
    - misma área y forma, `desplazamiento` distinto -> zonificación en estado puro

    `desplazamiento` se expresa en fracción de celda (0.5 = media celda).
    Los hexágonos se dimensionan para tener la misma superficie que el cuadrado
    de `lado_km`, de modo que las dos grillas sean comparables.

    Devuelve un GeoDataFrame en el CRS de `zona`, recortado a su extensión.
    """
    import geopandas as gpd
    import numpy as np
    from shapely.geometry import Polygon

    crs_original = zona.crs
    if crs_original is None:
        raise ValueError("La zona no tiene CRS definido.")

    zona_m = zona.to_crs(crs_metrico)
    minx, miny, maxx, maxy = zona_m.total_bounds
    lado = lado_km * 1000.0

    celdas = []
    if forma == "cuadrado":
        dx = dy = lado
        offset_x = offset_y = desplazamiento * lado
        xs = np.arange(minx - dx - offset_x, maxx + dx, dx)
        ys = np.arange(miny - dy - offset_y, maxy + dy, dy)
        for x in xs:
            for y in ys:
                celdas.append(Polygon([(x, y), (x + dx, y),
                                       (x + dx, y + dy), (x, y + dy)]))

    elif forma == "hexagono":
        # Hexágono regular de la misma área que el cuadrado de lado `lado`:
        # area = 3*sqrt(3)/2 * r^2  ->  r = sqrt(2*area / (3*sqrt(3)))
        area = lado ** 2
        r = np.sqrt(2 * area / (3 * np.sqrt(3)))
        dx = 1.5 * r                      # separación horizontal entre centros
        dy = np.sqrt(3) * r               # separación vertical
        offset_x = desplazamiento * dx
        offset_y = desplazamiento * dy
        col = 0
        x = minx - dx - offset_x
        while x < maxx + dx:
            desfase = 0 if col % 2 == 0 else dy / 2
            y = miny - dy - offset_y + desfase
            while y < maxy + dy:
                celdas.append(Polygon([
                    (x + r * np.cos(a), y + r * np.sin(a))
                    for a in np.linspace(0, 2 * np.pi, 7)[:-1]
                ]))
                y += dy
            x += dx
            col += 1
    else:
        raise ValueError("forma debe ser 'cuadrado' o 'hexagono'")

    g = gpd.GeoDataFrame({"celda_id": range(len(celdas))},
                         geometry=celdas, crs=crs_metrico)

    # Nos quedamos solo con las celdas que tocan la zona de estudio
    envolvente = zona_m.union_all()
    g = g[g.intersects(envolvente)].reset_index(drop=True)
    g["celda_id"] = range(len(g))
    g["area_km2"] = g.area / 1e6

    return g.to_crs(crs_original)
