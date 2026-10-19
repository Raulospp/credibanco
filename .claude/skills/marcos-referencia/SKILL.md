---
name: marcos-referencia
description: Usar cuando el PETI nombra, aplica o mapea un marco o una norma (COBIT 2019, TOGAF, ITIL 4, ISO/IEC 27001:2022, ISO/IEC 42001:2023, NIST CSF 2.0, NIST AI RMF, SOC 2, SOX, MRAE del MinTIC, Política de Gobierno Digital, MIPG, Ley 1581 de 2012 u otras leyes de datos), cuando se redacta el marco normativo (§3), la gobernanza (§13) o el mapeo de controles (Anexo B), cuando hay que decidir si una norma aplica a la organización, se adapta o es solo referencia, o cuando se mapean procesos o controles (APO06, DSS01, 8.28…).
argument-hint: "[marco o norma]"
---

# Marcos y normas del PETI

## Principio

Un marco se cita por lo que exige o aporta al plan, no por su prestigio. Cada mención responde tres preguntas: **qué es** (emisor, versión, año), **qué relación tiene con la organización** (obligatorio, contractual, voluntario, referencia metodológica) y **dónde se usa en el PETI** (numeral, brecha, proyecto, indicador). Lo que no se ha comprobado en el texto oficial se marca `[VERIFICAR]` y no se presenta como cierto. Al verificar algo, quita la marca aquí y registra la fuente en `docs/registro-de-evidencias.md` en el mismo cambio.

## Tres tipos de relación (decídelo antes de escribir)

| Relación | Significa | Ejemplos |
|---|---|---|
| **Obligación legal** | Aplica por ley donde opera la organización | Protección de datos personales; normas del sector (financiero, salud, servicios públicos); para entidades públicas, Gobierno Digital y MIPG |
| **Compromiso voluntario o contractual** | La organización lo adoptó o un cliente o regulador lo exige | ISO/IEC 27001 si está certificada; informes SOC 2 si los entrega a clientes; PCI DSS si procesa tarjetas |
| **Referencia metodológica** | Se usa como guía para construir el plan | Guía y plantilla del MinTIC (si es privada), MRAE, COBIT, TOGAF, ITIL, NIST |

La naturaleza de la organización (tabla "Datos del proyecto" de `.claude/CLAUDE.md`) decide la columna: la guía del MinTIC, el MRAE, MIPG, el Decreto 767 de 2022 y el Decreto 612 de 2018 **obligan a entidades públicas colombianas**; para una empresa privada son referencia metodológica, y el PETI lo dice en §3 y §4.

## Marcos internacionales

| Marco | Emisor y versión | Qué aporta al PETI | Cuidado al citarlo |
|---|---|---|---|
| COBIT 2019 | ISACA, 2018-2019 | Gobierno y gestión de TI: 40 objetivos en 5 dominios (EDM, APO, BAI, DSS, MEA); cascada de metas; diseño del sistema de gobierno. Ej.: EDM01 marco de gobierno, APO05 portafolio, APO06 *Managed Budget and Costs*, APO12 *Managed Risk*, DSS01 *Managed Operations* | Se cita el objetivo por código y nombre. No es certificable para una organización. |
| TOGAF | The Open Group; TOGAF Standard, 10.ª edición (2022) | Método ADM (fase preliminar, A-H y gestión de requisitos) y dominios de arquitectura: negocio, datos, aplicaciones, tecnología | Si el PETI añade "seguridad" como capa, decir que TOGAF la trata como transversal. |
| ITIL 4 | AXELOS/PeopleCert, 2019 | Sistema de valor del servicio y 34 prácticas (gestión de incidentes, de cambios, de niveles de servicio, monitoreo y eventos, mejora continua) | Es buena práctica, no norma. |
| ISO/IEC 27001:2022 | ISO/IEC | SGSI certificable. Anexo A con 93 controles en 4 temas: organizacionales (5.x), personas (6.x), físicos (7.x) y tecnológicos (8.x). Ej.: 5.9 inventario de activos, 5.23 nube, 5.31 requisitos legales, 5.34 privacidad, 8.9 configuración, 8.15 registro de eventos, 8.16 monitoreo, 8.28 codificación segura, 8.29 pruebas de seguridad | El certificado dura 3 años con auditorías de seguimiento anuales y de recertificación al final `[VERIFICAR con el certificado de la organización]`. La transición desde la versión 2013 terminó el 31 de octubre de 2025. Un control A.12 o A.14 es de 2013 y está mal. |
| ISO/IEC 42001:2023 | ISO/IEC, diciembre de 2023 | Sistema de gestión de IA (AIMS) certificable, estructura de sistema de gestión (cláusulas 4-10) y anexo de controles | Número y agrupación de controles del anexo A `[VERIFICAR]`. Solo si la organización usa o desarrolla IA de forma relevante. |
| NIST CSF 2.0 | NIST, febrero de 2024 (CSWP 29) | Funciones Gobernar, Identificar, Proteger, Detectar, Responder, Recuperar; perfiles actual y objetivo (encaja con AS-IS y TO-BE de seguridad) | Voluntario; se adopta, no se certifica. |
| NIST AI RMF 1.0 | NIST, enero de 2023 (NIST AI 100-1) | Funciones Gobernar, Mapear, Medir, Gestionar. Perfil de IA generativa NIST AI 600-1 (julio de 2024) | Voluntario; se adopta, no se certifica. |
| SOC 2 | AICPA | Informe de **atestación** sobre controles según los Trust Services Criteria: seguridad, disponibilidad, integridad del procesamiento, confidencialidad y privacidad. Tipo I (diseño en una fecha) y tipo II (eficacia operativa en un periodo de observación de varios meses) | No es certificación ni acreditación. Solo aplica si la organización presta servicios a clientes que lo exigen. |
| SOX §302/§906 | Congreso de EE. UU., 2002 | Certificación de estados financieros por CEO y CFO de emisores registrados ante la SEC | Solo si la organización o su matriz cotiza en EE. UU. Verificar la condición actual en SEC EDGAR antes de presentarla como obligación. |
| PCI DSS v4.0.1 | PCI Security Standards Council, junio de 2024 (la v4.0 se retiró el 31 de diciembre de 2024) | Seguridad de datos de tarjetas | Solo si almacena, procesa o transmite datos de tarjetas. Se valida con un informe de cumplimiento y un certificado de cumplimiento (AOC); no es una certificación ISO. |
| OWASP Top 10 (web y aplicaciones LLM) | OWASP | Riesgos de aplicaciones web y de aplicaciones con LLM | Citar la edición por año. |

