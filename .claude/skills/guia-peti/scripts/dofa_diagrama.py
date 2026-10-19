"""Dibuja los diagramas DOFA del PETI como imágenes PNG.

Uso:
    python .claude/skills/guia-peti/scripts/dofa_diagrama.py <peti.md> <carpeta_salida>

Genera:
  - dofa_consolidada.png: matriz cruzada con factores y estrategias FO, DO, FA y DA (tablas "Matriz DOFA
    consolidada de TI" y "Estrategias derivadas de la matriz DOFA").
  - dofa_<dominio>.png: diagrama de cuatro cuadrantes por dominio (tablas "DOFA del dominio ...").
La altura de cada fila se ajusta al texto. Requiere PyMuPDF.
"""
import os
import re
import sys
import unicodedata

import pymupdf

AZUL = (0.20, 0.27, 0.49)
NARANJA = (0.91, 0.60, 0.20)
AZUL_CLARO = (0.86, 0.89, 0.95)
NARANJA_CLARO = (0.99, 0.91, 0.80)
GRIS = (0.96, 0.96, 0.96)
BLANCO, NEGRO = (1, 1, 1), (0.1, 0.1, 0.1)
_MEDIDA = pymupdf.open().new_page(width=2000, height=4000)
DOMINIOS = ["Estrategia de TI", "Gobierno de TI", "Información", "Sistemas de información", "Infraestructura de TI",
            "Uso y apropiación", "Seguridad de la información"]


def slug(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]+", "_", "".join(c for c in s if unicodedata.category(c) != "Mn")).strip("_")


def tabla(texto, titulo):
    i = texto.index(f"Tabla: {titulo}")
    filas = []
    for linea in texto[i:].splitlines()[1:]:
        if linea.startswith("|"):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", c or "-") for c in celdas):
                filas.append(celdas)
        elif filas:
            break
    return filas[1:]


def items_numerados(celda):
    celda = celda.replace("**", "")
    celda = re.sub(r"^\s*(Fortalezas|Debilidades|Oportunidades|Amenazas):\s*", "", celda)
    return [p.strip() for p in re.split(r"\s(?=[FDOA](?:-[A-Z]{1,2})?\d+\.\s)", " " + celda) if p.strip()]


def vinetas(celda):
    """'**Fortalezas:** a; b; c' -> ["- a", "- b", "- c"] (sin partir los ';' dentro de paréntesis)."""
    celda = re.sub(r"^\*\*[^*]+\*\*\s*", "", celda)
    partes, nivel, actual = [], 0, ""
    for ch in celda:
        nivel += ch == "("
        nivel -= ch == ")"
        if ch == ";" and nivel == 0:
            partes.append(actual.strip())
            actual = ""
        else:
            actual += ch
    partes.append(actual.strip())
    return ["- " + p[0].upper() + p[1:] for p in partes if p]


def alto_texto(texto, ancho, tam, fuente="helv"):
    sobra = _MEDIDA.insert_textbox(pymupdf.Rect(0, 0, ancho, 4000), texto, fontsize=tam, fontname=fuente,
                                   lineheight=1.15)
    return 4000 - sobra


def caja(pag, r, texto, fondo, color, tam, fuente="helv", centrado=False):
    pag.draw_rect(r, color=(0.75, 0.75, 0.78), fill=fondo, width=0.6)
    interior = r + (5, 4, -5, -2)
    alinear = pymupdf.TEXT_ALIGN_CENTER if centrado else pymupdf.TEXT_ALIGN_LEFT
    desplazar = 0
    if centrado:
        desplazar = max(0, (interior.height - alto_texto(texto, interior.width, tam, fuente)) / 2)
    pag.insert_textbox(interior + (0, desplazar, 0, desplazar), texto, fontsize=tam, fontname=fuente, color=color,
                       align=alinear, lineheight=1.15)


