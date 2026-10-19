"""Extrae a texto plano los documentos de referencia del PETI (PDF, DOCX, XLSX).

Uso:
    python .claude/skills/guia-peti/scripts/extraer_referencias.py [carpeta_salida]

Sin argumento escribe en <temp>/peti-referencias. Solo usa la biblioteca estándar
y, para los PDF, el ejecutable `pdftotext` (Poppler; viene con algunas instalaciones de
Git Bash). Si no está, intenta con la librería `pypdf` (`pip install pypdf`).

Salidas:
    guia.txt          Guía MGGTI.GE.ES.03 v3.0 (el archivo se llama .01)
    plantilla.txt     Anexo 2, texto completo sin líneas vacías
    plantilla_titulos.txt  Anexo 2, solo títulos con su estilo
    anexo1.txt        Anexo 1, una sección por hoja, celdas como REF=valor
    minciencias.txt   PETI MinCiencias (referente del profesor)
    mintic.txt        PETI MinTIC (referente del profesor)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DOCS = os.path.join(RAIZ, "docs")


def buscar(patron):
    for nombre in os.listdir(DOCS):
        if re.search(patron, nombre, re.I):
            return os.path.join(DOCS, nombre)
    return None


def pdf_a_texto(origen, destino):
    exe = shutil.which("pdftotext")
    if not exe:
        try:
            from pypdf import PdfReader
        except ImportError:
            print("  ni pdftotext ni pypdf están disponibles; se omite", os.path.basename(origen))
            return False
        paginas = PdfReader(origen).pages
        with open(destino, "w", encoding="utf8") as f:
            for i, pagina in enumerate(paginas, 1):
                f.write(f"\n\f--- página {i} ---\n{pagina.extract_text() or ''}")
        return True
    # Copia a una ruta ASCII: pdftotext falla con rutas que llevan tildes.
    with tempfile.TemporaryDirectory() as tmp:
        copia = os.path.join(tmp, "entrada.pdf")
        shutil.copyfile(origen, copia)
        subprocess.run([exe, "-layout", "-enc", "UTF-8", copia, destino], check=True)
    return True


def texto_runs(xml):
    return "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml, re.S))


def docx_a_texto(origen, destino, destino_titulos):
    xml = zipfile.ZipFile(origen).read("word/document.xml").decode("utf8")
    lineas, titulos = [], []
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        texto = texto_runs(p).strip()
        if not texto:
            continue
        lineas.append(texto)
        estilo = re.findall(r'<w:pStyle w:val="([^"]+)"', p)
        if estilo and re.match(r"(?i)(heading|t.?tulo)", estilo[0]):
            titulos.append(f"{estilo[0]} | {texto}")
    with open(destino, "w", encoding="utf8") as f:
        f.write("\n".join(lineas))
    with open(destino_titulos, "w", encoding="utf8") as f:
        f.write("\n".join(titulos))


def xlsx_a_texto(origen, destino):
    z = zipfile.ZipFile(origen)
    compartidas = []
    if "xl/sharedStrings.xml" in z.namelist():
        sx = z.read("xl/sharedStrings.xml").decode("utf8")
        for si in re.findall(r"<si>(.*?)</si>", sx, re.S):
            compartidas.append("".join(re.findall(r"<t[^>]*>(.*?)</t>", si, re.S)))
    libro = z.read("xl/workbook.xml").decode("utf8")
    nombres = re.findall(r'<sheet [^>]*name="([^"]+)"', libro)
    hojas = sorted(
        (n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml$", n)),
        key=lambda n: int(re.findall(r"\d+", n)[0]),
    )
    salida = []
    for i, hoja in enumerate(hojas):
        salida.append(f"\n######## HOJA {i + 1}: {nombres[i] if i < len(nombres) else hoja}")
        sx = z.read(hoja).decode("utf8")
        for fila in re.findall(r"<row[^>]*>(.*?)</row>", sx, re.S):
            celdas = []
            for attrs, cuerpo in re.findall(r"<c ([^>]*?)(?:/>|>(.*?)</c>)", fila, re.S):
                v = re.findall(r"<v>(.*?)</v>", cuerpo or "", re.S)
                tipo = re.findall(r'\bt="(\w+)"', attrs)
                ref = re.findall(r'r="([A-Z]+\d+)"', attrs)
                if v:
                    valor = compartidas[int(v[0])] if tipo and tipo[0] == "s" else v[0]
                else:
                    valor = "".join(re.findall(r"<t[^>]*>(.*?)</t>", cuerpo or "", re.S))
                if valor.strip():
                    celdas.append((ref[0] if ref else "") + "=" + valor.strip())
            if celdas:
                salida.append(" | ".join(celdas))
    with open(destino, "w", encoding="utf8") as f:
        f.write("\n".join(salida))


def main():
    # La consola de Windows usa cp1252 y el nombre del PDF de MinCiencias trae tildes combinadas.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    salida =sys.argv[1] if len(sys.argv) > 1 else os.path.join(tempfile.gettempdir(), "peti-referencias")
    os.makedirs(salida, exist_ok=True)

    trabajos = [
        (r"^MGGTI.*\.pdf$", lambda o: pdf_a_texto(o, os.path.join(salida, "guia.txt"))),
        (r"^Anexo 2.*\.docx$", lambda o: docx_a_texto(
            o, os.path.join(salida, "plantilla.txt"), os.path.join(salida, "plantilla_titulos.txt"))),
        (r"^Anexo 1.*\.xlsx$", lambda o: xlsx_a_texto(o, os.path.join(salida, "anexo1.txt"))),
        (r"^Plan-Estrat.*\.pdf$", lambda o: pdf_a_texto(o, os.path.join(salida, "minciencias.txt"))),
        (r"^articles-274095.*\.pdf$", lambda o: pdf_a_texto(o, os.path.join(salida, "mintic.txt"))),
    ]
    for patron, accion in trabajos:
        origen = buscar(patron)
        if not origen:
            print("  no encontrado:", patron)
            continue
        accion(origen)
        print("  ok:", os.path.basename(origen))
    print("Salida en", salida)


if __name__ == "__main__":
    main()