## Marco colombiano

| Documento | Qué es | Entidad pública | Empresa privada |
|---|---|---|---|
| Guía MGGTI.GE.ES.03 v3.0 (nov. 2023) | Metodología de construcción del PETI | Se aplica | Referencia metodológica adaptada. Ver `guia-peti` |
| Plantilla PETI (Anexo 2) y herramientas (Anexo 1) | Estructura del documento y formatos | Se aplican | Ídem |
| MRAE v3.0 | Marco de referencia de arquitectura empresarial del Estado | Obligatorio | Dominios de gestión de TI y lineamientos para el diagnóstico |
| Decreto 767 de 2022 | Política de Gobierno Digital | Obligatorio | Contexto de la plantilla; no obliga |
| Decreto 612 de 2018 | Integración de planes institucionales (incluye el PETI) al plan de acción | Obligatorio | Antecedente |
| Decreto 1078 de 2015, Decreto 1083 de 2015 (MIPG), Decreto 415 de 2016, Ley 1341 de 2009 | Normas que obligan a entidades públicas a tener PETI, área de TI y MIPG | Obligatorias según el tipo de entidad `[VERIFICAR artículos]` | Solo como antecedente |
| MSPI | Modelo de Seguridad y Privacidad de la Información del MinTIC | Obligatorio para entidades del Estado | Instrumento sugerido por la plantilla (6.7) para calificar controles; se puede usar con los temas de ISO 27001 |
| Ley 1581 de 2012 y Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015) | Protección de datos personales; autoridad: SIC | Obligatoria | Obligatoria si trata datos personales en Colombia `[VERIFICAR artículos antes de citarlos]` |
| Ley 1712 de 2014 | Transparencia y acceso a la información pública | Obligatoria | No aplica, salvo que preste funciones públicas |
| Normas del sector financiero | Superintendencia Financiera: Circular Básica Jurídica, reexpedida por la CE 006 de 2025 (vigente desde el 26 de junio de 2025), con los requerimientos de ciberseguridad de las CE 007 de 2018 y 033 de 2020; **Circular Básica Financiera** (CE 004 de 2026), que desde el 1 de junio de 2026 sustituye a la Circular Básica Contable y Financiera (CE 100 de 1995). Verificado el 29 de septiembre de 2026 | Según sector | Obligatorias para entidades vigiladas. Capítulo de ciberseguridad en la CBJ vigente `[VERIFICAR]`. No citar la Circular Básica Contable y Financiera como vigente después del 1 de junio de 2026 |

## Protección de datos en otros países (si la organización opera fuera de Colombia)

| País | Norma principal | Nota |
|---|---|---|
| Argentina | Ley 25.326 de 2000 | `[VERIFICAR vigencia]` |
| Chile | Ley 19.628; Ley 21.719 de 2024 | Fecha de entrada en vigencia `[VERIFICAR en BCN]`: hubo propuestas de aplazamiento |
| México | Nueva LFPDPPP, DOF 20 de marzo de 2025 | `[VERIFICAR]` |
| Perú | Ley 29733 y su reglamento | `[VERIFICAR]` |
| Uruguay | Ley 18.331 de 2008 y modificaciones | `[VERIFICAR]` |
| EE. UU. y UE | CCPA/CPRA, GDPR; Reglamento (UE) 2024/1689 de IA | Solo si hay titulares o clientes allí `[VERIFICAR aplicabilidad]` |

En el PETI basta una fila por país con la norma y la obligación para TI (autorización, finalidad, seguridad, transferencias internacionales, derechos del titular). No se desarrolla doctrina.

## Mapeo del PETI a los marcos (Anexo B)

- Una fila por proceso o control del PETI, con el objetivo COBIT o el control ISO que le corresponde **por código y nombre**. Si no hay correspondencia clara, "—" y no un código forzado.
- ISO 27001 se mapea al Anexo A de 2022 (5.x a 8.x).
- Cada marco del §3 debe aparecer en al menos un proyecto, brecha, indicador o fila del Anexo B.

## Señales de alerta

- "Acreditación SOC 2" o "certificación SOC 2".
- "Certificación NIST" o "cumplimiento NIST" como si fuera auditable.
- SOX, PCI DSS u otra norma presentada como obligación sin comprobar que aplica.
- En empresa privada: "el PETI cumple MIPG" o "de acuerdo con el Decreto 612 la empresa debe…".
- En entidad pública: tratar MIPG, FURAG o el Decreto 612 como simple referencia.
- Controles ISO 27001 con numeración de 2013.
- Un marco en el §3 que no aparece en ningún proyecto, brecha o indicador: o se usa o se retira.
