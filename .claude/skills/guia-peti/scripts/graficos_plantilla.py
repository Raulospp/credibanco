"""Dibuja las ilustraciones que pide la Plantilla PETI (Anexo 2) como imágenes PNG.

Uso:
    python .claude/skills/guia-peti/scripts/graficos_plantilla.py <carpeta_salida>

Genera:
  - seguridad_radar.png: brechas de seguridad por tema del Anexo A de ISO/IEC 27001:2022 (numeral 6.7,
    Ilustración 11 de la plantilla). Valores de la tabla "Evaluación de efectividad de controles".
  - arquitectura_actual.png: vista conceptual de la arquitectura de tecnología de línea base (numeral 6.5,
    Ilustración 10).
  - arquitectura_objetivo.png: vista conceptual de la arquitectura objetivo (numeral 7.5.1, Ilustración 17).
  - integraciones_objetivo.png: mapa de integraciones objetivo (numeral 7.4.2).
Los contenidos salen de los numerales citados en cada función; si cambian allí, se cambian aquí.
Requiere PyMuPDF.
"""
import math
import os
import sys

import pymupdf

NARANJA = (0.91, 0.60, 0.20)
NARANJA_CLARO = (0.99, 0.91, 0.80)
MORADO = (0.40, 0.33, 0.72)
MORADO_CLARO = (0.90, 0.88, 0.97)
AZUL = (0.20, 0.27, 0.49)
GRIS = (0.95, 0.95, 0.95)
GRIS_BORDE = (0.72, 0.72, 0.76)
GRIS_TEXTO = (0.35, 0.35, 0.38)
ROJO = (0.72, 0.18, 0.18)
BLANCO, NEGRO = (1, 1, 1), (0.12, 0.12, 0.12)
_MEDIDA = pymupdf.open().new_page(width=2000, height=4000)


def alto_texto(texto, ancho, tam, fuente="helv"):
    return 4000 - _MEDIDA.insert_textbox(pymupdf.Rect(0, 0, ancho, 4000), texto, fontsize=tam, fontname=fuente,
                                         lineheight=1.15)


def caja(pag, r, texto, fondo, color=NEGRO, tam=7, fuente="helv", borde=GRIS_BORDE, centrado=True, grosor=0.6):
    pag.draw_rect(r, color=borde, fill=fondo, width=grosor, radius=0.06)
    interior = r + (4, 3, -4, -2)
    while tam > 4.6 and alto_texto(texto, interior.width, tam, fuente) > interior.height:
        tam -= 0.2
    desplazar = max(0, (interior.height - alto_texto(texto, interior.width, tam, fuente)) / 2) if centrado else 0
    pag.insert_textbox(interior + (0, desplazar, 0, desplazar), texto, fontsize=tam, fontname=fuente, color=color,
                       align=pymupdf.TEXT_ALIGN_CENTER if centrado else pymupdf.TEXT_ALIGN_LEFT, lineheight=1.15)


def guardar(doc, ruta, zoom=4):
    doc[0].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom)).save(ruta)
    print("Generado:", ruta)


