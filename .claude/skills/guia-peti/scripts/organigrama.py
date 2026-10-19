"""Dibuja el organigrama directivo de la organización con las áreas de TI resaltadas (PNG).

Uso:
    python .claude/skills/guia-peti/scripts/organigrama.py <salida.png>

Los datos salen del organigrama directivo publicado (septiembre de 2025); solo nombres de áreas,
nunca de personas. Requiere PyMuPDF (pip install pymupdf).
"""
import sys

import pymupdf

PRESIDENCIA = "Presidencia"
APOYO = ["G. Mercadeo y Experiencia", "Auditor Interno", "Oficial de Cumplimiento"]
# (vicepresidencia, [(unidad, tiene funciones de TI)])
AREAS = [
    [("Negocios", [(u, False) for u in ["G. Negocios Empresarial", "G. Negocios Retail", "G. Negocios Servicios",
                                        "G. Negocios Transporte", "G. Negocios Entidades Financieras",
                                        "G. Negocios Comercial", "G. PSP Adquirentes"]]),
     ("Desarrollo de Soluciones", [("G. Data Science", True), ("G. Producto (2)", False),
                                   ("G. Expansión de Nuevos Negocios", False),
                                   ("G. Desarrollo de Productos de Acceso", False),
                                   ("G. Transformación Digital", True), ("D. Desarrollo de Mercados", False),
                                   ("D. Desarrollo de Franquicias", False)]),
     ("Tecnología", [(u, True) for u in ["G. PMO", "G. Infraestructura, Seguridad y Operaciones", "G. Gobierno TI",
                                         "G. Ingeniería de Software", "G. Desarrollo de Acceso",
                                         "G. Arquitectura Empresarial", "D. Aplicaciones", "D. Implementaciones",
                                         "D. Desarrollo Canje"]]),
     ("Negocios Open Business", [("G. Open Finance y Data", True), ("G. Pagos Inmediatos", True)])],
    [("Secretaría General", []),
     ("Riesgo Integral y Cumplimiento", [("G. Seguridad de la Información", True), ("G. Riesgo y Continuidad", True)]),
     ("Finanzas y Servicios Corporativos", [(u, False) for u in ["G. Abastecimiento Estratégico",
                                                                 "G. Planeación y Finanzas", "G. Talento Humano",
                                                                 "G. Administrativa"]]),
     ("Operaciones", [(u, False) for u in ["G. Operaciones Comercios", "G. Operaciones Entidades Financieras",
                                           "G. Asignación de Clientes", "G. Facturación"]])],
]

AZUL = (0.20, 0.27, 0.49)       # vicepresidencias
NARANJA = (0.91, 0.60, 0.20)    # unidades con funciones de TI
GRIS = (0.86, 0.89, 0.95)       # demás unidades
LINEA = (0.55, 0.58, 0.65)
ANCHO, ALTO = 560, 640


_MEDIDA = pymupdf.open().new_page()


def caja(pag, r, texto, fondo, color_texto, tam, negrita=False):
    """Caja redondeada con el texto centrado en ambos ejes (reduce la letra si no cabe)."""
    pag.draw_rect(r, color=fondo, fill=fondo, radius=0.15)
    fuente = "hebo" if negrita else "helv"
    interior = r + (3, 1, -3, 0)
    for t in (tam, tam - 0.5, tam - 1, tam - 1.5, tam - 2):
        sobra = _MEDIDA.insert_textbox(pymupdf.Rect(0, 0, interior.width, interior.height), texto, fontsize=t,
                                       fontname=fuente, align=pymupdf.TEXT_ALIGN_CENTER)
        if sobra >= 0:
            pag.insert_textbox(interior + (0, sobra / 2, 0, sobra / 2), texto, fontsize=t, fontname=fuente,
                               color=color_texto, align=pymupdf.TEXT_ALIGN_CENTER)
            return


def dibujar(salida):
    doc = pymupdf.open()
    pag = doc.new_page(width=ANCHO, height=ALTO)
    m, col_w, gap = 14, 124, 10
    pres = pymupdf.Rect(ANCHO / 2 - 70, 12, ANCHO / 2 + 70, 36)
    caja(pag, pres, PRESIDENCIA, AZUL, (1, 1, 1), 10, True)
    # unidades de apoyo a la Presidencia
    for k, u in enumerate(APOYO):
        r = pymupdf.Rect(ANCHO - m - 118, 44 + k * 22, ANCHO - m, 62 + k * 22)
        caja(pag, r, u, GRIS, (0.1, 0.1, 0.1), 7)
        pag.draw_line((ANCHO / 2, (r.y0 + r.y1) / 2), (r.x0, (r.y0 + r.y1) / 2), color=LINEA, width=0.6)
    pag.draw_line((ANCHO / 2, 36), (ANCHO / 2, 120), color=LINEA, width=0.8)
    y = 120
    for n_fila, fila in enumerate(AREAS):
        alto_unidad, sep = 22, 4
        n_max = max(len(u) for _, u in fila)
        x_centros = [m + col_w / 2 + j * (col_w + gap) for j in range(4)]
        pag.draw_line((x_centros[0], y - 8), (x_centros[-1], y - 8), color=LINEA, width=0.8)
        for j, (vp, unidades) in enumerate(fila):
            x0 = m + j * (col_w + gap)
            pag.draw_line((x_centros[j], y - 8), (x_centros[j], y), color=LINEA, width=0.8)
            caja(pag, pymupdf.Rect(x0, y, x0 + col_w, y + 28), vp, AZUL, (1, 1, 1), 8.5, True)
            for k, (u, ti) in enumerate(unidades):
                yy = y + 34 + k * (alto_unidad + sep)
                caja(pag, pymupdf.Rect(x0 + 6, yy, x0 + col_w, yy + alto_unidad), u,
                     NARANJA if ti else GRIS, (1, 1, 1) if ti else (0.1, 0.1, 0.1), 7)
            if unidades:
                pag.draw_line((x0 + 3, y + 28), (x0 + 3, y + 34 + (len(unidades) - 1) * (alto_unidad + sep) + 11),
                              color=LINEA, width=0.6)
        siguiente = y + 34 + n_max * (alto_unidad + sep) + 22
        if n_fila < len(AREAS) - 1:
            pag.draw_line((ANCHO / 2, y - 8), (ANCHO / 2, siguiente - 8), color=LINEA, width=0.8)
        y = siguiente
    # leyenda
    ly = y - 6
    pag.draw_rect(pymupdf.Rect(m, ly, m + 14, ly + 10), color=NARANJA, fill=NARANJA)
    pag.insert_text((m + 18, ly + 8), "Unidad con funciones de TI (tecnología, datos, seguridad, continuidad, pagos inmediatos)",
                    fontsize=7.5, fontname="helv")
    pag.draw_rect(pymupdf.Rect(m, ly + 14, m + 14, ly + 24), color=GRIS, fill=GRIS)
    pag.insert_text((m + 18, ly + 22), "Otras unidades.  G.: gerencia; D.: dirección", fontsize=7.5, fontname="helv")
    pag.set_cropbox(pymupdf.Rect(0, 0, ANCHO, ly + 30))
    pag.get_pixmap(dpi=220).save(salida)
    print("Generado:", salida)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    dibujar(sys.argv[1])
