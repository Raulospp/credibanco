"""Convierte el PETI en Markdown a .docx usando los estilos de la Plantilla PETI del MinTIC (Anexo 2).

Uso:
    python .claude/skills/guia-peti/scripts/md_a_docx.py <entrada.md> <salida.docx> ["pie de página"]

Sin tercer argumento, el pie de página es "PETI — Clasificación: interno".

Soporta: '#' título del documento, '##'-'####' títulos 1-3, párrafos, '> ' cita, viñetas '- ',
tablas con '|', **negrita**, *cursiva* y `código` (como texto). Inserta un índice que Word
actualiza al abrir (F9 o "Actualizar tabla"). Requiere python-docx.
"""
import os
import re
import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
PLANTILLA = os.path.join(RAIZ, "docs", "Anexo 2. Plantilla PETI.docx")


def documento_vacio(pie):
    d = docx.Document(PLANTILLA)
    cuerpo = d.element.body
    for hijo in list(cuerpo):
        if hijo.tag != qn("w:sectPr"):
            cuerpo.remove(hijo)
    for seccion in d.sections:
        for parte in (seccion.header, seccion.footer, seccion.first_page_header, seccion.first_page_footer,
                      seccion.even_page_header, seccion.even_page_footer):
            for hijo in list(parte._element):
                parte._element.remove(hijo)
            parte._element.append(OxmlElement("w:p"))
        seccion.footer.paragraphs[0].text = pie
        seccion.footer.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    return d


def texto_con_formato(parrafo, texto, tam=None):
    for trozo in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)", texto):
        if not trozo:
            continue
        if trozo.startswith("**"):
            run = parrafo.add_run(trozo[2:-2]); run.bold = True
        elif trozo.startswith("*"):
            run = parrafo.add_run(trozo[1:-1]); run.italic = True
        elif trozo.startswith("`"):
            run = parrafo.add_run(trozo[1:-1])
        else:
            run = parrafo.add_run(trozo)
        if tam:
            run.font.size = Pt(tam)


def sombrear(celda, color):
    tc = celda._element.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), color)
    tc.append(shd)


def agregar_tabla(d, filas):
    filas = [f for f in filas if not all(re.fullmatch(r":?-+:?", c.strip() or "-") for c in f)]
    ncol = max(len(f) for f in filas)
    tabla = d.add_table(rows=0, cols=ncol)
    tabla.style = d.styles["Table Grid"]
    tam = 8 if ncol >= 7 else 9
    for i, fila in enumerate(filas):
        celdas = tabla.add_row().cells
        for j in range(ncol):
            p = celdas[j].paragraphs[0]
            texto_con_formato(p, fila[j] if j < len(fila) else "", tam)
            if i == 0:
                for run in p.runs:
                    run.bold = True; run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                sombrear(celdas[j], "3366CC")
    d.add_paragraph()


def agregar_indice(d):
    p = d.add_paragraph()
    run = p.add_run()
    for tipo, texto in (("begin", None), (None, 'TOC \\o "1-2" \\h \\z \\u'), ("separate", None), ("end", None)):
        if tipo:
            fld = OxmlElement("w:fldChar"); fld.set(qn("w:fldCharType"), tipo); run._r.append(fld)
            if tipo == "separate":
                t = OxmlElement("w:t"); t.text = "Actualice el índice: clic derecho > Actualizar campo."
                run._r.append(t)
        else:
            instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = texto
            run._r.append(instr)
    d.add_page_break()


def convertir(entrada, salida, pie="PETI — Clasificación: interno"):
    # Los comentarios HTML (<!-- … -->) son notas de trabajo y no pasan al Word.
    lineas = re.sub(r"<!--.*?-->", "", open(entrada, encoding="utf8").read(), flags=re.S).splitlines()
    d = documento_vacio(pie)
    tabla, primer_h2 = [], True
    for linea in lineas + [""]:
        if linea.strip().startswith("|"):
            tabla.append([c.strip() for c in linea.strip().strip("|").split("|")])
            continue
        if tabla:
            agregar_tabla(d, tabla); tabla = []
        s = linea.rstrip()
        if not s.strip():
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            nivel, texto = len(m.group(1)), m.group(2)
            if nivel == 1:
                titulo = d.add_paragraph(texto, style="Title")
                titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                if nivel == 2 and primer_h2:
                    # Lo que va antes del primer numeral es la portada: el índice empieza en otra página.
                    d.add_page_break()
                    agregar_indice(d); primer_h2 = False
                elif nivel == 2:
                    d.add_page_break()
                d.add_paragraph(texto, style=f"Heading {nivel - 1}")
        elif primer_h2:
            p = d.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            texto_con_formato(p, s[2:] if s.startswith("> ") else s)
        elif s.startswith("> "):
            texto_con_formato(d.add_paragraph(style="Quote"), s[2:])
        elif re.match(r"^\s*[-*]\s+", s):
            p = d.add_paragraph(style="List Paragraph")
            texto_con_formato(p, "• " + re.sub(r"^\s*[-*]\s+", "", s))
        else:
            texto_con_formato(d.add_paragraph(), s)
    d.save(salida)
    print("Generado:", salida)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    convertir(*sys.argv[1:4])