def radar(salida):
    temas = ["5. Organizacionales", "6. Personas", "7. Físicos", "8. Tecnológicos"]
    actual, objetivo = [4, 2, 3, 4], [5, 4, 4, 5]
    ancho, alto = 470, 282
    doc = pymupdf.open()
    pag = doc.new_page(width=ancho, height=alto)
    cx, cy, rmax = 180, 144, 100
    angulos = [-math.pi / 2 + k * 2 * math.pi / len(temas) for k in range(len(temas))]

    def punto(k, v):
        return pymupdf.Point(cx + rmax * v / 5 * math.cos(angulos[k]), cy + rmax * v / 5 * math.sin(angulos[k]))

    for nivel in range(1, 6):
        pag.draw_polyline([punto(k, nivel) for k in range(len(temas))] + [punto(0, nivel)], color=GRIS_BORDE,
                          width=0.5)
        pag.insert_text(punto(0, nivel) + (3, 3), str(nivel), fontsize=6, color=GRIS_TEXTO)
    for k in range(len(temas)):
        pag.draw_line(pymupdf.Point(cx, cy), punto(k, 5), color=GRIS_BORDE, width=0.5)
    pag.draw_polyline([punto(k, v) for k, v in enumerate(objetivo)] + [punto(0, objetivo[0])], color=MORADO,
                      fill=MORADO_CLARO, width=1.4, fill_opacity=0.45)
    pag.draw_polyline([punto(k, v) for k, v in enumerate(actual)] + [punto(0, actual[0])], color=NARANJA,
                      fill=NARANJA_CLARO, width=1.6, fill_opacity=0.6)
    for k in range(len(temas)):
        for v, c in ((actual[k], NARANJA), (objetivo[k], MORADO)):
            pag.draw_circle(punto(k, v), 2.2, color=c, fill=c)
    posiciones = [(cx - 50, cy - rmax - 28), (cx + rmax + 4, cy - 10), (cx - 50, cy + rmax + 4), (cx - rmax - 84, cy - 10)]
    for k, (x, y) in enumerate(posiciones):
        pag.insert_textbox(pymupdf.Rect(x, y, x + (80 if k in (1, 3) else 100), y + 30), f"{temas[k]}\nActual {actual[k]}; objetivo {objetivo[k]}",
                           fontsize=6.8, fontname="helv", color=NEGRO,
                           align=pymupdf.TEXT_ALIGN_CENTER)
    lx = 372
    pag.draw_rect(pymupdf.Rect(lx, 50, lx + 12, 60), color=NARANJA, fill=NARANJA_CLARO, width=1.2)
    pag.insert_text((lx + 17, 58), "Actual (estimada)", fontsize=7)
    pag.draw_rect(pymupdf.Rect(lx, 68, lx + 12, 78), color=MORADO, fill=MORADO_CLARO, width=1.2)
    pag.insert_text((lx + 17, 76), "Objetivo (año 4)", fontsize=7)
    caja(pag, pymupdf.Rect(lx - 4, 96, ancho - 6, 250),
         "Promedio: de 3,25 a 4,5 (KPI-14)\n\nEscala MSPI: 0 inexistente, 1 inicial, 2 repetible, 3 definido, "
         "4 administrado, 5 optimizado.\n\nBrecha mayor: controles de personas (de 2 a 4), por la sensibilización sin "
         "cobertura medida (SE2).\n\nLa línea base se recalibra con la autoevaluación del mes 3 (P1.6).",
         GRIS, tam=6.3, centrado=False)
    guardar(doc, os.path.join(salida, "seguridad_radar.png"))


def _capas(pag, x0, x1, y, capas, estilo):
    """capas: [(nombre, [(texto, clave)])]; estilo: clave -> (fondo, borde, grosor)."""
    for nombre, cajas in capas:
        alto = 33
        pag.draw_rect(pymupdf.Rect(x0, y, x1, y + alto + 8), color=None, fill=GRIS)
        caja(pag, pymupdf.Rect(x0, y, x0 + 62, y + alto + 8), nombre, AZUL, BLANCO, 7, "hebo", AZUL)
        ancho = (x1 - x0 - 66 - 4 * (len(cajas) - 1)) / len(cajas)
        for k, (texto, clave) in enumerate(cajas):
            fondo, borde, grosor = estilo[clave]
            xa = x0 + 66 + k * (ancho + 4)
            caja(pag, pymupdf.Rect(xa, y + 4, xa + ancho, y + alto + 4), texto, fondo, NEGRO, 6.3, borde=borde,
                 grosor=grosor)
        y += alto + 12
    return y


