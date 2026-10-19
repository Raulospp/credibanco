"""Llena una copia del Anexo 1 (Herramientas para la construcción del PETI) con el contenido del PETI.

Uso:
    python .claude/skills/guia-peti/scripts/llenar_anexo1.py <peti.md> <salida.xlsx>

No cambia el formato del libro: edita el XML de cada hoja y solo escribe valores en las celdas de las
tablas, así que se conservan estilos, celdas combinadas, logos, comentarios y listas. Cuando una tabla
necesita más filas o columnas de las que trae la plantilla, las nuevas copian el estilo de la fila o la
columna vecina. Solo biblioteca estándar más lxml (viene con python-docx).
"""
import copy
import os
import re
import shutil
import sys
import tempfile
import zipfile

from lxml import etree

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
ANEXO = os.path.join(RAIZ, "docs", "Anexo 1. Herramientas_para_la_construccion_del_PETI.xlsx")
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
N = "{%s}" % NS


# ---------- utilidades de celdas ----------

def col_num(letras):
    n = 0
    for ch in letras:
        n = n * 26 + ord(ch) - 64
    return n


def col_letras(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def partir(ref):
    m = re.match(r"([A-Z]+)(\d+)", ref)
    return m.group(1), int(m.group(2))


class Hoja:
    def __init__(self, ruta):
        self.ruta = ruta
        self.arbol = etree.parse(ruta)
        self.datos = self.arbol.getroot().find(N + "sheetData")

    def fila(self, r, crear=True):
        for f in self.datos.findall(N + "row"):
            n = int(f.get("r"))
            if n == r:
                return f
            if n > r:
                if not crear:
                    return None
                nueva = etree.Element(N + "row", r=str(r))
                f.addprevious(nueva)
                return nueva
        if not crear:
            return None
        nueva = etree.SubElement(self.datos, N + "row", r=str(r))
        return nueva

    def celda(self, ref, crear=True):
        col, r = partir(ref)
        f = self.fila(r, crear)
        if f is None:
            return None
        for c in f.findall(N + "c"):
            ccol, _ = partir(c.get("r"))
            if ccol == col:
                return c
            if col_num(ccol) > col_num(col):
                if not crear:
                    return None
                nueva = etree.Element(N + "c", r=ref)
                c.addprevious(nueva)
                return nueva
        if not crear:
            return None
        return etree.SubElement(f, N + "c", r=ref)

    def estilo(self, ref):
        c = self.celda(ref, crear=False)
        return c.get("s") if c is not None else None

    def poner(self, ref, valor, estilo_de=None):
        c = self.celda(ref)
        if estilo_de and c.get("s") is None and self.estilo(estilo_de):
            c.set("s", self.estilo(estilo_de))
        for hijo in list(c):
            c.remove(hijo)
        if "t" in c.attrib:
            del c.attrib["t"]
        if valor is None or valor == "":
            return
        c.set("t", "inlineStr")
        is_ = etree.SubElement(c, N + "is")
        t = etree.SubElement(is_, N + "t")
        t.text = str(valor)
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        # La altura la calcula Excel según el texto (no se fija una altura manual)
        f = self.fila(partir(ref)[1])
        for a in ("ht", "customHeight"):
            if a in f.attrib:
                del f.attrib[a]

    def copiar_estilo_fila(self, origen, destino, desde="A", hasta="Z"):
        for n in range(col_num(desde), col_num(hasta) + 1):
            letra = col_letras(n)
            s = self.estilo(f"{letra}{origen}")
            if s:
                self.celda(f"{letra}{destino}").set("s", s)

    def copiar_estilo_col(self, origen, destino, filas):
        for r in filas:
            s = self.estilo(f"{origen}{r}")
            if s:
                self.celda(f"{destino}{r}").set("s", s)

    def combinaciones(self):
        mc = self.arbol.getroot().find(N + "mergeCells")
        return mc

    def combinar(self, rango):
        mc = self.combinaciones()
        if mc is None:
            mc = etree.Element(N + "mergeCells")
            self.datos.addnext(mc)
        etree.SubElement(mc, N + "mergeCell", ref=rango)
        mc.set("count", str(len(mc)))

    def descombinar(self, rango):
        mc = self.combinaciones()
        for m in list(mc):
            if m.get("ref") == rango:
                mc.remove(m)
        mc.set("count", str(len(mc)))

    def guardar(self):
        self.arbol.write(self.ruta, xml_declaration=True, encoding="UTF-8", standalone=True)


# ---------- lectura del PETI ----------

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


def leer_peti(ruta):
    texto = open(ruta, encoding="utf8").read() + "\n\n" + texto_auxiliar(ruta)
    lineas = texto.splitlines()
    tablas, i = {}, 0
    while i < len(lineas):
        m = re.match(r"^Tabla:\s*(.*?)\s*\{T\d+\}", lineas[i])
        if m:
            j = i + 1
            while j < len(lineas) and not lineas[j].startswith("|"):
                j += 1
            filas = []
            while j < len(lineas) and lineas[j].startswith("|"):
                celdas = [c.strip() for c in lineas[j].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c or "-") for c in celdas):
                    filas.append(celdas)
                j += 1
            tablas.setdefault(m.group(1), filas)
            i = j
        else:
            i += 1
    return texto, tablas