def consolidada(texto, salida):
    cons = tabla(texto, "Matriz DOFA consolidada de TI")
    F, D = items_numerados(cons[0][1]), items_numerados(cons[0][2])
    O, A = items_numerados(cons[1][1]), items_numerados(cons[1][2])
    grupos = {"FO": [], "DO": [], "FA": [], "DA": []}
    for tipo, e, factores, proyectos in tabla(texto, "Estrategias derivadas de la matriz DOFA"):
        grupos[tipo].append(f"{tipo}{len(grupos[tipo]) + 1}. {e} ({factores}). Proyectos: {proyectos}.")
    ancho, m, c0, tam = 470, 8, 92, 7.5
    anchos = [c0, (ancho - 2 * m - c0) / 2, (ancho - 2 * m - c0) / 2]
    x = [m, m + anchos[0], m + anchos[0] + anchos[1], ancho - m]
    celdas = [
        [("OPORTUNIDADES (externas)\n\n" + "\n".join(O), AZUL_CLARO),
         ("Estrategias FO: usar las fortalezas para aprovechar las oportunidades\n\n" + "\n\n".join(grupos["FO"]), GRIS),
         ("Estrategias DO: superar las debilidades aprovechando las oportunidades\n\n" + "\n\n".join(grupos["DO"]), GRIS)],
        [("AMENAZAS (externas)\n\n" + "\n".join(A), NARANJA_CLARO),
         ("Estrategias FA: usar las fortalezas para reducir las amenazas\n\n" + "\n\n".join(grupos["FA"]), GRIS),
         ("Estrategias DA: reducir las debilidades y evitar las amenazas\n\n" + "\n\n".join(grupos["DA"]), GRIS)],
    ]
    h_fact = max(alto_texto("\n".join(F), anchos[1] - 10, tam), alto_texto("\n".join(D), anchos[2] - 10, tam)) + 18
    altos = [max(alto_texto(t, anchos[j] - 10, tam if j else 7) for j, (t, _) in enumerate(fila)) + 18 for fila in celdas]
    y = [m, m + 26, m + 26 + h_fact, m + 26 + h_fact + altos[0], m + 26 + h_fact + altos[0] + altos[1]]
    doc = pymupdf.open()
    pag = doc.new_page(width=ancho, height=y[-1] + m)
    caja(pag, pymupdf.Rect(x[0], y[0], x[1], y[1]), "Matriz DOFA de TI", AZUL, BLANCO, 9, "hebo", True)
    caja(pag, pymupdf.Rect(x[1], y[0], x[2], y[1]), "FORTALEZAS (internas)", AZUL, BLANCO, 9, "hebo", True)
    caja(pag, pymupdf.Rect(x[2], y[0], x[3], y[1]), "DEBILIDADES (internas)", NARANJA, BLANCO, 9, "hebo", True)
    caja(pag, pymupdf.Rect(x[0], y[1], x[1], y[2]), "Factores internos", GRIS, NEGRO, 8, "hebo", True)
    caja(pag, pymupdf.Rect(x[1], y[1], x[2], y[2]), "\n".join(F), AZUL_CLARO, NEGRO, tam)
    caja(pag, pymupdf.Rect(x[2], y[1], x[3], y[2]), "\n".join(D), NARANJA_CLARO, NEGRO, tam)
    for i, fila in enumerate(celdas):
        for j, (t, fondo) in enumerate(fila):
            caja(pag, pymupdf.Rect(x[j], y[2 + i], x[j + 1], y[3 + i]), t, fondo, NEGRO, tam if j else 7)
    pag.get_pixmap(dpi=220).save(salida)


def dominio(texto, nombre, salida):
    filas = tabla(texto, f"DOFA del dominio {nombre}")
    cuadrantes = [("FORTALEZAS", vinetas(filas[0][1]), AZUL, AZUL_CLARO),
                  ("DEBILIDADES", vinetas(filas[0][2]), NARANJA, NARANJA_CLARO),
                  ("OPORTUNIDADES", vinetas(filas[1][1]), AZUL, AZUL_CLARO),
                  ("AMENAZAS", vinetas(filas[1][2]), NARANJA, NARANJA_CLARO)]
    ancho, m, tam, alto_tit = 470, 8, 7.5, 20
    col = (ancho - 2 * m - 6) / 2
    doc = pymupdf.open()
    altos = []
    for k in (0, 2):
        altos.append(max(alto_texto("\n".join(cuadrantes[k + j][1]), col - 10, tam) for j in (0, 1)) + 18)
    alto = m + 24 + 2 * (alto_tit + 6) + sum(altos) + 6 + m
    pag = doc.new_page(width=ancho, height=alto)
    caja(pag, pymupdf.Rect(m, m, ancho - m, m + 20), f"DOFA del dominio {nombre}", AZUL, BLANCO, 9.5, "hebo", True)
    y = m + 24
    for fila in (0, 1):
        for j in (0, 1):
            titulo, lineas, fuerte, suave = cuadrantes[fila * 2 + j]
            x0 = m + j * (col + 6)
            origen = "internas" if fila == 0 else "externas"
            caja(pag, pymupdf.Rect(x0, y, x0 + col, y + alto_tit), f"{titulo} ({origen})", fuerte, BLANCO, 8.5, "hebo", True)
            caja(pag, pymupdf.Rect(x0, y + alto_tit, x0 + col, y + alto_tit + altos[fila]), "\n".join(lineas), suave, NEGRO, tam)
        y += alto_tit + altos[fila] + 6
    pag.get_pixmap(dpi=220).save(salida)