def arquitectura(salida, objetivo):
    ancho = 470
    doc = pymupdf.open()
    pag = doc.new_page(width=ancho, height=420)
    x0, x1 = 10, ancho - 78
    caja(pag, pymupdf.Rect(10, 8, ancho - 10, 28),
         "Vista conceptual de la arquitectura de tecnología " + ("objetivo (septiembre de 2030)" if objetivo
                                                                 else "de línea base (2025)"),
         AZUL, BLANCO, 8.5, "hebo", AZUL)
    estilo = {"n": (BLANCO, GRIS_BORDE, 0.6), "c": (NARANJA_CLARO, NARANJA, 0.8), "p": (MORADO_CLARO, MORADO, 1.3),
              "f": (BLANCO, ROJO, 1.0)}
    nube = "c"
    if not objetivo:
        capas = [
            ("Canales", [("Terminales de punto de venta\n(más de 76.000)", "n"), ("Pasarela y botón de pagos", "n"),
                         ("Portal de autogestión", "n"), ("Portal de desarrolladores\n(API)", "n"),
                         ("Contact center\n(nube)", nube)]),
            ("Integración", [("Bus de servicios del switch", "n"), ("Hubs de API\n(tiempo real, Open Finance)", "n"),
                             ("Mensajería ISO 20022\n(Bre-B)", "n"),
                             ("Esquema de seguridad de las integraciones: no publicado (S4)", "f")]),
            ("Aplicaciones", [("Switch y multiswitch\nen contenedores", "n"), ("Canje y compensación", "n"),
                              ("Nodo de pagos\ninmediatos (nube)", nube), ("Hub de Open Finance\n(nube)", nube),
                              ("Antifraude con IA", "n"), ("CRM y ERP (SAP)", "n")]),
            ("Datos", [("Plataforma de datos y bodega (Cloudera)", "n"),
                       ("Productos de información\n(DaInsight, Analítico Banco)", "n"),
                       ("Gobierno y calidad de datos: no publicados (I1, I6)", "f")]),
            ("Infraestructura", [("Multinube\n(nodo, hub, contact center)", nube),
                                 ("Centro de datos principal y secundario\n(a más de 50 km, replicación en línea)",
                                  "n"), ("Contenedores\n(OpenShift, Docker, Kubernetes)", "n"),
                                 ("Catálogo de infraestructura y costos de nube: no publicados (T6, T7)", "f")]),
        ]
        lateral = [("Seguridad", "Perimetral y de red, tokenización, 3D Secure, controles PCI DSS y PCI PIN; "
                    "contención de 79 millones de ataques en 2025", "n"),
                   ("Observabilidad", "100 soluciones e infraestructura propia y en la nube", "n")]
        leyenda = [("n", "Componente en operación"), ("c", "En la nube"), ("f", "Sin evidencia pública (hallazgo)")]
        fuente = ("Fuente: elaboración propia a partir de los numerales 6.4 y 6.5 (informes de gestión 2022 a 2025, "
                  "estados financieros 2024-2025 y comunicados de aliados).")
    else:
        capas = [
            ("Canales", [("Terminales, pasarela y portales", "n"), ("Contact center (nube)", nube),
                         ("Soporte interno de TI con ANS\n(P1.4)", "p")]),
            ("Integración", [("Bus de servicios y hubs de API", "n"), ("Mensajería ISO 20022", "n"),
                             ("Gestión de API y esquema de seguridad por integración (P2.3)", "p")]),
            ("Aplicaciones", [("Switch, canje y compensación", "n"), ("Nodo de pagos inmediatos\n(nube)", nube),
                              ("Hub de Open Finance (nube)", nube), ("Antifraude, CRM y ERP", "n"),
                              ("Arquitectura de referencia e inventario\n(P2.2)", "p")]),
            ("Datos", [("Plataforma de datos", "n"),
                       ("Gobierno de datos y catálogo\n(P2.1)", "p"),
                       ("Calidad de datos e inventario de modelos de IA (P3.1)", "p"),
                       ("Plataforma gobernada para productos de información (P4.2)", "p")]),
            ("Infraestructura", [("Multinube", nube), ("Centros de datos principal y secundario", "n"),
                                 ("Catálogo y gestión de la configuración\n(P2.5)", "p"),
                                 ("Presupuesto y costos de nube por servicio (P1.5)", "p")]),
        ]
        lateral = [("Seguridad", "Confianza cero: identidades y segmentación (P2.4) y monitoreo continuo (P4.1); "
                    "madurez 4,5 (KPI-14)", "p"),
                   ("Observabilidad", "De extremo a extremo del nodo; capacidad probada cada año con 2 veces el pico "
                    "(P3.3, KPI-11)", "p")]
        leyenda = [("n", "Se mantiene"), ("c", "En la nube (se mantiene)"), ("p", "Propuesto (proyecto del PETI)")]
        fuente = "Fuente: propuesta del equipo a partir de los numerales 7.4 y 7.5 y del portafolio del numeral 8."
    y = _capas(pag, x0, x1, 34, capas, estilo)
    alto_lat = (y - 34 - 12) / 2
    for k, (nombre, texto, clave) in enumerate(lateral):
        fondo, borde, grosor = estilo[clave]
        r = pymupdf.Rect(x1 + 4, 34 + k * (alto_lat + 8), ancho - 10, 34 + k * (alto_lat + 8) + alto_lat)
        pag.draw_rect(r, color=borde, fill=fondo, width=grosor, radius=0.06)
        pag.insert_textbox(r + (3, 4, -3, 0), nombre, fontsize=7, fontname="hebo", color=AZUL,
                           align=pymupdf.TEXT_ALIGN_CENTER)
        pag.insert_textbox(r + (3, 16, -3, -2), texto, fontsize=6, color=NEGRO, align=pymupdf.TEXT_ALIGN_CENTER,
                           lineheight=1.15)
    lx = 10
    for clave, texto in leyenda:
        fondo, borde, grosor = estilo[clave]
        pag.draw_rect(pymupdf.Rect(lx, y + 2, lx + 12, y + 11), color=borde, fill=fondo, width=grosor)
        pag.insert_text((lx + 16, y + 10), texto, fontsize=6.5)
        lx += 30 + len(texto) * 3.3
    doc2 = pymupdf.open()
    p2 = doc2.new_page(width=ancho, height=y + 16)
    p2.show_pdf_page(p2.rect, doc, 0, clip=pymupdf.Rect(0, 0, ancho, y + 16))
    guardar(doc2, os.path.join(salida, "arquitectura_objetivo.png" if objetivo else "arquitectura_actual.png"))


