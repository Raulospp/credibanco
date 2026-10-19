---
name: guia-peti
description: Usar antes de redactar, completar, reestructurar o auditar cualquier capítulo del PETI, cuando hay que saber qué exige la Guía MGGTI.GE.ES.03 v3.0 del MinTIC, la Plantilla PETI (Anexo 2) o las herramientas del Anexo 1 para una sección o actividad, cuando se pregunta qué falta en el PETI frente a la norma, cómo se llena un formato (catálogo de brechas, catálogo de iniciativas, hoja de vida de indicadores, DOFA, tendencias, plan de comunicaciones), o cómo resolvieron una sección los PETI de referencia de MinCiencias y MinTIC.
argument-hint: "[capítulo, actividad o formato]"
---

# Norma del PETI: guía, plantilla y herramientas del MinTIC

## Principio

El PETI se juzga contra tres documentos que están en `docs/` y que **no se modifican**: la guía (metodología), la plantilla (estructura y contenido mínimo) y el Anexo 1 (formatos de trabajo). Los PETI de MinCiencias y MinTIC son ejemplos de cómo otros los aplicaron, no norma. Cuando esta skill y los documentos originales discrepen, mandan los originales: extráelos con `python .claude/skills/guia-peti/scripts/extraer_referencias.py` y cita la página o la hoja.

La guía se declara "orientación o buena práctica, no obligatoriedad" y admite ajustarla "de acuerdo con las necesidades, madurez tecnológica y capacidades" (§2.2). Mira la naturaleza de la organización en la tabla "Datos del proyecto" de `.claude/CLAUDE.md`:

- **Entidad pública colombiana**: MIPG, FURAG, trámites (SUIT), OPAs, SECOP, Comité Institucional de Gestión y Desempeño y publicación en el sitio web oficial aplican tal cual.
- **Empresa privada u otra naturaleza**: cada uno de esos elementos se **adapta o se declara no aplicable con una razón**, nunca se omite en silencio. Esa adaptación se explica en el numeral de metodología (§4) del PETI.

## Metodología: 4 fases, 17 actividades

| Fase | Actividad | Producto esperado | Herramienta del Anexo 1 |
|---|---|---|---|
| 1. Planear | 1. Conformar equipo e identificar stakeholders | Equipo y stakeholders con rol y capacidad de decisión | Hoja "Actividad 1" |
| | 2. Determinar presupuesto para elaborar el PETI | Presupuesto de elaboración (equipo interno o consultor) | Hoja "Actividad 1" |
| | 3. Plan y cronograma de trabajo | Cronograma por fase con responsables y ruta crítica | Hoja "Actividad 3" |
| 2. Analizar | 4. Comprender el entorno organizacional | Ficha de la entidad (misión, visión, objetivos, metas), procesos de la cadena de valor y su soporte en SI, servicios/trámites/OPAs, normatividad | Hojas 4A, 4B, 4C, 4D |
| | 5. Planes estratégicos externos y compromisos | Lista de planes externos con la obligación de TI y el plazo | Hoja "Actividad 5" |
| | 6. Analizar y diagnosticar la gestión de TI | Diagnóstico por dominio contra el MRAE v3.0 y **DOFA por dominio** | Hoja "Actividad 6" |
| | 7. Tendencias y tecnologías emergentes | Matriz tendencia × servicio/trámite/proceso | Hoja "Actividad 7" |
| 3. Construir | 8. Construir la estrategia de TI | Misión, visión, objetivos de TI (verbo en infinitivo, SMART, perspectivas BSC) y **metas por año con línea base** | Hoja "Actividad 8" |
| | 9. Mejoras en servicios y operación | Matriz de mejoras por servicio o proceso | Anexo 1 (general) |
| | 10. Oportunidades de mejora por dominio | Acciones a mejorar, eliminar o crear por dominio | Anexo 1 (general) |
| | 11. Identificar brechas | **Catálogo de brechas** con acción, justificación, tiempo y costo estimados | Hoja "Actividad 11" |
| | 12. Otros planes de la Política de Gobierno Digital | Iniciativas de otros planes con componente de TI | Hoja "Actividad 12" |
| | 13. Consolidar, priorizar y construir hoja de ruta | **Catálogo de iniciativas y proyectos** agrupando brechas, con objetivo, meta, área líder, tiempo, fecha, costo | Hoja "Actividad 13" |
| | 14. Indicadores de la estrategia de TI | Indicadores por dominio y **hoja de vida** de cada uno | Hojas 14A y 14B |
| | 15. Consolidar el documento PETI | Documento según la plantilla, con anexos | Plantilla + Anexo 1 |
| 4. Socializar | 16. Presentar para aprobación y publicar | Acta de aprobación del comité; publicación | Plantillas institucionales |
| | 17. Socializar el PETI | Plan de comunicaciones: grupos de interés, actividad, canal, formato, responsable, frecuencia | Hoja "Actividad 17" |

