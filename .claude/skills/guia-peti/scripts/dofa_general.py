"""Arma la matriz DOFA general de TI a partir de las siete matrices por dominio.

Uso:
    python .claude/skills/guia-peti/scripts/dofa_general.py

Lee las tablas "DOFA del dominio ..." de docs/dofa-por-dominio.md, numera cada factor (F1..., D1..., O1..., A1...)
con el dominio al que pertenece y su referencia de hallazgo, y escribe (o reemplaza) la tabla
"Matriz DOFA general de TI" al final del mismo archivo. Las citas largas de fuentes se omiten: están en las
matrices por dominio y en los numerales 6.1 a 6.7 del PETI.
"""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
ARCHIVO = os.path.join(RAIZ, "docs", "dofa-por-dominio.md")
CORTO = {"Estrategia de TI": "Estrategia", "Gobierno de TI": "Gobierno", "Información": "Información",
         "Sistemas de información": "Sistemas", "Infraestructura de TI": "Infraestructura",
         "Uso y apropiación": "Uso y apropiación", "Seguridad de la información": "Seguridad"}
TITULO = "Tabla: Matriz DOFA general de TI {T4}"
PREFIJO = {"Estrategia": "E", "Gobierno": "G", "Información": "I", "Sistemas": "S", "Infraestructura": "T",
           "Uso y apropiación": "U", "Seguridad": "SE"}


def factores(celda):
    celda = re.sub(r"^\*\*[^*]+\*\*\s*", "", celda.strip())
    partes = re.split(r";(?![^()]*\))", celda)
    salida = []
    for p in partes:
        p = p.strip()
        # se conservan las referencias de hallazgo o de riesgo cortas (E1, SE4, R02) y se quitan las citas de fuentes
        p = re.sub(r"\s*\((?![A-Z]{1,2}\d+(?:[,; y]+[A-Z]{1,2}\d+)*\))[^()]*(?:\([^()]*\)[^()]*)*\)", "", p)
        if p:
            salida.append(p[0].upper() + p[1:])
    return salida


def main():
    texto = open(ARCHIVO, encoding="utf8").read()
    if TITULO in texto:
        texto = texto[:texto.index("\n\n" + TITULO)] if "\n\n" + TITULO in texto else texto[:texto.index(TITULO)]
    cuadrantes = {"F": [], "D": [], "O": [], "A": []}
    patron = r"Tabla: DOFA del dominio (.+?) \{T4\}\n\n[^\n]*\n[^\n]*\n(\| Interno [^\n]*)\n(\| Externo [^\n]*)"
    for m in re.finditer(patron, texto):
        dom = CORTO[m.group(1)]
        interno = [c.strip() for c in m.group(2).strip("|").split("|")]
        externo = [c.strip() for c in m.group(3).strip("|").split("|")]
        for letra, celda in (("F", interno[1]), ("D", interno[2]), ("O", externo[1]), ("A", externo[2])):
            for f in factores(celda):
                # el mismo factor puede estar en dos dominios (p. ej., la sensibilización): se deja una vez
                clave = re.sub(r"\s*\([^()]*\)$|en seguridad ", "", f.lower()).strip()
                previo = next((k for k, (_, g) in enumerate(cuadrantes[letra])
                               if re.sub(r"\s*\([^()]*\)$|en seguridad ", "", g.lower()).strip() == clave), None)
                if previo is None:
                    cuadrantes[letra].append((dom, f))
                else:
                    d0, g = cuadrantes[letra][previo]
                    refs = re.findall(r"\(([^()]*)\)$", g) + re.findall(r"\(([^()]*)\)$", f)
                    base = re.sub(r"\s*\([^()]*\)$", "", g)
                    cuadrantes[letra][previo] = (f"{d0} y {dom}", f"{base} ({', '.join(refs)})" if refs else base)

    def lista(letra, nombre):
        # código por dominio, como los hallazgos del numeral 6: F-E1 (estrategia), D-SE2 (seguridad)...
        cuenta, items = {}, []
        for dom, f in cuadrantes[letra]:
            pref = next(v for k, v in PREFIJO.items() if dom.startswith(k))  # "Uso y apropiación y Seguridad" -> U
            cuenta[pref] = cuenta.get(pref, 0) + 1
            items.append(f"{letra}-{pref}{cuenta[pref]}. [{dom}] {f}.")
        return f"**{nombre}:** " + " ".join(items)

    tabla = (f"{TITULO}\n\n| Origen | Habilitadores | Barreras |\n|---|---|---|\n"
             f"| Interno | {lista('F', 'Fortalezas')} | {lista('D', 'Debilidades')} |\n"
             f"| Externo | {lista('O', 'Oportunidades')} | {lista('A', 'Amenazas')} |\n")
    open(ARCHIVO, "w", encoding="utf8").write(texto.rstrip() + "\n\n" + tabla)
    print({k: len(v) for k, v in cuadrantes.items()})


if __name__ == "__main__":
    main()