def parrafo_tras(texto, titulo):
    i = texto.index(titulo)
    resto = texto[i + len(titulo):].strip().split("\n\n")[0]
    return resto.strip()


def limpiar(s):
    return s.replace("**", "")


# ---------- llenado por hoja (Valor+, PETI 2027-2030) ----------

EQUIPO = {"hannyer": "Hannyer Arce Ararat", "kevin": "Kevin Steven Tabares Blanco", "raul": "Raul Guillermo Orobio Ospina",
          "ever": "Ever Jonatan Delgado Chaguendo", "juan": "Juan Jose Muñoz", "luis": "Luis Fernando Narvaes Marin"}
FECHA = "5 de octubre de 2026"
MES = "P"  # columna de octubre en la hoja Actividad 3

# Factores clave de la DOFA general (los mismos de la figura del numeral 6)
DOFA_GENERAL = {
    "F": ["F1 ANS de clientes cumplidos: 95,71 % (Estrategia)", "F2 Riesgos con tres líneas de defensa y Comité de Riesgos (Gobierno)",
          "F3 Activos de información inventariados; PINAR vigente (Información)", "F4 ERP financiero en SaaS; software propio registrado (Sistemas)",
          "F5 Nube AWS, Oracle y Azure sin hallazgos críticos (Infraestructura)", "F6 Boletín mensual de ciberseguridad (Uso y apropiación)",
          "F7 SGSI actualizado al MSPI 2025; 100 % de ataques bloqueados (Seguridad)"],
    "D": ["D1 Visión y objetivos de TI sin metas; sin catálogo de servicios (Estrategia)",
          "D2 Ninguna instancia decide sobre TI; auditoría de TI en 49 %; sin cargo de seguridad (Gobierno)",
          "D3 Datos sin responsables ni calidad; archivos sin versiones (Información)",
          "D4 Procesos comercial y de servicio en Excel; ERP sin decidir (Sistemas)",
          "D5 Servicios críticos en sitio; sin plan de capacidad; IPv6 atrasado (Infraestructura)",
          "D6 Sin estrategia de uso y apropiación (Uso y apropiación)", "D7 Incidentes sin gestión constante; recuperación sin probar (Seguridad)"],
    "O": ["O1 PEI y Plan de Desarrollo de Antioquia que demandan TI; 48 contratos", "O2 PMO en construcción y MIPG con Gobierno Digital en 86,3",
          "O3 Oferta madura de ERP, CRM y BPMS en la nube", "O4 Demanda de SOC por los municipios; IA que ya se vende",
          "O5 Acuerdo 001 de 2024 del AGN y MSPI como guía"],
    "A": ["A1 Ransomware y phishing contra entidades públicas", "A2 Fin del PEI (2027) y cambio de gobierno departamental (2028)",
          "A3 Hallazgos de la Contraloría: control fiscal interno en 2,0", "A4 Dependencia de proveedores SaaS y del proveedor de internet",
          "A5 Rotación de personal y procedimientos desactualizados"],
}


def cod_brecha(x):
    return ("B" + x[4:]) if x.startswith("BRE-") else x