def general(texto, carpeta):
    """DOFA general en dos imágenes: factores internos (F y D) y externos (O y A), en dos columnas por cuadrante."""
    filas = tabla(texto, "Matriz DOFA general de TI")
    grupos = [("dofa_general_internos.png", [("FORTALEZAS (factores internos)", items_numerados(filas[0][1]), AZUL, AZUL_CLARO),
                                             ("DEBILIDADES (factores internos)", items_numerados(filas[0][2]), NARANJA, NARANJA_CLARO)]),
              ("dofa_general_externos.png", [("OPORTUNIDADES (factores externos)", items_numerados(filas[1][1]), AZUL, AZUL_CLARO),
                                             ("AMENAZAS (factores externos)", items_numerados(filas[1][2]), NARANJA, NARANJA_CLARO)])]
    ancho, m, tam, alto_tit, sep = 470, 8, 7.5, 20, 8
    col = (ancho - 2 * m - 4) / 2
    for nombre, cuadrantes in grupos:
        bloques = []
        for titulo, items, fuerte, suave in cuadrantes:
            items = [i.rstrip(".") + "." for i in items]
            # corte donde la altura acumulada llega a la mitad, para que las dos columnas queden parejas
            alturas = [alto_texto(i, col - 10, tam) for i in items]
            acumulado, mitad = 0, len(items)
            for k, h in enumerate(alturas):
                acumulado += h
                if acumulado >= sum(alturas) / 2:
                    mitad = k + 1
                    break
            partes = ["\n".join(items[:mitad]), "\n".join(items[mitad:])]
            alto = max(alto_texto(x, col - 10, tam) for x in partes) + 18
            bloques.append((titulo, partes, fuerte, suave, alto))
        total = m + sum(alto_tit + b[4] + sep for b in bloques) + m
        doc = pymupdf.open()
        pag = doc.new_page(width=ancho, height=total)
        y = m
        for titulo, partes, fuerte, suave, alto in bloques:
            caja(pag, pymupdf.Rect(m, y, ancho - m, y + alto_tit), titulo, fuerte, BLANCO, 9, "hebo", True)
            for j, parte in enumerate(partes):
                x0 = m + j * (col + 4)
                caja(pag, pymupdf.Rect(x0, y + alto_tit, x0 + col, y + alto_tit + alto), parte, suave, NEGRO, tam)
            y += alto_tit + alto + sep
        pag.get_pixmap(dpi=220).save(os.path.join(carpeta, nombre))


def texto_auxiliar(md):
    """Matrices DOFA por dominio (docs/dofa-por-dominio.md) con las citas convertidas a nombre de documento."""
    ruta = os.path.join(os.path.dirname(os.path.abspath(md)), "dofa-por-dominio.md")
    if not os.path.exists(ruta):
        return ""
    texto = open(ruta, encoding="utf8").read()
    registro = open(os.path.join(os.path.dirname(os.path.abspath(md)), "registro-de-evidencias.md"), encoding="utf8").read()
    bloque = registro.split("## Nombres de cita", 1)[1].split("\n## ", 1)[0]
    nombres = dict(re.findall(r"^\|\s*((?:PUB|INT|PRV)-\d{3})\s*\|\s*([^|]+?)\s*\|", bloque, re.M))
    texto = texto.replace("elaboración propia (INT-001)", "elaboración propia del equipo")
    return re.sub(r"(?:PUB|INT|PRV)-\d{3}", lambda m: nombres.get(m.group(0), m.group(0)), texto)


def generar(md, carpeta):
    texto = open(md, encoding="utf8").read() + "\n\n" + texto_auxiliar(md)
    os.makedirs(carpeta, exist_ok=True)
    consolidada(texto, os.path.join(carpeta, "dofa_consolidada.png"))
    general(texto, carpeta)
    if "--dominios" in sys.argv:  # diagramas por dominio: opcionales, el PETI ya no los usa
        for d in DOMINIOS:
            dominio(texto, d, os.path.join(carpeta, f"dofa_{slug(d)}.png"))
    print("Generados en", carpeta)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    generar(sys.argv[1], sys.argv[2])