La guía exige ejecutar las actividades **en orden** y dice textualmente: "Un plan que no tenga indicadores ni metas no es un plan" (Actividad 14).

Dominios de gestión de TI usados por la guía y la plantilla (MRAE v3.0): **Estrategia de TI, Gobierno de TI, Información, Sistemas de Información, Infraestructura de TI, Uso y Apropiación, Seguridad de la Información**. Toda brecha, iniciativa e indicador se asocia a uno.

Acciones permitidas sobre un elemento (fase Construir): **crear, modificar, mantener o eliminar**. En el catálogo de brechas del Anexo 1 solo aparecen crear, eliminar o modificar.

La Actividad 12 (otros planes de Gobierno Digital) solo aplica tal cual a entidades públicas. En una empresa privada se declara "no aplica" en §4 y su equivalente (compromisos con clientes, casa matriz, reguladores del sector) va en los motivadores (§5.1).

## Archivos de apoyo

- [plantilla-capitulos.md](plantilla-capitulos.md): capítulo por capítulo de la plantilla, contenido mínimo, herramienta asociada y **numeral del PETI donde va** (estructura de 16 numerales de `docs/peti_2026_2028.md`).
- [anexo1-formatos.md](anexo1-formatos.md): columnas exactas de cada hoja del Anexo 1, escalas y ejemplos de indicadores.
- [referentes.md](referentes.md): cómo estructuraron MinCiencias y MinTIC sus PETI y qué patrones conviene imitar.

## Contrato de salida

Cuando esta skill se usa para responder qué exige la norma sobre algo, entrega:

1. **Requisito**: qué pide la guía, la plantilla o el Anexo 1, con la ubicación (sección de la guía, capítulo de la plantilla u hoja del Anexo 1).
2. **Adaptación a la organización**: si aplica tal cual, se adapta (cómo) o no aplica (por qué), según su naturaleza.
3. **Estado en el PETI**: numeral donde está o "sin sección equivalente", con la frase o tabla que lo atiende.
4. **Qué falta**, si se pidió evaluar.

## Señales de alerta

- Un capítulo de la plantilla sin sección equivalente y sin nota de "no aplica".
- Objetivos de TI sin metas por año ni línea base (Actividad 8).
- Brechas o iniciativas sin tiempo ni costo estimado (Actividades 11 y 13).
- Indicadores sin fórmula, fuente de datos, responsable o rangos (Actividad 14B).
- DOFA ausente o consolidada en una sola tabla sin dominio (Actividad 6) o tendencias sin cruzar con servicios o procesos (Actividad 7).
- Citar la guía como "MGGTI.GE.ES.01" (es el nombre del archivo, no el código del documento).
- En una empresa privada: afirmar que el PETI "cumple MIPG" o fue "aprobado por el Comité Institucional de Gestión y Desempeño".