def llenar(md, salida):
    texto, T = leer_peti(md)
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(ANEXO) as z:
        z.extractall(tmp)
    hojas = {"Actividad 1": 2, "Actividad 3": 3, "Actividad 4A": 4, "Actividad 4B": 5, "Actividad 4C": 6,
             "Actividad 4D": 7, "Actividad 5": 8, "Actividad 6": 9, "Actividad 7": 10, "Actividad 8": 11,
             "Actividad 11": 12, "Actividad 12": 13, "Actividad 13": 14, "Actividad 14 A": 15,
             "Actividad 14 B": 16, "Actividad 17": 17}
    H = {k: Hoja(os.path.join(tmp, "xl", "worksheets", f"sheet{v}.xml")) for k, v in hojas.items()}

    # Actividad 1: equipo y partes interesadas
    h = H["Actividad 1"]
    for k, f in enumerate(T["Equipo del PETI"][1:]):
        r = 10 + k
        h.poner(f"A{r}", "Equipo académico del PETI (rol del área de TI)")
        h.poner(f"B{r}", f[0])
        h.poner(f"D{r}", f"{f[1]}. Actividades {f[3]}")
        h.poner(f"E{r}", "No se publica")
        h.poner(f"F{r}", "No se publica")
        h.poner(f"G{r}", "No: equipo académico externo a la organización")
    for k, f in enumerate(T["Partes interesadas en la organización"][1:]):  # Rol | Área | Capacidad | Aporte
        r = 20 + k
        if r > 25:
            h.copiar_estilo_fila(25, r, "A", "G")
            h.combinar(f"B{r}:C{r}")
        h.poner(f"A{r}", f[1])
        h.poner(f"B{r}", f"Rol: {f[0]} (no se nombran personas)")
        h.poner(f"D{r}", f"{f[3]}. Capacidad de decisión: {f[2]}")
        h.poner(f"E{r}", "No aplica")
        h.poner(f"F{r}", "No aplica")

    # Actividad 3: cronograma (todas las actividades el 5 de octubre de 2026; socializar no se nombra)
    h = H["Actividad 3"]
    h.poner("G9", "2026")
    e = EQUIPO
    plan = {
        11: (e["kevin"], "Contexto y modelo operativo (numeral 5)"),
        12: (e["kevin"], "Mapa de procesos y alineación de TI con los procesos (numeral 5.1)"),
        13: (e["kevin"], "Marco normativo (numeral 3)"),
        14: (e["kevin"], "Motivadores estratégicos (numeral 5)"),
        15: (e["kevin"], "Compromisos con plazo CE-01 a CE-10 (hoja Actividad 5)"),
        16: (e["kevin"], "Servicios de negocio; trámites y OPA no aplican (numerales 5.1.6 a 5.1.8)"),
        17: (e["raul"], "Situación actual de los siete dominios (numeral 6)"),
        18: (e["ever"], "Catálogo de sistemas de información (numeral 6.4.1 y Anexo F)"),
        19: (e["raul"], "Entidades de información frente a componentes (numeral 6.3.2)"),
        20: (e["ever"], "Servicios y elementos de infraestructura (numerales 6.5.1 y 6.5.2)"),
        21: (e["raul"], "Catálogo de servicios de TI (numeral 6.1.3 y Anexo F)"),
        22: (e["raul"], "Diagnóstico y DOFA de estrategia de TI (numeral 6.1)"),
        23: (e["raul"], "Diagnóstico y DOFA de gobierno de TI (numeral 6.2)"),
        24: (e["ever"], "Diagnóstico y DOFA de sistemas de información (numeral 6.4)"),
        25: (e["ever"], "Diagnóstico y DOFA de seguridad (numeral 6.7)"),
        26: (e["raul"], "Diagnóstico y DOFA de información (numeral 6.3)"),
        27: (e["ever"], "Diagnóstico y DOFA de infraestructura (numeral 6.5)"),
        28: (e["ever"], "Diagnóstico y DOFA de uso y apropiación (numeral 6.6)"),
        29: (e["ever"], "Tendencias frente a servicios y procesos (numeral 6)"),
        30: (e["juan"], "Misión, visión, objetivos y metas de TI (numeral 7.1)"),
        31: (e["juan"], "Servicios de TI objetivo (numeral 7.1.4)"),
        32: (e["juan"], "Situación objetivo por dominio y oportunidades (numerales 7 y 8)"),
        33: (e["juan"], "Catálogo de brechas (numeral 8)"),
        34: (e["luis"], "Catálogo de proyectos, fichas, presupuesto y mapa de ruta (numeral 8)"),
        35: (e["juan"], "Iniciativas de otros planes IPGD001 a IPGD006 (numeral 8)"),
        36: (e["luis"], "Hojas de vida de indicadores (numeral 7.1.6) y riesgos (numeral 7.2)"),
        37: (e["hannyer"], "Documento PETI consolidado"),
    }
    for r, (resp, sal) in plan.items():
        h.poner(f"D{r}", FECHA)
        h.poner(f"E{r}", resp)
        h.poner(f"F{r}", sal)
        h.poner(f"{MES}{r}", "X")

    # Actividad 4A: ficha de la entidad, estrategia, objetivos y metas
    h = H["Actividad 4A"]
    h.poner("C6", "Valor + S.A.S. (Valor+)")
    h.poner("F6", "Medellín, Antioquia")
    h.poner("C7", "Departamental; nivel descentralizado por servicios (filial del IDEA)")
    h.poner("F7", "No se encontró el total ejecutado. Inversión 2025: $2.007 millones comprometidos de $2.134 millones (Informe de gestión 2025, pág. 157)")
    h.poner("C8", "Sociedad por acciones simplificada de economía mixta (IDEA 98,95 %, FEIDEA 1,05 %); régimen de empresa industrial y comercial del Estado (Ley 489 de 1998, art. 97)")
    h.poner("F8", "No publicado por separado")
    h.poner("C9", "Territorial")
    h.poner("F9", "25 de noviembre de 2024: aprobación del PEI 2024-2027, Acta 006 del Comité Institucional de Gestión y Desempeño")
    h.poner("F10", "28 de enero de 2026 (PETI 2026-2027, versión 4.0); este PETI 2027-2030, octubre de 2026 (propuesta)")
    h.poner("F11", "No aplica plan sectorial propio; referencia: Plan de Desarrollo de Antioquia 2024-2027 \"Por Antioquia Firme\"")
    h.poner("C13", limpiar(parrafo_tras(texto, "#### Misión")))
    h.poner("C14", limpiar(parrafo_tras(texto, "#### Visión")))
    ocs = T["Objetivos corporativos"][1:]
    mcs = T["Metas corporativas e indicadores de referencia"][1:]  # Objetivo | Indicador | Meta | Resultado | Fuente
    r = 18
    for oc in ocs:
        metas = [mc for mc in mcs if mc[0] == oc[0]]
        h.poner(f"A{r}", oc[0])
        h.poner(f"B{r}", oc[1])
        for n, mc in enumerate(metas, 1):
            h.poner(f"D{r}", f"M{oc[0][2:]}.{n}")
            h.poner(f"E{r}", f"{mc[1]} (meta 2025: {mc[2]})")
            h.poner(f"F{r}", f"{mc[3]} en 2025 ({mc[4]})")
            r += 1
        if not metas:
            r += 1

    # Actividad 4B: procesos frente a sistemas de información (T total, P parcial)
    h = H["Actividad 4B"]
    sis = ["ERP (SICOF)", "Mesa de ayuda (OTRS, GLPI)", "FURAG y Power BI", "Sitio web e intranet",
           "Telefonía IP y contact center", "SECOP y Gestión Transparente", "Office 365, Visio, Project y Carriel"]
    for k, s in enumerate(sis):
        h.poner(f"{col_letras(4 + k)}7", s)
    cobertura = {"PE01": {2: "P", 5: "P"}, "PE03": {6: "P"}, "PE04": {0: "P"}, "PE05": {3: "P", 6: "P"}, "PE06": {6: "P"},
                 "PM01": {1: "P"}, "PM03": {4: "P"}, "PA01": {5: "P"}, "PA02": {5: "P"}, "PA03": {3: "T"},
                 "PA05": {6: "P"}, "PA06": {0: "T"}, "PV01": {5: "P"}}
    procesos = []
    for nombre in ("Procesos estratégicos", "Procesos misionales", "Procesos de apoyo", "Procesos de evaluación y control"):
        procesos += T[nombre][1:]
    for k, p in enumerate(procesos):
        r = 8 + k
        h.poner(f"A{r}", p[0])
        h.poner(f"B{r}", p[1])
        for c in range(4, 11):
            h.poner(f"{col_letras(c)}{r}", "")
        for idx, v in cobertura.get(p[0], {}).items():
            h.poner(f"{col_letras(4 + idx)}{r}", v)
    h.poner("A28", "Fuente: elaboración del equipo a partir de la alineación de TI con los procesos (numeral 5.1.5). PE02, PM02 y PA04 no tienen sistema")

    # Actividad 4C: servicios de negocio (Valor+ no tiene trámites ni OPA)
    h = H["Actividad 4C"]
    extra = {
        "S01": ("Gerencia de Operaciones; Gerencia de TI", "Entidades públicas (Gobernación, Medellín, Envigado)", "Contratos con cada entidad; Ley 1150 de 2007, art. 14", "PM03, PM01", "Parcialmente automatizado y en linea", ["Contact center", "Correo", "SMS e IVR", "Puntos de atención"]),
        "S02": ("Gerencia de Operaciones; Gestión Documental; Gerencia de TI", "IDEA, Indeportes, Gobernación, Envigado, Pascual Bravo", "Ley 594 de 2000; Acuerdo 001 de 2024 del AGN", "PM03, PA05", "Parcialmente automatizado", ["Mesa de ayuda", "Correo", "Atención en sede del cliente"]),
        "S03": ("Dirección de Planeación y Proyectos", "Gobernación y municipios", "Contratos con cada entidad", "PE03", "Totalmente manual", ["Reuniones", "Correo"]),
        "S04": ("Gerencia de TI; Dirección Comercial", "Gobernación, IDEA, Ferrocarril de Antioquia, Lotería de Medellín, Crediantioquia", "Contratos con ANS; Decreto 767 de 2022", "PM01, PM02", "Parcialmente automatizado y en linea", ["Mesa de servicio", "Correo", "Portal"]),
        "S05": ("Gerencia de TI", "IDEA, Lotería de Medellín, municipios", "Resolución 500 de 2021 (MSPI); Decreto 338 de 2022", "PM01", "Automatizado parcialmente", ["Portal del SOC", "Correo"]),
        "S06": ("Gerencia de Operaciones", "Departamento de Antioquia", "Contrato de alumbrado público", "PM03", "No aplica: sin rol de TI (fuera del alcance)", ["—"]),
    }
    for k, s in enumerate(T["Servicios de negocio"][1:]):  # ID | Línea | Ejemplos | Rol de la TI
        r = 9 + k
        areas, usuario, norma, procs, auto, canales = extra[s[0]]
        h.poner(f"A{r}", s[0])
        h.poner(f"B{r}", s[1])
        h.poner(f"C{r}", f"{s[2]}. Rol de la TI: {s[3]}")
        h.poner(f"D{r}", "Servicio")
        h.poner(f"E{r}", "N (Valor+ no tiene trámites para la ciudadanía)")
        h.poner(f"F{r}", areas)
        h.poner(f"G{r}", usuario)
        h.poner(f"H{r}", norma)
        h.poner(f"I{r}", procs)
        for c in "JKLMNOPQ":
            h.poner(f"{c}{r}", "Sin dato público")
        h.poner(f"R{r}", "Sin dato público")
        h.poner(f"S{r}", auto)
        for j, canal in enumerate(canales):
            h.poner(f"{col_letras(20 + j)}{r}", canal)

    # Actividad 4D: normatividad
    h = H["Actividad 4D"]
    for k, f in enumerate(T["Marco normativo"][1:]):  # Norma | Qué exige | Aplicación
        r = 7 + k
        if r > 26:
            h.copiar_estilo_fila(26, r, "A", "E")
            h.combinar(f"B{r}:C{r}")
        h.poner(f"A{r}", f"N{k + 1:02d}")
        h.poner(f"B{r}", f[0])
        h.poner(f"D{r}", f[1])
        h.poner(f"E{r}", f[2])

    # Actividad 5: planes externos y compromisos (motivadores del numeral 5)
    h = H["Actividad 5"]
    plazos = ["2027 (fin del PEI 2024-2027)", "Cada vigencia 2027-2030", "2027 (cierre del Plan de Mejoramiento Institucional)",
              "Reporte anual del FURAG", "Evaluación anual del ITA", "2027-2028 (implantación de la PMO)",
              "Según convalidación de las TRD y TVD; PINAR hasta 2027", "2027 (fases 2 y 3 del BCP/DRP) y operación continua del MSPI",
              "Plan de mejoramiento ante la Contraloría (vigencia 2026)", "2027 (fin del Plan de Desarrollo 2024-2027)"]
    for k, f in enumerate(T["Motivadores estratégicos"][1:]):  # Motivador | Qué exige | Fuente
        r = 8 + k
        if r > 14:
            h.copiar_estilo_fila(14, r, "A", "E")
            h.combinar(f"B{r}:C{r}")
        h.poner(f"A{r}", f"CE-{k + 1:02d}")
        h.poner(f"B{r}", f"{f[0]} ({f[2]})")
        h.poner(f"D{r}", f[1])
        h.poner(f"E{r}", plazos[k] if k < len(plazos) else "Vigencia 2027-2030")

    # Actividad 6: DOFA general en la matriz de la plantilla y una matriz por dominio debajo
    h = H["Actividad 6"]

    def matriz(fila0, titulo, f, d, o, a):
        if titulo:
            h.poner(f"B{fila0 - 1}", titulo)
        h.poner(f"B{fila0 + 2}", f)
        h.poner(f"C{fila0 + 2}", d)
        h.poner(f"B{fila0 + 4}", o)
        h.poner(f"C{fila0 + 4}", a)

    g = DOFA_GENERAL
    matriz(4, None, "\n".join(g["F"]), "\n".join(g["D"]), "\n".join(g["O"]), "\n".join(g["A"]))
    nombres = {"Estrategia": "Estrategia de TI", "Gobierno": "Gobierno de TI", "Información": "Información",
               "Sistemas": "Sistemas de información", "Infraestructura": "Infraestructura de TI",
               "Uso y apropiación": "Uso y apropiación", "Seguridad": "Seguridad de la información"}
    for k, fila in enumerate(T["DOFA por dominio de TI"][1:]):  # Dominio | F | D | O | A
        base = 11 + k * 7
        for off in range(5):
            h.copiar_estilo_fila(4 + off, base + off, "A", "C")
        h.poner(f"B{base}", "Habilitadores")
        h.poner(f"C{base}", "Barreras")
        h.poner(f"A{base + 1}", "Origen Interno")
        h.poner(f"B{base + 1}", "Fortalezas")
        h.poner(f"C{base + 1}", "Debilidades")
        h.poner(f"A{base + 3}", "Origen Externo")
        h.poner(f"B{base + 3}", "Oportunidades")
        h.poner(f"C{base + 3}", "Amenazas")
        for rango in (f"A{base + 1}:A{base + 2}", f"A{base + 3}:A{base + 4}"):
            h.combinar(rango)
        matriz(base, f"DOFA del dominio {nombres.get(fila[0], fila[0])}", fila[1], fila[2], fila[3], fila[4])

    # Actividad 7: tendencias frente a grupos de servicios y procesos
    h = H["Actividad 7"]
    for col, v in {"C9": "ST01-ST08 Servicios de TI internos", "D9": "SC01-SC02 Mesas de servicio y SOC",
                   "E9": "SC03-SC05 Conectividad, desarrollo y nube", "F9": "No aplica: sin trámites",
                   "G9": "No aplica", "H9": "No aplica", "I9": "PM Procesos misionales", "J9": "PE Procesos estratégicos",
                   "K9": "PA y PV Apoyo y evaluación"}.items():
        h.poner(col, v)
    tend = {f[0]: f for f in T["Tendencias tecnológicas frente a servicios y procesos"][1:]}
    mapa = {10: "Nube y SaaS", 11: "Inteligencia artificial generativa", 13: "Analítica de datos",
            17: "Ciberseguridad gestionada (SOC)", 24: "Automatización de procesos (BPMS, RPA)", 25: "Conectividad satelital"}
    manual = {15: ("Base de la capa de integración por API entre ERP, CRM, gestión de servicios y SGDEA (P3.1)", "ST06", "PM03, PA01"),
              19: ("Office 365, Teams y SharePoint como espacio común de documentos (P2.4)", "ST02", "PE05, PA05")}
    no_prior = {12: "No priorizada: sin caso de uso en la TI interna de Valor+",
                14: "No priorizada: sin caso de uso",
                16: "No priorizada en este plan: el desarrollo usa Scrum; se revisará con el procedimiento de ciclo de vida (P1.2)",
                18: "No priorizada: sin caso de uso",
                20: "No priorizada: la automatización de software (RPA) va en la fila de automatización de procesos",
                21: "No priorizada: sin caso de uso",
                22: "Se trata dentro de la IA generativa (P4.2)",
                23: "No priorizada: sin caso de uso"}

    def marca(servicios, procesos_, r):
        ss = set(re.findall(r"S[TC]\d\d", servicios))
        if ss & {f"ST0{i}" for i in range(1, 9)}:
            h.poner(f"C{r}", "X")
        if ss & {"SC01", "SC02"}:
            h.poner(f"D{r}", "X")
        if ss & {"SC03", "SC04", "SC05"}:
            h.poner(f"E{r}", "X")
        pp = set(re.findall(r"P[MEAV]\d\d", procesos_))
        if any(p.startswith("PM") for p in pp):
            h.poner(f"I{r}", "X")
        if any(p.startswith("PE") for p in pp):
            h.poner(f"J{r}", "X")
        if any(p.startswith(("PA", "PV")) for p in pp):
            h.poner(f"K{r}", "X")

    for r, nombre in mapa.items():
        f = tend[nombre]  # Tendencia | Evidencia | Servicios | Procesos | Uso previsto
        if r == 25:
            h.copiar_estilo_fila(24, 25, "A", "K")
        if r in (24, 25):
            h.poner(f"A{r}", nombre)
        h.poner(f"B{r}", f"{f[1]}. Uso previsto: {f[4]}")
        marca(f[2], f[3], r)
    for r, (desc, servicios, procesos_) in manual.items():
        h.poner(f"B{r}", desc)
        marca(servicios, procesos_, r)
    for r, motivo in no_prior.items():
        h.poner(f"B{r}", motivo)

    # Actividad 8: misión, visión, objetivos y metas (se agrega "Año 4" con el formato de "Año 3")
    h = H["Actividad 8"]
    h.poner("C7", limpiar(parrafo_tras(texto, "#### 7.1.1 Misión de TI")))
    h.poner("C8", limpiar(parrafo_tras(texto, "#### 7.1.2 Visión de TI")))
    objetivos = {f[0]: f for f in T["Definición de objetivos estratégicos de TI"][1:]}
    metas = T["Metas de los objetivos estratégicos de TI"][1:]
    for rango in ("A11:A12", "A13:A14", "A15:A16", "A17:A18", "A19:A20"):
        h.descombinar(rango)
    h.copiar_estilo_col("I", "J", range(9, 11))
    h.poner("G10", "Año 1 (2027)")
    h.poner("H10", "Año 2 (2028)")
    h.poner("I10", "Año 3 (2029)")
    h.poner("J10", "Año 4 (2030)", estilo_de="I10")
    if h.estilo("I9"):
        h.celda("J9").set("s", h.estilo("I9"))
    h.descombinar("D9:I9")
    h.combinar("D9:J9")
    r = 11
    for oid in sorted(objetivos):
        suyas = [m for m in metas if m[1] == oid]
        inicio = r
        for m in suyas:
            if r > 20:
                h.copiar_estilo_fila(19, r, "A", "I")
            h.copiar_estilo_col("I", "J", [r])
            h.poner(f"D{r}", m[0])
            h.poner(f"E{r}", f"{m[2]} ({m[3]})")
            h.poner(f"F{r}", m[4])
            h.poner(f"G{r}", m[5])
            h.poner(f"H{r}", m[6])
            h.poner(f"I{r}", m[7])
            h.poner(f"J{r}", m[8])
            r += 1
        o = objetivos[oid]  # ID | Nombre | Descripción | Perspectiva | OC | Hallazgos
        h.poner(f"A{inicio}", oid)
        h.poner(f"B{inicio}", f"{o[1]}: {o[2]}. Perspectiva: {o[3]}")
        h.poner(f"C{inicio}", o[4])
        if r - 1 > inicio:
            h.combinar(f"A{inicio}:A{r - 1}")

    # Actividad 11: catálogo de brechas (B001 = BRE-001)
    h = H["Actividad 11"]
    procesos_brecha = {"BRE-005": "PE03", "BRE-010": "PA06, PA01, PA02, PE04", "BRE-013": "PM02", "BRE-016": "PA05",
                       "BRE-017": "PE04, PE05", "BRE-018": "PM03, PA01", "BRE-020": "PE02", "BRE-021": "PE01"}
    en_curso = {"BRE-009": "Sí, parcial: SOC en implementación (PETI 2026-2027 de Valor+, pág. 44)",
                "BRE-010": "No: ERP en estudio de mercado desde 2024",
                "BRE-011": "Sí, parcial: fase 1 del BCP/DRP terminada en 2025 (Informe de gestión 2025, pág. 88)",
                "BRE-016": "Sí, parcial: SGDEA en diseño (Informe de gestión 2025, pág. 77)"}
    costos = {"Bajo": "Bajo: menos de COP 200 millones", "Medio": "Medio: COP 200 a 700 millones", "Alto": "Alto: más de COP 700 millones"}
    for k, b in enumerate(T["Catálogo de brechas"][1:]):  # ID | Elemento | Dominio | Acción | Justificación | Objetivo | Tiempo | Costo | Proyecto
        r = 8 + k
        if r > 27:
            h.copiar_estilo_fila(27, r, "A", "H")
        h.poner(f"A{r}", cod_brecha(b[0]))
        h.poner(f"B{r}", procesos_brecha.get(b[0], "PM01 (Gestión de TI)"))
        h.poner(f"C{r}", f"{b[0]}: {b[1]} (dominio: {b[2]})")
        h.poner(f"D{r}", b[3])
        h.poner(f"E{r}", f"{b[4]}. Situación objetivo: {b[5]}")
        h.poner(f"F{r}", b[6])
        h.poner(f"G{r}", costos.get(b[7], b[7]))
        h.poner(f"H{r}", f"{en_curso.get(b[0], 'No')}. Proyecto propuesto: {b[8]}")

    # Actividad 12: iniciativas de otros planes (IPGD001 a IPGD006)
    h = H["Actividad 12"]
    for k, f in enumerate(T["Iniciativas de otros planes con componente de TI"][1:]):
        r = 8 + k
        h.poner(f"A{r}", f[0])
        for j, col in enumerate("BCDEFGHIJK", start=1):
            h.poner(f"{col}{r}", f[j])
        h.poner(f"L{r}", ", ".join(cod_brecha(x) for x in re.split(r",\s*", f[11])))

    # Actividad 13: catálogo de proyectos (IT001 = P1.1 ... IT017 = P4.2)
    h = H["Actividad 13"]
    fichas = {f[0]: f for f in T["Fichas de los proyectos de la fase 1"][1:]}
    fases = dict(re.findall(r"^- \*\*(P[234]\.\d) [^*]+\*\* (.+)$", texto, re.M))
    vigencia = {"1": "Fase 1: vigencia 2027", "2": "Fase 2: vigencia 2028", "3": "Fase 3: vigencia 2029", "4": "Fase 4: vigencia 2030"}
    for k, p in enumerate(T["Catálogo de proyectos"][1:]):
        if not p[0]:
            continue  # fila de total
        r = 7 + k
        pid = p[0]
        if pid in fichas:
            desc, sub = f"{fichas[pid][1]}. {fichas[pid][2]}", fichas[pid][3]
        else:
            partes = fases[pid].split(". ")
            desc, sub = partes[0], ". ".join(partes[1:]) or "—"
        lider, involucradas = (p[8].split(" / ") + [""])[:2]
        h.poner(f"A{r}", f"IT{k + 1:03d}")
        h.poner(f"B{r}", f"{pid} {p[1]}")
        h.poner(f"C{r}", desc)
        h.poner(f"D{r}", sub)
        h.poner(f"E{r}", p[2])
        h.poner(f"F{r}", p[3])
        h.poner(f"G{r}", p[4])
        h.poner(f"H{r}", p[5])
        h.poner(f"I{r}", lider)
        h.poner(f"J{r}", involucradas)
        h.poner(f"K{r}", p[9].split(" ")[0])
        h.poner(f"L{r}", vigencia[pid[1]])
        h.poner(f"M{r}", p[10])
        h.poner(f"N{r}", f"COP {p[11]} millones (estimación del equipo)")
        h.poner(f"O{r}", ", ".join(cod_brecha(x) for x in re.split(r",\s*", p[6])))

    # Actividad 14 A: indicadores; 14 B: hojas de vida
    kpis = T["Hojas de vida de los indicadores de TI"][1:]
    meta_por_kpi = {m[3]: m for m in metas}
    h = H["Actividad 14 A"]
    for k, i in enumerate(kpis):
        r = 9 + k
        dominio, categoria = (i[1].split("; ") + [""])[:2]
        h.poner(f"A{r}", i[0])
        h.poner(f"B{r}", dominio)
        h.poner(f"C{r}", categoria.capitalize())
        h.poner(f"D{r}", i[5])
        h.poner(f"E{r}", i[2])
        h.poner(f"F{r}", i[3])
        h.poner(f"G{r}", f"{i[6]}. {i[7]}")
    for fila, txt in ((37, "Mayor o igual que la meta del año"), (38, "Hasta 10 puntos por debajo de la meta (KPI-03: 3; KPI-08: 20; KPI-09: 1)"),
                      (39, "Más abajo que el rango intermedio")):
        h.poner(f"B{fila}", txt)
        h.poner(f"C{fila}", "")
        h.poner(f"D{fila}", "")
    h = H["Actividad 14 B"]
    for k, i in enumerate(kpis):
        r = 8 + k
        m = meta_por_kpi.get(i[0])
        h.poner(f"A{r}", f"IND.ES.{k + 1:02d} ({i[0]})")
        h.poner(f"B{r}", i[2])
        h.poner(f"C{r}", i[3])
        h.poner(f"D{r}", i[5])
        h.poner(f"E{r}", f"{i[6]}. {i[7]}")
        h.poner(f"F{r}", i[4])
        h.poner(f"G{r}", i[8])
        h.poner(f"H{r}", i[13])
        h.poner(f"I{r}", f"2027: {m[5]}; 2028: {m[6]}; 2029: {m[7]}; 2030: {m[8]}" if m else "")
        h.poner(f"J{r}", i[10])
        h.poner(f"K{r}", i[11])
        h.poner(f"L{r}", i[12])
        h.poner(f"M{r}", f"Línea base: {m[4]}. Unidad: {i[9]}" if m else f"Unidad: {i[9]}")

    # Actividad 17: grupos de interés y plan de comunicación
    h = H["Actividad 17"]
    for k, g_ in enumerate(T["Grupos de interés del PETI"][1:]):  # Grupo | Interés | Mensaje
        r = 9 + k
        h.poner(f"A{r}", g_[0])
        h.poner(f"B{r}", g_[1])
        h.poner(f"C{r}", f"Mensaje principal: {g_[2]}")
    acts = T["Plan de comunicación del PETI"][1:]
    for k, a in enumerate(acts):
        r = 24 + k * 3
        if r > 45:
            for off in range(3):
                h.copiar_estilo_fila(45 + off, r + off, "A", "G")
            h.combinar(f"B{r}:B{r + 2}")
            h.descombinar("A23:A47")
            h.combinar(f"A23:A{r + 2}")
        h.poner(f"B{r}", a[0])
        h.poner(f"C{r}", a[1])
        h.poner(f"D{r}", a[2])
        h.poner(f"E{r}", a[3])
        h.poner(f"F{r}", a[4])
        h.poner(f"G{r}", a[5])

    for hoja in H.values():
        hoja.guardar()
    if os.path.exists(salida):
        os.remove(salida)
    with zipfile.ZipFile(ANEXO) as original, zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as z:
        for item in original.infolist():
            z.write(os.path.join(tmp, item.filename), item.filename)
    shutil.rmtree(tmp)
    print("Generado:", salida)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    llenar(sys.argv[1], sys.argv[2])
