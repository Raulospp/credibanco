"""Figuras del PETI 2027-2030 de Valor+ (numeral 6).

Uso: python .claude/skills/guia-peti/scripts/figuras_valor.py
Escribe en docs/figuras/: indicadores_ti_2025.png, infraestructura_actual.png, radar_seguridad.png.
Los datos salen de los numerales 6.1.6, 6.5.1 y 6.7 de docs/peti.md (con su fuente allí).
"""
import math
from pathlib import Path

import pymupdf as fitz

OUT = Path(__file__).resolve().parents[4] / "docs" / "figuras"
VERDE = (0.04, 0.36, 0.23)
VERDE_CLARO = (0.91, 0.95, 0.93)
AZUL = (0.11, 0.44, 0.66)
AZUL_CLARO = (0.89, 0.93, 0.97)
ROJO = (0.75, 0.22, 0.17)
GRIS = (0.45, 0.45, 0.45)
NEGRO = (0.1, 0.1, 0.1)


def texto(pg, rect, s, fs=10, font="helv", color=NEGRO, align=1):
    while pg.insert_textbox(rect, s, fontsize=fs, fontname=font, color=color, align=align) < 0 and fs > 5:
        fs -= 0.5


def caja(pg, cx, cy, w, h, s, fill, stroke, color=NEGRO, fs=10, font="hebo"):
    r = fitz.Rect(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    pg.draw_rect(r, color=stroke, fill=fill, width=1.3, radius=0.08)
    n = s.count("\n") + 1
    alto = n * fs * 1.25
    texto(pg, fitz.Rect(r.x0 + 4, cy - alto / 2 - 1, r.x1 - 4, cy + alto / 2 + fs), s, fs, font, color)


def fuente(pg, y, s):
    pg.insert_text((20, y), s, fontsize=9, color=(0.3, 0.3, 0.3))


def indicadores():
    datos = [  # (nombre, meta, resultado) en %
        ("ANS contractuales", 94, 95.71),
        ("ANS internos", 80, 94.71),
        ("Facturación de ingresos", 80, 77.83),
        ("Presupuesto de costos", 93, 80.72),
        ("Disponibilidad servicios críticos", 99, 100),
        ("Gestión de incidentes de seguridad", 100, 100),
        ("Protección ante ataques", 99, 100),
        ("Oportunidad de atención TI", 95, 98.72),
        ("Registros de propiedad intelectual (4 = 100 %)", 100, 50),
    ]
    W, H = 1000, 520
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    x0, x1, y = 330, 900, 40
    paso = 48
    for v in (0, 25, 50, 75, 100):
        x = x0 + (x1 - x0) * v / 100
        pg.draw_line((x, 30), (x, 30 + paso * len(datos)), color=(0.85, 0.85, 0.85), width=0.6)
        pg.insert_text((x - 8, 30 + paso * len(datos) + 14), f"{v} %", fontsize=8, color=GRIS)
    for nombre, meta, res in datos:
        cumple = res >= meta
        texto(pg, fitz.Rect(10, y, x0 - 10, y + 30), nombre, 10, "helv", NEGRO, 2)
        xr = x0 + (x1 - x0) * min(res, 100) / 100
        pg.draw_rect(fitz.Rect(x0, y + 4, xr, y + 26), color=None, fill=VERDE if cumple else ROJO)
        xm = x0 + (x1 - x0) * meta / 100
        pg.draw_line((xm, y), (xm, y + 30), color=NEGRO, width=2)
        etiqueta = f"{res:.2f}".replace(".", ",").replace(",00", "") + " %"
        if nombre.startswith("Registros"):
            etiqueta = "2 de 4"
        pg.insert_text((min(max(xr, xm + 2), x1) + 6, y + 20), etiqueta, fontsize=9, color=NEGRO)
        y += paso
    pg.draw_rect(fitz.Rect(330, 478, 342, 490), color=None, fill=VERDE)
    pg.insert_text((346, 488), "Cumple", fontsize=9)
    pg.draw_rect(fitz.Rect(400, 478, 412, 490), color=None, fill=ROJO)
    pg.insert_text((416, 488), "No cumple", fontsize=9)
    pg.draw_line((490, 478), (490, 490), color=NEGRO, width=2)
    pg.insert_text((496, 488), "Meta", fontsize=9)
    fuente(pg, 510, "Fuente: Informe de gestión 2025 de Valor+, págs. 16-17.")
    pg.get_pixmap(dpi=200).save(OUT / "indicadores_ti_2025.png")


def infraestructura():
    W, H = 1100, 560
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    # Nube
    nube = fitz.Rect(30, 30, 1070, 200)
    pg.draw_rect(nube, color=AZUL, fill=AZUL_CLARO, width=1.2, radius=0.05)
    pg.insert_text((45, 52), "Nube pública y SaaS", fontsize=12, fontname="hebo", color=AZUL)
    for cx, s in ((135, "AWS\nSitio web, servidores\ny respaldo"), (335, "Oracle Cloud\ny Azure"),
                  (535, "Microsoft 365\nCorreo, Teams,\nOneDrive, Power BI"), (745, "SaaS de proveedores\nERP (SICOF), sistemas\nde clientes"),
                  (955, "Plataformas del Estado\nSECOP, FURAG")):
        caja(pg, cx, 125, 180, 90, s, (1, 1, 1), AZUL, fs=10, font="helv")
    # Perímetro
    caja(pg, 550, 250, 520, 46, "Perímetro: UTM en alta disponibilidad (comodato con el proveedor de internet)", (1, 0.97, 0.9), (0.8, 0.55, 0.1), fs=10)
    pg.draw_line((550, 200), (550, 227), color=GRIS, width=1.5)
    pg.draw_line((550, 273), (550, 300), color=GRIS, width=1.5)
    # Sedes
    sedes = fitz.Rect(30, 300, 1070, 500)
    pg.draw_rect(sedes, color=VERDE, fill=VERDE_CLARO, width=1.2, radius=0.05)
    pg.insert_text((45, 322), "En sitio: sede Edatel y otras seis sedes y puntos", fontsize=12, fontname="hebo", color=VERDE)
    for cx, s in ((140, "Servidor de archivos\n(unidad V)"), (330, "Directorio activo,\nDNS, DHCP"), (520, "Intranet"),
                  (710, "Telefonía IP\nAsterisk, FreePBX"), (900, "Mesa de ayuda\nOTRS, GLPI")):
        caja(pg, cx, 380, 170, 70, s, (1, 1, 1), VERDE, fs=10, font="helv")
    caja(pg, 550, 460, 700, 44, "LAN, WAN y VPN entre sedes · equipos de usuario con antimalware · cuartos técnicos", (1, 1, 1), VERDE, fs=10, font="helv")
    fuente(pg, 530, "Fuente: elaboración del equipo con base en PETI 2026-2027 de Valor+, págs. 46-61 y 77, e Informe de gestión 2025, pág. 87.")
    pg.get_pixmap(dpi=200).save(OUT / "infraestructura_actual.png")


def radar():
    temas = ["Políticas y\norganización", "Gestión de\nactivos", "Control de\nacceso", "Seguridad de\nlas personas",
             "Seguridad\nfísica", "Operaciones y\ncomunicaciones", "Gestión de\nincidentes", "Continuidad\ndel negocio", "Cumplimiento"]
    actual = [60, 40, 60, 40, 40, 60, 40, 20, 60]
    meta = [80, 80, 80, 60, 60, 80, 80, 80, 80]
    W, H = 800, 730
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    cx, cy, R = 400, 345, 230
    n = len(temas)

    def punto(i, v):
        a = -math.pi / 2 + 2 * math.pi * i / n
        return fitz.Point(cx + R * v / 100 * math.cos(a), cy + R * v / 100 * math.sin(a))

    for v in (20, 40, 60, 80, 100):
        pts = [punto(i, v) for i in range(n)]
        pg.draw_polyline(pts + [pts[0]], color=(0.8, 0.8, 0.8), width=0.6)
        pg.insert_text((cx + 3, cy - R * v / 100 + 10), str(v), fontsize=7, color=GRIS)
    for i, t in enumerate(temas):
        pg.draw_line((cx, cy), punto(i, 100), color=(0.8, 0.8, 0.8), width=0.6)
        p = punto(i, 122)
        etiqueta = f"{t}\n{actual[i]} → {meta[i]}".replace("→", "a")
        texto(pg, fitz.Rect(p.x - 65, p.y - 18, p.x + 65, p.y + 30), etiqueta, 10, "helv")
    for vals, col, w, relleno in ((meta, AZUL, 2, AZUL_CLARO), (actual, ROJO, 2.4, (0.98, 0.86, 0.84))):
        pts = [punto(i, v) for i, v in enumerate(vals)]
        pg.draw_polyline(pts + [pts[0]], color=col, width=w, fill=relleno, fill_opacity=0.55)
        for p in pts:
            pg.draw_circle(p, 3.5, color=col, fill=col)
    pg.draw_line((230, 675), (255, 675), color=ROJO, width=2.4)
    pg.insert_text((260, 679), "Actual (2026): promedio 47", fontsize=10)
    pg.draw_line((430, 675), (455, 675), color=AZUL, width=2)
    pg.insert_text((460, 679), "Objetivo (2030): promedio 76", fontsize=10)
    fuente(pg, 712, "Fuente: estimación del equipo con la escala del MSPI (0 a 100), con base en el Informe de gestión 2025, págs. 87-89.")
    pg.get_pixmap(dpi=200).save(OUT / "radar_seguridad.png")


def alineacion():
    ocs = [("OC01", "Fortalecer la gobernanza"), ("OC02", "Articular la gestión\ninstitucional"),
           ("OC03", "Sostenibilidad financiera"), ("OC04", "Experiencia del cliente"),
           ("OC05", "Principal aliado\ntecnológico de Antioquia")]
    oetis = [("OETI01", "Formalizar el gobierno\ny la gestión de la TI", ("OC01", "OC02")),
             ("OETI02", "Gestionar la TI como servicios\ncon niveles acordados", ("OC04", "OC05")),
             ("OETI03", "Digitalizar los procesos\nmisionales y de apoyo", ("OC02", "OC03")),
             ("OETI04", "Gobernar y aprovechar\nlos datos", ("OC01", "OC04")),
             ("OETI05", "Asegurar una infraestructura\ndisponible y recuperable", ("OC03", "OC04")),
             ("OETI06", "Elevar la madurez de seguridad\ny la apropiación", ("OC01", "OC05"))]
    W, H = 1000, 640
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    pg.insert_text((90, 40), "Objetivos corporativos (PEI 2024-2027)", fontsize=12, fontname="hebo", color=VERDE)
    pg.insert_text((620, 40), "Objetivos de TI (PETI 2027-2030)", fontsize=12, fontname="hebo", color=AZUL)
    yoc = {}
    for i, (cod, nom) in enumerate(ocs):
        cy = 100 + i * 110
        yoc[cod] = cy
        caja(pg, 200, cy, 280, 70, f"{cod}\n{nom}", VERDE_CLARO, VERDE, fs=10)
    for i, (cod, nom, rel) in enumerate(oetis):
        cy = 90 + i * 95
        for oc in rel:
            pg.draw_line((340, yoc[oc]), (580, cy), color=GRIS, width=1)
        caja(pg, 730, cy, 300, 70, f"{cod}\n{nom}", AZUL_CLARO, AZUL, fs=10)
    fuente(pg, 625, "Fuente: elaboración del equipo. Objetivos corporativos del PEI 2024-2027 (Informe de gestión 2025, pág. 13); objetivos de TI propuestos (numeral 7.1.3).")
    pg.get_pixmap(dpi=200).save(OUT / "alineacion_oc_oeti.png")


def arquitectura_objetivo():
    W, H = 1100, 700
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    capas = [
        (70, "Canales", AZUL, [("Sitio web y PQRSD", "Mantener"), ("Intranet en SharePoint", "Migrar"), ("Contact center en la nube", "Migrar"), ("Tableros Power BI", "Mantener")]),
        (190, "Sistemas misionales", VERDE, [("CRM", "Crear"), ("Gestión de procesos (BPMS)", "Crear"), ("Gestión de servicios TI (ITSM)", "Reemplazar"), ("Sistemas de clientes (SaaS)", "Mantener")]),
        (310, "Sistemas de apoyo y control", VERDE, [("ERP integrado", "Reemplazar"), ("SGDEA (Carriel)", "Modificar"), ("Gestión de riesgos", "Crear"), ("SECOP, FURAG", "Mantener")]),
    ]
    for y, nombre, col, cajas in capas:
        pg.insert_text((30, y - 30), nombre, fontsize=11, fontname="hebo", color=col)
        for i, (s, acc) in enumerate(cajas):
            cx = 160 + i * 260
            fill = {"Crear": (0.88, 0.95, 0.88), "Reemplazar": (1, 0.94, 0.86), "Migrar": (1, 0.94, 0.86), "Modificar": (1, 0.94, 0.86)}.get(acc, (1, 1, 1))
            caja(pg, cx, y + 15, 230, 60, f"{s}\n({acc.lower()})", fill, col, fs=10, font="helv")
    # capa de integración
    caja(pg, 550, 410, 1000, 40, "Capa de integración (API documentadas) · identidad única con segundo factor (crear)", (0.88, 0.95, 0.88), AZUL, fs=11)
    caja(pg, 550, 470, 1000, 40, "Datos: catálogo de entidades de información, responsables y reglas de calidad (crear)", (0.88, 0.95, 0.88), AZUL, fs=11)
    pg.insert_text((30, 525), "Infraestructura", fontsize=11, fontname="hebo", color=GRIS)
    for i, (s, acc) in enumerate((("Nube: AWS, Oracle, Azure,\nMicrosoft 365", "mantener"), ("Archivos, directorio, intranet,\ntelefonía y mesa en la nube", "migrar"),
                                  ("NOC y SOC propios", "crear"), ("Sedes: red segmentada,\nequipos, cuartos técnicos", "modificar"))):
        cx = 160 + i * 260
        fill = {"crear": (0.88, 0.95, 0.88), "migrar": (1, 0.94, 0.86), "modificar": (1, 0.94, 0.86)}.get(acc, (1, 1, 1))
        caja(pg, cx, 575, 230, 70, f"{s}\n({acc})", fill, GRIS, fs=10, font="helv")
    pg.draw_rect(fitz.Rect(30, 632, 42, 644), color=None, fill=(0.88, 0.95, 0.88))
    pg.insert_text((46, 642), "Nuevo", fontsize=9)
    pg.draw_rect(fitz.Rect(100, 632, 112, 644), color=None, fill=(1, 0.94, 0.86))
    pg.insert_text((116, 642), "Cambia", fontsize=9)
    pg.draw_rect(fitz.Rect(175, 632, 187, 644), color=GRIS, fill=(1, 1, 1))
    pg.insert_text((191, 642), "Se mantiene", fontsize=9)
    fuente(pg, 680, "Fuente: elaboración del equipo (numerales 7.4 y 7.5). Propuesta sujeta a aprobación.")
    pg.get_pixmap(dpi=200).save(OUT / "arquitectura_objetivo.png")


def brechas_dominio():
    # (dominio, crear, modificar) según el catálogo de brechas del numeral 8
    datos = [("Gobierno", 4, 2), ("Estrategia", 1, 2), ("Sistemas", 3, 2), ("Información", 2, 1),
             ("Infraestructura", 1, 2), ("Seguridad", 0, 2), ("Uso y apropiación", 1, 0)]
    W, H = 900, 420
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    x0, esc, y = 180, 70, 40
    for v in range(0, 8):
        x = x0 + v * esc
        pg.draw_line((x, 30), (x, 30 + 45 * len(datos)), color=(0.88, 0.88, 0.88), width=0.6)
        pg.insert_text((x - 3, 30 + 45 * len(datos) + 14), str(v), fontsize=8, color=GRIS)
    for dom, c, m in datos:
        texto(pg, fitz.Rect(10, y + 6, x0 - 10, y + 30), dom, 10, "helv", NEGRO, 2)
        if c:
            pg.draw_rect(fitz.Rect(x0, y + 6, x0 + c * esc, y + 30), color=None, fill=VERDE)
        if m:
            pg.draw_rect(fitz.Rect(x0 + c * esc, y + 6, x0 + (c + m) * esc, y + 30), color=None, fill=AZUL)
        pg.insert_text((x0 + (c + m) * esc + 6, y + 23), str(c + m), fontsize=10, fontname="hebo")
        y += 45
    pg.draw_rect(fitz.Rect(180, 375, 192, 387), color=None, fill=VERDE)
    pg.insert_text((196, 385), "Crear (12)", fontsize=9)
    pg.draw_rect(fitz.Rect(270, 375, 282, 387), color=None, fill=AZUL)
    pg.insert_text((286, 385), "Modificar (11)", fontsize=9)
    fuente(pg, 410, "Fuente: catálogo de brechas del numeral 8 (análisis del equipo).")
    pg.get_pixmap(dpi=200).save(OUT / "brechas_dominio.png")


def presupuesto():
    datos = [("2027", 1640), ("2028", 2236), ("2029", 1554), ("2030", 740)]
    W, H = 760, 440
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    base, alto, maxv = 360, 300, 2500
    for v in (0, 500, 1000, 1500, 2000, 2500):
        y = base - alto * v / maxv
        pg.draw_line((90, y), (700, y), color=(0.88, 0.88, 0.88), width=0.6)
        pg.insert_text((30, y + 3), f"{v:,}".replace(",", "."), fontsize=8, color=GRIS)
    yref = base - alto * 2134 / maxv
    pg.draw_line((90, yref), (700, yref), color=ROJO, width=1.2, dashes="[5 3] 0")
    pg.insert_text((450, yref - 5), "Inversión total de Valor+ en 2025: 2.134", fontsize=8, color=ROJO)
    for i, (anio, v) in enumerate(datos):
        x = 140 + i * 145
        y = base - alto * v / maxv
        pg.draw_rect(fitz.Rect(x, y, x + 80, base), color=None, fill=VERDE)
        pg.insert_text((x + 18, y - 6), f"{v:,}".replace(",", "."), fontsize=10, fontname="hebo")
        pg.insert_text((x + 25, base + 16), anio, fontsize=10)
    pg.insert_text((30, 25), "Millones de pesos", fontsize=9, color=GRIS)
    fuente(pg, 420, "Fuente: catálogo de proyectos del numeral 8 (estimación del equipo); Informe de gestión 2025, pág. 157 (referencia).")
    pg.get_pixmap(dpi=200).save(OUT / "presupuesto_vigencias.png")


def mapa_ruta():
    # (proyecto, inicio en meses desde enero de 2027 (0), duración en meses, color)
    proyectos = [
        ("P1.1 Modelo de gobierno de TI", 0, 6, VERDE), ("P1.2 Procesos de gestión de TI", 1, 11, VERDE),
        ("P1.3 Catálogo y tablero de TI", 2, 10, AZUL), ("P1.4 Incidentes y SOC propio", 0, 12, ROJO),
        ("P1.5 ERP integrado", 0, 24, (0.55, 0.35, 0.65)), ("P1.6 Continuidad y recuperación", 0, 12, ROJO),
        ("P2.1 Gobierno de datos e IA", 12, 12, (0.85, 0.55, 0.1)), ("P2.2 CRM", 13, 11, (0.55, 0.35, 0.65)),
        ("P2.3 Gestión de servicios de TI", 12, 9, AZUL), ("P2.4 Migración a la nube", 12, 18, GRIS),
        ("P2.5 SGDEA", 15, 21, (0.85, 0.55, 0.1)), ("P2.6 Uso y apropiación", 12, 36, (0.2, 0.6, 0.6)),
        ("P3.1 Procesos, integración y riesgos", 24, 18, (0.55, 0.35, 0.65)), ("P3.2 Analítica institucional", 27, 12, (0.85, 0.55, 0.1)),
        ("P3.3 Capacidad, NOC e IPv6", 24, 12, GRIS), ("P4.1 Evaluación del PETI", 42, 6, VERDE),
        ("P4.2 IA en PQRSD y mesa", 36, 12, (0.85, 0.55, 0.1)),
    ]
    W, H = 1150, 120 + 30 * len(proyectos)
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    x0, x1 = 290, 1120
    mes = (x1 - x0) / 48
    for a in range(4):
        xa = x0 + a * 12 * mes
        pg.draw_rect(fitz.Rect(xa, 30, xa + 12 * mes, 55), color=(1, 1, 1), fill=VERDE if a % 2 == 0 else (0.2, 0.5, 0.35))
        pg.insert_text((xa + 12 * mes / 2 - 30, 47), f"{2027 + a} (fase {a + 1})", fontsize=10, fontname="hebo", color=(1, 1, 1))
        for t in range(4):
            xt = xa + t * 3 * mes
            pg.draw_line((xt, 55), (xt, H - 50), color=(0.9, 0.9, 0.9), width=0.5)
            pg.insert_text((xt + 3 * mes / 2 - 6, 68), f"T{t + 1}", fontsize=7, color=GRIS)
    y = 78
    for nombre, ini, dur, col in proyectos:
        pg.insert_text((10, y + 14), nombre, fontsize=9)
        pg.draw_rect(fitz.Rect(x0 + ini * mes, y + 4, x0 + (ini + dur) * mes, y + 20), color=None, fill=col, radius=0.3)
        y += 30
    fuente(pg, H - 20, "Fuente: catálogo de proyectos del numeral 8 (propuesta del equipo). Colores por dominio: gobierno, servicios, seguridad, sistemas, datos, infraestructura, uso.")
    pg.get_pixmap(dpi=200).save(OUT / "mapa_ruta.png")


def organigrama_ti_objetivo():
    W, H = 1100, 520
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    linea = lambda a, b: pg.draw_line(a, b, color=GRIS, width=1.2)
    caja(pg, 550, 50, 300, 50, "Gerencia General", VERDE, VERDE, (1, 1, 1), 13)
    linea((550, 75), (550, 150))
    linea((550, 110), (820, 110))
    caja(pg, 900, 110, 190, 60, "Comité de TI\n(sesión mensual del\nComité Directivo)", (0.88, 0.95, 0.88), AZUL, fs=10)
    linea((550, 110), (280, 110))
    caja(pg, 190, 110, 190, 50, "Responsable de seguridad\nde la información (nuevo)", (0.88, 0.95, 0.88), AZUL, fs=10)
    caja(pg, 550, 175, 340, 50, "Gerencia de Tecnología, Innovación y Sostenibilidad", AZUL, AZUL, (1, 1, 1), 11)
    linea((550, 200), (550, 240))
    linea((190, 240), (910, 240))
    dirs = [(190, "Dirección de\nInfraestructura", "Nube, redes, NOC,\nrespaldo y recuperación"),
            (430, "Dirección de\nServicios", "Catálogo, ANS, mesa de\nservicios, uso y apropiación"),
            (670, "Dirección de Desarrollo\ny Servicios", "Sistemas, integración,\nmesas de clientes"),
            (910, "Responsable de gobierno\nde datos (nuevo)", "Catálogo de datos,\ncalidad, datos abiertos")]
    for x, t, f in dirs:
        linea((x, 240), (x, 262))
        nuevo = "nuevo" in t
        caja(pg, x, 292, 210, 60, t, (0.88, 0.95, 0.88) if nuevo else AZUL_CLARO, AZUL, fs=10)
        caja(pg, x, 375, 210, 60, f, (1, 1, 1), GRIS, fs=9, font="helv")
    caja(pg, 550, 450, 760, 40, "Roles asignados, no cargos nuevos: responsables de datos por proceso, responsable de cada servicio de TI", (1, 1, 1), GRIS, fs=10, font="helv")
    fuente(pg, 505, "Fuente: elaboración del equipo (numeral 7.2.4). Verde: elementos nuevos. Propuesta sujeta a aprobación.")
    pg.get_pixmap(dpi=200).save(OUT / "organigrama_ti_objetivo.png")


DOFA = {
    "F": ("Fortalezas", VERDE, [
        "F1 ANS de clientes cumplidos: 95,71 % (Estrategia)",
        "F2 Riesgos con tres líneas de defensa y Comité de Riesgos (Gobierno)",
        "F3 Activos de información inventariados; PINAR vigente (Información)",
        "F4 ERP financiero en SaaS; software propio registrado (Sistemas)",
        "F5 Nube AWS, Oracle y Azure sin hallazgos críticos (Infraestructura)",
        "F6 Boletín mensual de ciberseguridad (Uso y apropiación)",
        "F7 SGSI actualizado al MSPI 2025; 100 % de ataques bloqueados (Seguridad)"]),
    "D": ("Debilidades", ROJO, [
        "D1 Visión y objetivos de TI sin metas; sin catálogo de servicios (Estrategia)",
        "D2 Ninguna instancia decide sobre TI; auditoría de TI en 49 %; sin cargo de seguridad (Gobierno)",
        "D3 Datos sin responsables ni calidad; archivos sin versiones (Información)",
        "D4 Procesos comercial y de servicio en Excel; ERP sin decidir (Sistemas)",
        "D5 Servicios críticos en sitio; sin plan de capacidad; IPv6 atrasado (Infraestructura)",
        "D6 Sin estrategia de uso y apropiación (Uso y apropiación)",
        "D7 Incidentes sin gestión constante; recuperación sin probar (Seguridad)"]),
    "O": ("Oportunidades", AZUL, [
        "O1 PEI y Plan de Desarrollo de Antioquia que demandan TI; 48 contratos",
        "O2 PMO en construcción y MIPG con Gobierno Digital en 86,3",
        "O3 Oferta madura de ERP, CRM y BPMS en la nube",
        "O4 Demanda de SOC por los municipios; IA que ya se vende",
        "O5 Acuerdo 001 de 2024 del AGN y MSPI como guía"]),
    "A": ("Amenazas", (0.85, 0.55, 0.1), [
        "A1 Ransomware y phishing contra entidades públicas",
        "A2 Fin del PEI (2027) y cambio de gobierno departamental (2028)",
        "A3 Hallazgos de la Contraloría: control fiscal interno en 2,0",
        "A4 Dependencia de proveedores SaaS y del proveedor de internet",
        "A5 Rotación de personal y procedimientos desactualizados"]),
}


def dofa():
    W, H = 1200, 600
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    cajas = {"F": fitz.Rect(30, 30, 595, 300), "D": fitz.Rect(605, 30, 1170, 300),
             "O": fitz.Rect(30, 310, 595, 555), "A": fitz.Rect(605, 310, 1170, 555)}
    for k, r in cajas.items():
        titulo, col, items = DOFA[k]
        pg.draw_rect(r, color=col, fill=(1, 1, 1), width=1.5, radius=0.03)
        pg.draw_rect(fitz.Rect(r.x0, r.y0, r.x1, r.y0 + 32), color=col, fill=col, radius=0.03)
        pg.insert_text((r.x0 + 12, r.y0 + 22), titulo, fontsize=13, fontname="hebo", color=(1, 1, 1))
        texto(pg, fitz.Rect(r.x0 + 12, r.y0 + 42, r.x1 - 10, r.y1 - 8), "\n".join("- " + i for i in items), 12, "helv", NEGRO, 0)
    pg.insert_text((30, 580), "Fuente: elaboración del equipo a partir de los hallazgos del numeral 6 y los motivadores del numeral 5.", fontsize=9, color=(0.3, 0.3, 0.3))
    pg.get_pixmap(dpi=200).save(OUT / "dofa.png")


def dofa_cruzada():
    estr = [
        ("FO", "Usar fortalezas para aprovechar oportunidades", VERDE,
         ["FO1 (F7, O4): operar el SOC propio como base del servicio SOC para municipios (proyectos: P1.4, OPT-002)",
          "FO2 (F1, O4): llevar la IA que ya se vende a la atención de PQRSD y la mesa interna (proyectos: P4.2, OPT-001)"]),
        ("DO", "Superar debilidades con las oportunidades", AZUL,
         ["DO1 (D4, O3): reemplazar Excel con ERP, CRM y BPMS en la nube (proyectos: P1.5, P2.2, P3.1)",
          "DO2 (D1, D2, O2): Comité de TI, catálogo de servicios y procesos con la PMO y el MIPG (proyectos: P1.1, P1.2, P1.3)",
          "DO3 (D3, O5): gobierno de datos y SGDEA (proyectos: P2.1, P2.5)"]),
        ("FA", "Usar fortalezas para reducir amenazas", (0.85, 0.55, 0.1),
         ["FA1 (F2, F5, A1, A4): probar la recuperación y dar contingencia en la nube (proyectos: P1.6, P2.4)",
          "FA2 (F2, A2, A3): revisión anual del PETI en el Comité de TI y trazabilidad para los entes de control (proyectos: P1.1, P4.1)"]),
        ("DA", "Reducir debilidades y evitar amenazas", ROJO,
         ["DA1 (D7, A1): gestión de incidentes con responsable dedicado (proyectos: P1.4, P1.1)",
          "DA2 (D5, A4): migrar servicios críticos, IPv6 y plan de capacidad (proyectos: P2.4, P1.6, P3.3)",
          "DA3 (D6, A5): programa de uso y apropiación y procedimientos actualizados (proyectos: P2.6, P1.2)"]),
    ]
    W, H = 1200, 540
    doc = fitz.open()
    pg = doc.new_page(width=W, height=H)
    for i, (cod, sub, col, items) in enumerate(estr):
        x0 = 30 + (i % 2) * 575
        y0 = 30 + (i // 2) * 245
        r = fitz.Rect(x0, y0, x0 + 565, y0 + 235)
        pg.draw_rect(r, color=col, fill=(1, 1, 1), width=1.5, radius=0.03)
        pg.draw_rect(fitz.Rect(r.x0, r.y0, r.x1, r.y0 + 32), color=col, fill=col, radius=0.03)
        pg.insert_text((r.x0 + 12, r.y0 + 22), f"Estrategias {cod}: {sub}", fontsize=12, fontname="hebo", color=(1, 1, 1))
        texto(pg, fitz.Rect(r.x0 + 12, r.y0 + 45, r.x1 - 10, r.y1 - 8), "\n\n".join("- " + t for t in items), 12, "helv", NEGRO, 0)
    pg.insert_text((30, 525), "Fuente: elaboración del equipo. Los códigos F, D, O y A son los de la figura de la DOFA; P1.1 a P4.2 son los proyectos del numeral 8.", fontsize=9, color=(0.3, 0.3, 0.3))
    pg.get_pixmap(dpi=200).save(OUT / "dofa_cruzada.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    dofa()
    dofa_cruzada()
    organigrama_ti_objetivo()

    presupuesto()
    mapa_ruta()
    indicadores()
    infraestructura()


    arquitectura_objetivo()
    print("Figuras escritas en", OUT)