def integraciones(salida):
    filas = [
        ("Entidades participantes de Bre-B", "Nodo de pagos inmediatos", "Mensajería ISO 20022 con esquema de seguridad documentado", "P2.3"),
        ("Originador y receptor del pago", "Servicio de calificación de fraude", "API gestionada; autenticación y cifrado documentados", "P2.3"),
        ("Comercios y aliados", "Pasarela de pagos", "API gestionada; autenticación y cifrado documentados", "P2.3"),
        ("Desarrolladores", "Portal de desarrolladores y API", "Gestión de API; credenciales y políticas de consumo", "P2.3"),
        ("Redes de tarjetas", "Switch transaccional", "Mecanismo vigente; esquema documentado (PCI DSS y PCI PIN)", "P2.3"),
        ("Proveedores y receptores de datos", "Hub de Open Finance", "API estandarizadas, puerta de enlace y consentimiento trazable", "Se mantiene"),
        ("Switches transaccionales", "Switches transaccionales", "Multiswitch en contenedores; segmentación de confianza cero", "P2.4"),
    ]
    ancho = 470
    alto = 40 + len(filas) * 38 + 14
    doc = pymupdf.open()
    pag = doc.new_page(width=ancho, height=alto)
    xe, xi = (10, 120), (330, 460)
    caja(pag, pymupdf.Rect(*xe[:1], 8, xe[1], 28), "Externos", AZUL, BLANCO, 8, "hebo", AZUL)
    caja(pag, pymupdf.Rect(xi[0], 8, xi[1], 28), "Credibanco", NARANJA, BLANCO, 8, "hebo", NARANJA)
    caja(pag, pymupdf.Rect(xe[1] + 10, 8, xi[0] - 10, 28), "Mecanismo y seguridad objetivo", GRIS, AZUL, 7.5,
         "hebo")
    y = 36
    for origen, destino, mecanismo, proyecto in filas:
        nuevo = proyecto != "Se mantiene"
        color = MORADO if nuevo else GRIS_TEXTO
        caja(pag, pymupdf.Rect(xe[0], y, xe[1], y + 30), origen, MORADO_CLARO if nuevo else GRIS, NEGRO, 6.8)
        caja(pag, pymupdf.Rect(xi[0], y, xi[1], y + 30), destino, NARANJA_CLARO, NEGRO, 6.8, borde=NARANJA)
        ym = y + 15
        pag.draw_line(pymupdf.Point(xe[1], ym), pymupdf.Point(xi[0] - 4, ym), color=color, width=1.3 if nuevo else 0.8,
                      dashes=None if nuevo else "[3 2] 0")
        pag.draw_polyline([pymupdf.Point(xi[0] - 8, ym - 3.5), pymupdf.Point(xi[0] - 2, ym),
                           pymupdf.Point(xi[0] - 8, ym + 3.5)], color=color, fill=color, closePath=True)
        pag.insert_textbox(pymupdf.Rect(xe[1] + 8, y - 1, xi[0] - 12, ym - 1), mecanismo, fontsize=6.2,
                           color=NEGRO, align=pymupdf.TEXT_ALIGN_CENTER)
        pag.insert_textbox(pymupdf.Rect(xe[1] + 8, ym + 2, xi[0] - 12, y + 30), proyecto, fontsize=6.5,
                           fontname="hebo", color=color, align=pymupdf.TEXT_ALIGN_CENTER)
        y += 38
    pag.draw_line(pymupdf.Point(12, y + 4), pymupdf.Point(34, y + 4), color=MORADO, width=1.3)
    pag.insert_text((38, y + 7), "Integración con esquema de seguridad nuevo o formalizado (proyecto)", fontsize=6.5)
    pag.draw_line(pymupdf.Point(270, y + 4), pymupdf.Point(292, y + 4), color=GRIS_TEXTO, width=0.8,
                  dashes="[3 2] 0")
    pag.insert_text((296, y + 7), "Se mantiene (seguridad ya publicada)", fontsize=6.5)
    guardar(doc, os.path.join(salida, "integraciones_objetivo.png"))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    os.makedirs(sys.argv[1], exist_ok=True)
    radar(sys.argv[1])
    arquitectura(sys.argv[1], objetivo=False)
    arquitectura(sys.argv[1], objetivo=True)
    integraciones(sys.argv[1])
